from system.structures.dummyStruct import DummyStruct


class ApiConfig(DummyStruct):
    def __init__(self) -> None:
        super().__init__()
        self.key = ''
        self.secret = ''
        self.timeout = 10