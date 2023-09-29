from codeforces.structures.contest import Contest
from codeforces.structures.problem import Problem
from codeforces.structures.problemData import ProblemData
from system.structures.typelist import MyList

class ContestData:
    def __init__(self) -> None:
        self.contest = Contest()
        self.problem_list = dict()
        self.problem_data = dict()

        self.current_problem_index = str()