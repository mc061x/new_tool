import subprocess, time, psutil

from new_tool.exceptions import *
from new_tool.system.config import RunConfig
from new_tool.system.structures.runFileResult import RunFileResult

class FileRunner:
    def __init__(self, cfg: RunConfig, file_path: str) -> None:
        self.config = cfg
        self.config.format_commands('$FILENAME', file_path)
        self.config.format_run_command()
        self.path_to_file = file_path

    def build(self) -> int:
        buildCommand = f"{self.config.BuildCommand} {self.config.BuildArgs}"
        with subprocess.Popen(buildCommand, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, shell=True) as proc:
            errors = proc.stdout.read().decode().splitlines()
        if (errors != []):
            for line in errors:
                print(line)
            return 0
        return 1

    def kill(self, proc_pid) -> None:
        process = psutil.Process(proc_pid)
        for proc in process.children(recursive=True):
            proc.kill()
        process.kill()
    
    def getMemory(self, process: psutil.Process):
        RAM = process.memory_info().rss
        for child in process.children(recursive=True):
            RAM += child.memory_info().rss
        return RAM
    
    def getTime(self, timeStart: float):
        return time.time() - timeStart

    def run(self) -> RunFileResult:
        runCommand = f"ulimit -s {2 * self.config.MemoryLimit} && ulimit -v {2 * self.config.MemoryLimit} && {self.config.RunCommand} {self.config.RunArgs}"
        proc = subprocess.Popen(runCommand, shell=True, stderr=subprocess.PIPE)
        currentTime, timeStart, MAX_RAM = 0, time.time(), 0
        while proc.poll() is None:
            currentTime = self.getTime(timeStart=timeStart)
            try:
                p = psutil.Process(proc.pid)
                RAM = self.getMemory(process=p)
                MAX_RAM = max(MAX_RAM, RAM)
                if RAM >= self.config.MemoryLimit * 1024:
                    self.kill(proc.pid)
                    raise MemoryLimitExceededException
                if currentTime - timeStart > self.config.TimeLimit:
                    self.kill(proc.pid)
                    raise TimeLimitExceededException
            except psutil.NoSuchProcess:
                break
            # time.sleep(self.config.RunnerPollTime)
        # if proc.poll() != 0:
        #     raise RuntimeErrorException
        return RunFileResult(run_time=currentTime, run_memory=MAX_RAM, run_returncode=proc.poll())