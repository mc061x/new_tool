from system.structures.dummyStruct import DummyStruct
from exceptions import *

def convert(new_value, old_value) -> any:
    if type(old_value) == list:
        result = list()
        for element in new_value.split():
            result.append(element.strip())
        return result
    
    try:
        return type(old_value)(new_value)
    except ValueError:
        raise WrongAttributeTypeException

class ConfigStruct(DummyStruct):
    def __init__(self):
        super().__init__()

    def change_attribute(self, attr_name, new_value):
        try:
            old_value = getattr(self, attr_name)
        except AttributeError:
            raise ConfigAttributeNotFoundException

        new_value = convert(new_value=new_value, old_value=old_value)

        setattr(self, attr_name, new_value)
