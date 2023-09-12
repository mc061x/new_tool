from codeforces.config.cfCfg import CfConfig
from codeforces.config.apiCfg import ApiConfig
from system.config.runCfg import RunConfig
from system.structures.configStruct import ConfigStruct


class GeneralConfig(ConfigStruct):
    def __init__(self) -> None:
        super().__init__()
        self.cfConfig = CfConfig()
        self.apiConfig = ApiConfig()
        self.runConfig = RunConfig()
