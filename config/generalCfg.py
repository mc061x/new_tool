from config.cfCfg import CfConfig
from config.apiCfg import ApiConfig
from config.runCfg import RunCfg
from system.structures.configStruct import ConfigStruct


class GeneralConfig(ConfigStruct):
    def __init__(self) -> None:
        super().__init__()
        self.cfConfig = CfConfig()
        self.apiConfig = ApiConfig()
        self.runCfg = RunCfg()
