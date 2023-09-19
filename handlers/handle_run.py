from exceptions import *
from config.generalCfg import GeneralConfig
from system.runFile import FileRunner
import os

def assure_file_exists(file_path: str):
    if os.path.exists(file_path):
        return
    raise FileNotFoundException(f'File {file_path} not found in the current directory')

def format_command(command: str):
    formatted = command.split()
    formatted.remove('run')
    return formatted

class RunHandler:
    def __init__(self, cfg: GeneralConfig) -> None:
        self.cfg = cfg

    def handle_run(self, command: list):
        command = command[1:]
        path_to_file = command[0]

        try:
            assure_file_exists(path_to_file)
        except FileNotFoundException as exc:
            handle_exception(self.cfg.interfaceCfg.error, exc)
            return

        runner = FileRunner(cfg=self.cfg.runCfg.currentRunOption, file_path=path_to_file)

        if self.cfg.runCfg.currentRunOption.build_command + self.cfg.runCfg.currentRunOption.build_args != '':
            buildResult = runner.build()
            if not buildResult.success:
                print(self.cfg.interfaceCfg.error('Build failed :('))
                buildResult.errors = buildResult.errors[:10]
                for i in buildResult.errors:
                    print(i)
                return

            print(self.cfg.interfaceCfg.success(f'Build finished successfully in {buildResult.time}s'))

        try:
            runResult = runner.run(self.cfg.unix)
        except TimeLimitExceededException as exc:
            handle_exception(self.cfg.interfaceCfg.error, exc)
            return
        except MemoryLimitExceededException as exc:
            handle_exception(self.cfg.interfaceCfg.error, exc)
            return
        except RuntimeErrorException as exc:
            handle_exception(self.cfg.interfaceCfg.error, exc)
            return

        print(self.cfg.interfaceCfg.success(f'Run finished successfully with code {runResult.returncode}'))
        print(self.cfg.interfaceCfg.system(f'Time : {runResult.time}s | Memory : {runResult.memory / 1024}KB'))
        runner.cleanup()