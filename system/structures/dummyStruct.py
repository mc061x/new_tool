class DummyStruct:
    def __init__(self) -> None:
        pass

    def from_json(self, object: list | dict) -> None:
        attr_list, key_list = self.__dict__.keys(), object.keys()
        for attr in attr_list:
            if attr in key_list:
                try:
                    new_value = getattr(self, attr)
                    new_value.from_json(object[attr])
                    setattr(self, attr, new_value)
                except AttributeError:
                    setattr(self, attr, object[attr])

    def to_json(self) -> list | dict:
        attr_list = self.__dict__.keys()

        result = dict()
        for attr in attr_list:
            value = getattr(self, attr)
            if hasattr(value, 'to_json'):
                result[attr] = value.to_json()
            else:
                result[attr] = value
        return result
