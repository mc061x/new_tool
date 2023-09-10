from codeforces.structures.contest import Contest
from system.structures.typelist import my_list
from codeforces.structures.problem import Problem
from codeforces.structures.ranklistRow import RanklistRow
from codeforces.structures.dummyStruct import DummyStruct


class StandingsResult(DummyStruct):
    def __init__(self, json: dict) -> None:
        super().__init__()
        self.contest = Contest()
        self.problems = my_list(Problem)
        self.rows = my_list(RanklistRow)

        self.recursion_fill = ['contest']
        self.list_fill = ['problems', 'rows']

        self.from_json(json=json)
