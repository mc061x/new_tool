from system.structures.dummyStruct import DummyStruct


class MyList(DummyStruct):
    def __init__(self, object: any) -> None:
        super().__init__()
        self.list = list()
        self.type = object

    def from_json(self, array: list) -> None:
        try:
            for obj in array:
                value = self.type()
                value.from_json(object=obj)
                self.list.append(value)
        except AttributeError:
            self.list = array

    def to_json(self) -> list:
        result = list()
        try:
            for obj in self.list:
                result.append(obj.to_json())
        except AttributeError:
            result = self.list
        return result
