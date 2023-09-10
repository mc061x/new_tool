from codeforces.structures.hacks import Hack
from system.structures.typelist import my_list
from codeforces.structures.dummyStruct import DummyStruct


class HacksResult(DummyStruct):
    def __init__(self, json: list) -> None:
        super().__init__()
        self.hack_list = my_list(Hack)
        self.hack_list.fill_list(array=json)
        # self.from_json(json=json)

        self.list_fill = ['hack_list']