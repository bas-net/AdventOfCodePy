from types import ModuleType
from downloader.aocdownloader import download_missing_day_inputs
from enum import Enum
import os
import importlib.util
import re
import json


def prRed(skk): print("\033[91m {}\033[00m" .format(skk))
def prGreen(skk): print("\033[92m {}\033[00m" .format(skk))
def prCyan(skk): print("\033[96m {}\033[00m" .format(skk))
def prYellow(skk): print("\033[93m {}\033[00m" .format(skk))
def prLightPurple(skk): print("\033[94m {}\033[00m" .format(skk))

class TestStatus(Enum):
    FAIL = 0,
    SUCCESS = 1,
    NO_TESTS = 2,


def run_tests(dayModule: ModuleType, year: str, day: str, part: str) -> TestStatus:
    all_tests_green = True
    test_count = 0

    test_dir = f'./tests/{year}/{day}/{part}'
    test_dir_in = f'{test_dir}/in'
    test_dir_out = f'{test_dir}/out'
    if os.path.exists(test_dir_in):
        for testFile in os.scandir(test_dir_in):
            testName = testFile.name
            testDescr = f'    Test {year}.{day}.{part}.{testName}'

            with open(f'{test_dir_in}/{testName}', 'r') as test_input_file:
                test_input = test_input_file.read().strip()
            with open(f'{test_dir_out}/{testName}', 'r') as test_output_file:
                test_expected_output = test_output_file.read().strip()

            if part == '1':
                test_output = str(dayModule.p1(test_input))
            elif part == '2':
                test_output = str(dayModule.p2(test_input))
            else:
                raise 'Error'

            test_count += 1

            if test_output == test_expected_output:
                prGreen(testDescr + ' succeeded')
            else:
                all_tests_green = False
                prRed(
                    f'{testDescr} failed. Got \'{test_output}\', expected \'{test_expected_output}\'')

    return TestStatus.FAIL if not all_tests_green else TestStatus.SUCCESS if test_count > 0 else TestStatus.NO_TESTS


def run_day_part(dayModule: ModuleType, year: str, day: str, part: str) -> None:
    test_result = run_tests(dayModule, year, day, part)

    with open(f'./inputs/{year}/{day}.txt', 'r') as input_file:
        input_string = input_file.read().strip()

        if part == '1':
            output = str(dayModule.p1(input_string))
        elif part == '2':
            output = str(dayModule.p2(input_string))
        else:
            raise 'Error'

        if test_result == TestStatus.SUCCESS:
            prGreen(f'  {year}.{day}.{part} result \'{output}\'')
        elif test_result == TestStatus.FAIL:
            prRed(f'  {year}.{day}.{part} result \'{output}\'')
        else:
            prYellow(f'  {year}.{day}.{part} result \'{output}\'')


download_missing_day_inputs()

with open('./src/blacklist.json') as blacklist_json:
    blacklist = json.load(blacklist_json)

for yearDir in os.scandir('./src/solutions'):
    year = re.findall('y(\d\d\d\d)', yearDir.name)[0]
    for dayFile in os.scandir(f'./src/solutions/{yearDir.name}'):
        if not os.path.isfile(dayFile.path):
            continue
        dayMatches = re.findall('d(\d\d).py', dayFile.name)
        # Skip if not a day file.
        if not dayMatches:
            continue
        day = dayMatches[0]

        daySpec = importlib.util.spec_from_file_location(
            f'{yearDir.name}.{dayFile.name}',
            f'./src/solutions/{yearDir.name}/{dayFile.name}'
        )
        dayModule = importlib.util.module_from_spec(daySpec)
        daySpec.loader.exec_module(dayModule)

        prCyan(f'Running {year}.{day}')

        run_p1 = True
        run_p2 = True

        # Handle blacklisting
        if year in blacklist['blacklisted_day_parts']:
            if day in blacklist['blacklisted_day_parts'][year]:
                if '1' in blacklist['blacklisted_day_parts'][year][day]:
                    run_p1 = False
                if '2' in blacklist['blacklisted_day_parts'][year][day]:
                    run_p2 = False

        if run_p1:
            run_day_part(dayModule, year, day, '1')
        else:
            prLightPurple(f'  {year}.{day}.1 skipped')
        
        if run_p2:
            run_day_part(dayModule, year, day, '2')
        else:
            prLightPurple(f'  {year}.{day}.2 skipped')
