from new_tool.codeforces.config.cfCfg import CfConfig
from new_tool.system.config.apiCfg import ApiConfig
from new_tool.system.config.runCfg import RunConfig

class GeneralConfig:
    def __init__(self) -> None:
        self.cfConfig = CfConfig()
        self.apiConfig = ApiConfig()
        self.runConfig = RunConfig()
