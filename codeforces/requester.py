from codeforces.API import *
from codeforces.structures.header import *
from codeforces.structures.results.hacksResult import HacksResult
from codeforces.structures.results.ratedListResult import RatedListResult
from codeforces.structures.results.standingsResult import StandingsResult
from codeforces.structures.results.ratingResult import RatingResult


class Requester:
    def __init__(self, api: API) -> None:
        self.api = api

    def standings(self, args: dict) -> StandingsResult:
        return StandingsResult(self.api.request(method='contest.standings?', args=args))

    def hacks(self, args: dict) -> HacksResult:
        return HacksResult(self.api.request(method='contest.hacks?', args=args))

    def rated_list(self, args: dict) -> RatedListResult:
        return RatedListResult(self.api.request(method='contest.ratedList?', args=args))

    def rating(self, args: dict) -> RatingResult:
        return RatingResult(self.api.request(method='user.rating?', args=args))

    def to_dict(self, json: dict):
        pass
