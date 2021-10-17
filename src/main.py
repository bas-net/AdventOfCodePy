import os
import importlib.util
import re
import json

from types import ModuleType
from enum import Enum

from downloader.aocdownloader import download_missing_day_inputs


def print_red(skk):
    print(f'\033[91m {skk}\033[00m')


def print_green(skk):
    print("\033[92m {}\033[00m" .format(skk))


def print_cyan(skk):
    print("\033[96m {}\033[00m" .format(skk))


def print_yellow(skk):
    print("\033[93m {}\033[00m" .format(skk))


def print_light_purple(skk):
    print("\033[94m {}\033[00m" .format(skk))


class TestStatus(Enum):
    FAIL = 0
    SUCCESS = 1
    NO_TESTS = 2


def run_tests(day_module: ModuleType, year: str, day: str, part: str) -> TestStatus:
    all_tests_green = True
    test_count = 0

    test_dir = f'./tests/{year}/{day}/{part}'
    test_dir_in = f'{test_dir}/in'
    test_dir_out = f'{test_dir}/out'
    if os.path.exists(test_dir_in):
        for testFile in os.scandir(test_dir_in):
            testName = testFile.name
            testDescr = f'    Test {year}.{day}.{part}.{testName}'

            with open(f'{test_dir_in}/{testName}', 'r', encoding='utf-8') as test_input_file:
                test_input = test_input_file.read().strip()
            with open(f'{test_dir_out}/{testName}', 'r', encoding='utf-8') as test_output_file:
                test_expected_output = test_output_file.read().strip()

            if part == '1':
                test_output = str(day_module.p1(test_input))
            elif part == '2':
                test_output = str(day_module.p2(test_input))
            else:
                raise Exception('Error')

            test_count += 1

            if test_output == test_expected_output:
                print_green(testDescr + ' succeeded')
            else:
                all_tests_green = False
                print_red(
                    f'{testDescr} failed. Got \'{test_output}\', expected \'{test_expected_output}\'')

    return TestStatus.FAIL if not all_tests_green else TestStatus.SUCCESS if test_count > 0 else TestStatus.NO_TESTS


def run_day_part(day_module: ModuleType, year: str, day: str, part: str) -> None:
    test_result = run_tests(day_module, year, day, part)

    with open(f'./inputs/{year}/{day}.txt', 'r', encoding='utf-8') as input_file:
        input_string = input_file.read().strip()

        if part == '1':
            output = str(day_module.p1(input_string))
        elif part == '2':
            output = str(day_module.p2(input_string))
        else:
            Exception('Error')

        if test_result == TestStatus.SUCCESS:
            print_green(f'  {year}.{day}.{part} result \'{output}\'')
        elif test_result == TestStatus.FAIL:
            print_red(f'  {year}.{day}.{part} result \'{output}\'')
        else:
            print_yellow(f'  {year}.{day}.{part} result \'{output}\'')


def run_solutions():
    with open('./src/blacklist.json', encoding='utf-8') as blacklist_json:
        blacklist = json.load(blacklist_json)

    for year_dir in os.scandir('./src/solutions'):
        year = re.findall(r'y(\d\d\d\d)', year_dir.name)[0]
        for day_file in os.scandir(f'./src/solutions/{year_dir.name}'):
            if not os.path.isfile(day_file.path):
                continue
            day_matches = re.findall(r'd(\d\d).py', day_file.name)
            # Skip if not a day file.
            if not day_matches:
                continue
            day = day_matches[0]

            daySpec = importlib.util.spec_from_file_location(
                f'{year_dir.name}.{day_file.name}',
                f'./src/solutions/{year_dir.name}/{day_file.name}'
            )
            dayModule = importlib.util.module_from_spec(daySpec)
            daySpec.loader.exec_module(dayModule)

            print_cyan(f'Running {year}.{day}')

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
                print_light_purple(f'  {year}.{day}.1 skipped')

            if run_p2:
                run_day_part(dayModule, year, day, '2')
            else:
                print_light_purple(f'  {year}.{day}.2 skipped')

download_missing_day_inputs()

