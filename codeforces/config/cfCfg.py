from system.structures.dummyStruct import DummyStruct


class CfConfig(DummyStruct):
    def __init__(self) -> None:
        super().__init__()
        self.handle = str()
        self.friend_handles = list()

        self.current_contest = int()
        self.current_problem = str()

        