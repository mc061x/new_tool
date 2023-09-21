from text.print_cfg import print_cfg
from config.generalCfg import GeneralConfig
from config.runCfg import find_option, check_for_alias, RunConfigOption
from exceptions import *

class RunCfgPrinter:
    def __init__(self, cfg: GeneralConfig) -> None:
        self.cfg = cfg
    
    def handle(self, command: list):
        if '-a' in command:
            alias: str = str()
            try:
                alias = command[command.index('-a') + 1]
            except IndexError:
                handle_exception(self.cfg.interfaceCfg.error, IndexError('Alias not specified'))
                return
            try:
                check_for_alias(alias=alias, cfg_list=self.cfg.runCfg.runOptionList)
            except ConfigNotFoundException as exc:
                handle_exception(self.cfg.interfaceCfg.error, exc)
                return
            option = find_option(alias=alias, cfg_list=self.cfg.runCfg.runOptionList).option
            print_cfg(cfg=option, intf=self.cfg.interfaceCfg)
        elif '-all' in command:
            option: RunConfigOption
            for option in self.cfg.runCfg.runOptionList.list:
                print(self.cfg.interfaceCfg.error(option.alias))
                print_cfg(cfg=option.option, intf=self.cfg.interfaceCfg)
        elif '-cur' in command:
            print_cfg(cfg=self.cfg.runCfg.currentRunOption, intf=self.cfg.interfaceCfg)
        else:
            print_cfg(cfg=self.cfg.runCfg, intf=self.cfg.interfaceCfg)