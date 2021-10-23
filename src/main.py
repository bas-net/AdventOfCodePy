import os
import importlib.util
import json

from types import ModuleType
from enum import Enum

from downloader.aocdownloader import download_missing_day_inputs

from lib import print_red, print_cyan, print_green, print_light_purple, print_yellow, get_solutions


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
        for test_file in os.scandir(test_dir_in):
            test_file_name = test_file.name
            test_name = f'    Test {year}.{day}.{part}.{test_file_name}'

            with open(f'{test_dir_in}/{test_file_name}', 'r', encoding='utf-8') as test_input_file:
                test_input = test_input_file.read().strip()
            with open(f'{test_dir_out}/{test_file_name}', 'r', encoding='utf-8') as test_output_file:
                test_expected_output = test_output_file.read().strip()

            if part == '1':
                test_output = str(day_module.p1(test_input))
            elif part == '2':
                test_output = str(day_module.p2(test_input))
            else:
                raise Exception('Error')

            test_count += 1

            if test_output == test_expected_output:
                print_green(test_name + ' succeeded')
            else:
                all_tests_green = False
                print_red(
                    f'{test_name} failed. Got \'{test_output}\', expected \'{test_expected_output}\'')

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

    for (year_dir_name, day_file_name, year, day) in get_solutions():
        day_spec = importlib.util.spec_from_file_location(
            f'{year_dir_name}.{day_file_name}',
            f'./src/solutions/{year_dir_name}/{day_file_name}'
        )
        day_module = importlib.util.module_from_spec(day_spec)
        day_spec.loader.exec_module(day_module)

        run_p1 = True
        run_p2 = True

        # Handle blacklisting
        if year in blacklist['blacklisted_day_parts']:
            if day in blacklist['blacklisted_day_parts'][year]:
                if '1' in blacklist['blacklisted_day_parts'][year][day]:
                    run_p1 = False
                if '2' in blacklist['blacklisted_day_parts'][year][day]:
                    run_p2 = False

        if run_p1 or run_p2:
            print_cyan(f'Running {year}.{day}')
        else:
            continue

        if run_p1:
            run_day_part(day_module, year, day, '1')
        else:
            print_light_purple(f'  {year}.{day}.1 skipped')

        if run_p2:
            run_day_part(day_module, year, day, '2')
        else:
            print_light_purple(f'  {year}.{day}.2 skipped')


download_missing_day_inputs()

run_solutions()
