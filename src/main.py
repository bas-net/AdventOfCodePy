from types import ModuleType
from downloader.aocdownloader import download_missing_day_inputs
import os
import importlib.util
import re


def prRed(skk): print("\033[91m {}\033[00m" .format(skk))
def prGreen(skk): print("\033[92m {}\033[00m" .format(skk))
def prCyan(skk): print("\033[96m {}\033[00m" .format(skk))


def run_tests(dayModule: ModuleType, year: str, day: str, part: str) -> bool:
    all_tests_green = True

    test_dir = f'./tests/{year}/{day}/{part}'
    test_dir_in = f'{test_dir}/in'
    test_dir_out = f'{test_dir}/out'
    if os.path.exists(test_dir_in):
        for testFile in os.scandir(test_dir_in):
            testName = testFile.name
            testDescr = f'    Test {year}.{day}.{part}.{testName}'

            with open(f'{test_dir_in}/{testName}', 'r') as test_input_file:
                test_input = test_input_file.read()
            with open(f'{test_dir_out}/{testName}', 'r') as test_output_file:
                test_expected_output = test_output_file.read()

            if part == '1':
                test_output = str(dayModule.p1(test_input))
            elif part == '2':
                test_output = str(dayModule.p2(test_input))
            else:
                raise 'Error'

            if test_output == test_expected_output:
                prGreen(testDescr + ' succeeded')
            else:
                all_tests_green = False
                prRed(
                    f'{testDescr} failed. Got \'{test_output}\', expected \'{test_expected_output}\'')

    return all_tests_green


download_missing_day_inputs()

for yearDir in os.scandir('./src/solutions'):
    year = re.findall('y(\d\d\d\d)', yearDir.name)[0]
    for dayFile in os.scandir(f'./src/solutions/{yearDir.name}'):
        if not os.path.isfile(dayFile.path):
            continue
        day = re.findall('d(\d\d).py', dayFile.name)[0]
        daySpec = importlib.util.spec_from_file_location(
            f'{yearDir.name}.{dayFile.name}',
            f'./src/solutions/{yearDir.name}/{dayFile.name}'
        )
        dayModule = importlib.util.module_from_spec(daySpec)
        daySpec.loader.exec_module(dayModule)

        prCyan(f'Running {year}.{day}')

        p1_test_success = run_tests(dayModule, year, day, '1')
        p2_test_success = run_tests(dayModule, year, day, '2')

        with open(f'./inputs/{year}/{day}.txt', 'r') as input_file:
            input_string = input_file.read()

            output_p1 = str(dayModule.p1(input_string))
            if p1_test_success:
                prGreen(f'  {year}.{day}.1 result \'{output_p1}\'')
            else:
                prRed(f'  {year}.{day}.1 result \'{output_p1}\'')

            output_p2 = str(dayModule.p2(input_string))
            if p2_test_success:
                prGreen(f'  {year}.{day}.2 result \'{output_p2}\'')
            else:
                prRed(f'  {year}.{day}.2 result \'{output_p2}\'')
