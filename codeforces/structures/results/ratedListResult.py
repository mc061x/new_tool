from codeforces.structures.user import User
from codeforces.structures.dummyStruct import DummyStruct
from system.structures.typelist import my_list


class RatedListResult(DummyStruct):
    def __init__(self, array: list) -> None:
        super().__init__()
        self.rated_list = my_list(User)
        self.rated_list.fill_list(array=array)

        self.list_fill = ['rated_list']