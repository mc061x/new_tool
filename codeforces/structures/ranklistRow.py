from codeforces.structures.party import Party
from codeforces.structures.dummyStruct import DummyStruct
from system.structures.typelist import my_list
from codeforces.structures.problemResult import ProblemResult


class RanklistRow(DummyStruct):
    def __init__(self) -> None:
        super().__init__()
        self.party = Party()
        self.rank = int()
        self.points = float()
        self.penalty = int()
        self.successfulHackCount = int()
        self.unsuccessfulHackCount = int()
        self.problemResults = my_list(ProblemResult)
        self.lastSubmissionTimeSeconds = int()

        self.recursion_fill = ['party']
        self.list_fill = ['problemResults']
