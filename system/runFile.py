import subprocess, time, psutil, os, sys

from exceptions import *
from system.config.runCfg import RunConfig
from system.structures.runFileResult import RunFileResult
from system.structures.buildResult import BuildResult


def kill(proc_pid) -> None:
    process = psutil.Process(proc_pid)
    for proc in process.children(recursive=True):
        proc.kill()
    process.kill()


def get_time(timeStart: float):
    return time.perf_counter() - timeStart


def get_memory(process: psutil.Process):
    RAM = process.memory_info().rss
    for child in process.children(recursive=True):
        RAM += child.memory_info().rss
    return RAM

def get_outfile_size(path_to_file: str):
    return os.path.getsize(path_to_file)


class FileRunner:
    def __init__(self, cfg: RunConfig, file_path: str) -> None:
        self.config = cfg
        self.config.format_commands('$FILENAME', file_path)
        self.config.format_run_command()
        self.path_to_file = file_path

    def build(self) -> BuildResult:
        buildCommand = f"{self.config.BuildCommand} {self.config.BuildArgs}"
        timeStart = time.perf_counter()
        with subprocess.Popen(buildCommand, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, shell=True) as proc:
            errors = proc.stdout.read().decode().splitlines()
            timeEnd = time.perf_counter()
        if errors:
            return BuildResult(success=0, errors=errors, time=timeEnd - timeStart)
        return BuildResult(success=1, errors=[], time=timeEnd - timeStart)

    def run(self) -> RunFileResult:
        runCommand = f"ulimit -s {2 * self.config.MemoryLimit} && ulimit -v {2 * self.config.MemoryLimit} && {self.config.RunCommand} {self.config.RunArgs}"
        proc = subprocess.Popen(runCommand, shell=True, stderr=subprocess.PIPE)
        currentTime, timeStart, MAX_RAM = 0, time.perf_counter(), 0
        while proc.poll() is None:
            currentTime = get_time(timeStart=timeStart)
            try:
                p = psutil.Process(proc.pid)
                MAX_RAM = max(MAX_RAM, get_memory(process=p))
                if MAX_RAM >= self.config.MemoryLimit * 1024:
                    kill(proc.pid)
                    raise MemoryLimitExceededException
                if currentTime - timeStart > self.config.TimeLimit:
                    kill(proc.pid)
                    raise TimeLimitExceededException
                if get_outfile_size(self.config.OutputFilePath) >= self.config.output_file_size_limit * 1024:
                    kill(proc.pid)
                    raise OutputFileTooLargeException
            except psutil.NoSuchProcess:
                break
            time.sleep(self.config.RunnerPollTime)
        if proc.poll() != 0:
            raise RuntimeErrorException
        return RunFileResult(run_time=currentTime, run_memory=MAX_RAM, run_returncode=proc.poll())
