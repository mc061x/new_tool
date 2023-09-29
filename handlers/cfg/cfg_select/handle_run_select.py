from config.runCfg import *
from config.generalCfg import GeneralConfig
from exceptions import *

from handlers.run_util import get_alias, print_aliases

class RunCfgSelector:
    def __init__(self, cfg: GeneralConfig) -> None:
        self.cfg = cfg
    
    def handle(self, command: str) -> None:
        command = command[1:]
        if len(command):
            alias = command[0]
            try:
                check_for_alias(alias=command[0], cfg_list=self.cfg.runCfg.runOptionList)
            except ConfigNotFoundException as exc:
                handle_exception(self.cfg.interfaceCfg.error, exc)
                return
        else:
            alias = get_alias
