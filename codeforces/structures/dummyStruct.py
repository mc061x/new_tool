class DummyStruct:
    def __init__(self) -> None:
        self.recursion_fill = list()
        self.list_fill = list()
        pass

    def from_json(self, json: dict):
        attr_list, key_list = self.__dict__.keys(), json.keys()
        for attr in attr_list:
            if attr in key_list:
                if attr in self.list_fill:
                    new_value = getattr(self, attr)
                    new_value.fill_list(json[attr])
                    setattr(self, attr, new_value)
                elif attr in self.recursion_fill:
                    new_value = getattr(self, attr)
                    new_value.from_json(json[attr])
                    setattr(self, attr, new_value)
                else:
                    setattr(self, attr, json[attr])
