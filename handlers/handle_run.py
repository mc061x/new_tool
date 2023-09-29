from exceptions import *
from config.generalCfg import GeneralConfig
from system.runFile import FileRunner
from system.structures.flag import Flag, FlagParser
from config.runCfg import check_for_alias, find_option
import os

run_flags = [Flag('-s', 0), Flag('-c', 1)]

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
        self.parser = FlagParser(run_flags)
        self.samples = False
        self.option = cfg.runCfg.currentRunOption

    def handle_run(self, command: list):
        try:
            command = self.parser.parse_command(command)
        except IndexError as exc:
            handle_exception(self.cfg.interfaceCfg.error, exc)
            return

        flag: Flag
        for flag in self.parser.arg_list:
            if flag.name == '-s' and flag.present:
                self.samples = True
            if flag.name == '-c' and flag.present:
                alias = flag.arg_list[0]
                try:
                    check_for_alias(alias, self.cfg.runCfg.runOptionList)
                except ConfigNotFoundException as exc:
                    handle_exception(self.cfg.interfaceCfg.error, exc)
                    return
                self.option = find_option(alias, self.cfg.runCfg.runOptionList).option
                

        command = command[1:]
        path_to_file = os.path.join(self.cfg.directory, command[0])
        

        try:
            assure_file_exists(path_to_file)
        except FileNotFoundException as exc:
            handle_exception(self.cfg.interfaceCfg.error, exc)
            return

        runner = FileRunner(cfg=self.option, file_path=path_to_file)

        if self.option.build_command + self.option.build_args != '':
            buildResult = runner.build()
            if not buildResult.success:
                print(self.cfg.interfaceCfg.error('Build failed :('))
                buildResult.errors = buildResult.errors[:self.option.buildErrorLines]
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
        try:
            runner.cleanup()
        except:
            return