from config.generalCfg import GeneralConfig
from handlers.cfg.cfg_edit.handle_run_edit import RunCfgModifier
from handlers.cfg.cfg_print.handle_run_print import RunCfgPrinter

from text.print_cfg import print_cfg

class RunCfgHandler:
    def __init__(self, cfg: GeneralConfig) -> None:
        self.cfg = cfg
    
    def handle(self, command: list) -> None:
        command = command[1:]

        if command[0] == 'edit':
            RunCfgModifier(cfg=self.cfg).handle(cfg=self.cfg, command=command)
            return
    
        if command[0] == 'print':
            RunCfgPrinter(cfg=self.cfg).handle(command)
            return
