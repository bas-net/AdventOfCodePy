from types import ModuleType
from downloader.aocdownloader import download_missing_day_inputs
from enum import Enum
import os
import importlib.util
import re


def prRed(skk): print("\033[91m {}\033[00m" .format(skk))
def prGreen(skk): print("\033[92m {}\033[00m" .format(skk))
def prCyan(skk): print("\033[96m {}\033[00m" .format(skk))
def prYellow(skk): print("\033[93m {}\033[00m" .format(skk))


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


download_missing_day_inputs()

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

        p1_test_result = run_tests(dayModule, year, day, '1')
        p2_test_result = run_tests(dayModule, year, day, '2')

        with open(f'./inputs/{year}/{day}.txt', 'r') as input_file:
            input_string = input_file.read().strip()

            output_p1 = str(dayModule.p1(input_string))
            if p1_test_result == TestStatus.SUCCESS:
                prGreen(f'  {year}.{day}.1 result \'{output_p1}\'')
            elif p1_test_result == TestStatus.FAIL:
                prRed(f'  {year}.{day}.1 result \'{output_p1}\'')
            else:
                prYellow(f'  {year}.{day}.1 result \'{output_p1}\'')

            output_p2 = str(dayModule.p2(input_string))
            if p2_test_result == TestStatus.SUCCESS:
                prGreen(f'  {year}.{day}.2 result \'{output_p2}\'')
            elif p2_test_result == TestStatus.FAIL:
                prRed(f'  {year}.{day}.2 result \'{output_p2}\'')
            else:
                prYellow(f'  {year}.{day}.2 result \'{output_p2}\'')
