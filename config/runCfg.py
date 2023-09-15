from system.structures.typelist import MyList
from system.structures.configStruct import ConfigStruct
from system.config.runSettings import RunSettings
from system.config.runConfigOption import RunConfigOption
from exceptions import *
from copy import deepcopy


def check_for_alias(alias: str, cfg_list: MyList) -> None:
    option: RunConfigOption
    for option in cfg_list.list:
        if option.alias == alias:
            return
    raise ConfigNotFoundException


def check_for_last_config(cfg_list: MyList) -> None:
    if len(cfg_list.list) == 1:
        raise CannotLeaveEmptyConfigListException


def find_option(alias: str, cfg_list: MyList) -> RunConfigOption:
    option: RunConfigOption
    for option in cfg_list.list:
        if option.alias == alias:
            return option


class RunCfg(ConfigStruct):
    def __init__(self):
        super().__init__()
        self.runOptionList = MyList(RunConfigOption)
        self.currentRunOption = RunSettings()
        self.currentRunAlias = 'main'

        self.add_run_option(new_alias='main')

    def add_run_option(self, new_alias: str, copy_from: str = -1):
        if copy_from != -1:
            check_for_alias(copy_from, self.runOptionList)

            current_option = find_option(alias=copy_from, cfg_list=self.runOptionList)

            self.runOptionList.list.append(
                deepcopy(RunConfigOption(alias=new_alias, configOption=current_option.option)))

        else:
            self.runOptionList.list.append(deepcopy(RunConfigOption(alias=new_alias, configOption=RunSettings())))

    def remove_run_config(self, alias: str):
        check_for_alias(alias=alias, cfg_list=self.runOptionList)
        check_for_last_config(cfg_list=self.runOptionList)

        current_option = find_option(alias=alias, cfg_list=self.runOptionList)
        self.runOptionList.list.remove(current_option)

        if self.runOptionList == current_option.alias:
            first_option: RunConfigOption = self.runOptionList.list[0]

            self.currentRunAlias = first_option.alias
            self.currentRunOption = first_option.option

    def modify_run_config(self, alias: str, attr: str, new_value: str):
        check_for_alias(alias=alias, cfg_list=self.runOptionList)

        current_option = find_option(alias=alias, cfg_list=self.runOptionList)
        current_option.option.change_attribute(attr, new_value)

        if current_option.alias == self.currentRunAlias:
            self.currentRunOption.change_attribute(attr, new_value)
