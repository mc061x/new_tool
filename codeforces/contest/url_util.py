main_link = 'https://codeforces.com'
safe_link = 'https://m1.codeforces.com'

def get_contest_url(contestId: str, safeLink: bool = False):
    if not safeLink:
        return f'{main_link}/contest/{contestId}'
    return f'{safe_link}/contest/{contestId}'

def get_all_statements_url(contestId: str, safeLink: bool = False):
    if not safeLink:
        return f'{main_link}/contest/{contestId}/problems'
    return f'{safe_link}/contest/{contestId}/problems'


 
