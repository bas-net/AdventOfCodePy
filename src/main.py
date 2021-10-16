from downloader.aocdownloader import download_missing_day_inputs
import os
import importlib.util
import re

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
        with open(f'./inputs/{year}/{day}.txt', 'r') as input_file:
            input_string = input_file.read()
            dayModule.p1(input_string)
            dayModule.p2(input_string)
