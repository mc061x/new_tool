from config.generalCfg import GeneralConfig
from config.runCfg import *
from config.interfaceCfg import InterfaceConfig
from handlers.modify_cfg import modify_cfg
from config.get_config import dump_config
from exceptions import *
import os

def print_aliases(cfg: GeneralConfig):
    attrs = list()
    option: RunConfigOption
    for option in cfg.runCfg.runOptionList.list:
        attrs.append(option.alias)

    mx_name_len = 0
    for name in attrs:
        mx_name_len = max(mx_name_len, len(name))
    for i, attr in enumerate(attrs):
        first = str(i) + ' ' * (1 + int(len(attrs) >= 10) - len(str(i))) + ' | '
        print(cfg.interfaceCfg.system(first), end='')

        second = str(attr) + ' ' * (mx_name_len - len(attr)) 
        print(cfg.interfaceCfg.success(second))

def get_alias(cfg: GeneralConfig):
    print_aliases(cfg)
    print(cfg.interfaceCfg.system('Which config do you want to modify(alias)? > '), end='')
    alias = input().strip()

    check_for_alias(alias, cfg_list=cfg.runCfg.runOptionList)
    return alias

def check_files(cfg: RunSettings):
    fullInputPath = cfg.input_file_path
    if not fullInputPath == '' and (not os.path.exists(fullInputPath) or not os.path.isfile(fullInputPath)):
        raise InvalidAttributeValue(f'Input file at path {fullInputPath} not found')
    
    fullOutputPath =cfg.output_file_path
    if not fullOutputPath == '' and (not os.path.exists(fullOutputPath) or not os.path.isfile(fullOutputPath)):
        raise InvalidAttributeValue(f'Output file at path {fullOutputPath} not found')

def check_changes(cfg: RunSettings):
    check_files(cfg=cfg)
    
    return True

class RunCfgModifier:
    def handle(cfg: GeneralConfig):
        try:
            alias = get_alias(cfg)
        except ConfigNotFoundException as exc:
            handle_exception(cfg.interfaceCfg.error, exc)
            return
        current_option = find_option(alias=alias, cfg_list=cfg.runCfg.runOptionList).option
        current_option = modify_cfg(current_option, cfg.interfaceCfg, check_changes)
        if current_option is None:
            return
        cfg.runCfg.change_run_config(alias=alias, newCfg=current_option)
        dump_config(cfg)