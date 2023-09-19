from config.generalCfg import GeneralConfig
from handlers.cfg_edit.general import GeneralCfgModifier
from handlers.cfg_edit.run import RunCfgModifier

class CfgHandler:
    def __init__(self, cfg: GeneralConfig) -> None:
        self.cfg = cfg
    
    def handle(command: str) -> None:
        command = command[1:]
        if command[0] == 'run':
            