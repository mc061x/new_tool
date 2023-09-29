from io import TextIOWrapper
from bs4 import BeautifulSoup as BS
from bs4 import Tag
import requests, os
from codeforces.API import API
from exceptions import *

from codeforces.contest.url_util import get_all_statements_url
from codeforces.structures.problemData import ProblemData

tmp_file_name = 'tool-temp-file.tmp'

def getProblemsHtml(api: API, contestId: str):
    page = api.page_request(get_all_statements_url(contestId=contestId))
    html = BS(page, 'html.parser')
    return html

def parseProblemIds(html : BS):
    return [j['problemindex'] for j in html.select('.problemindexholder')]

def transfer_data(testcase_data: Tag, file: TextIOWrapper):
    for element in testcase_data:
        print(element.stripped_strings, file=file)

def parseStream(section_html : BS, stream: str):
    for testcase in section_html.select(f'.{stream} > pre'):
        tmp_file = open(tmp_file_name, 'w')
        transfer_data(testcase, tmp_file)
        tmp_file.close()
        

def parseProblemInput(html: BS, index: str):
    problem_section = html.select_one(f'div[problemindex=\"{index}\"]')

    stream = 'input'

    for testcase in problem_section.select(f'.{stream} > pre'):
        tmp_file = open(tmp_file_name, 'r')

def parseProblemData(html : BS):
    try:
        createFile = open(tmp_file_name, 'x')
        createFile.close()
    except FileExistsError:
        pass
    problem_data = dict()
    for problem in parseProblemIds(html):
        current_problem = ProblemData()
        problem_section = html.select_one(f'div[problemindex=\"{problem}\"]')
        for stream in ['input', 'output']:
            for testcase in problem_section.select(f'.{stream} > pre'):
                current_file = open(tmp_file_name, 'w')
                for element in testcase:
                    for i in element.stripped_strings:
                        print(i, file=current_file)
                current_file.close()
                current_file = open(tmp_file_name, 'r')
                if stream == 'input':
                    current_problem.input = current_file.read()
                else:
                    current_problem.output.append([j.strip() for j in current_file.readlines()])
                current_file.close()
        interactive = False
        for i in problem_section.select('.section-title'):
            current_problem.interactive |= 'Interaction' in i
        problem_data[problem]['Interactive'] = interactive
    os.remove(tmp_file_name)
    return problem_data