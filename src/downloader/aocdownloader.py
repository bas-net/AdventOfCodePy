import re
import urllib.parse
import os
import sys

from typing import Tuple
from configparser import ConfigParser
from requests.sessions import Session

from azure.keyvault.secrets import SecretClient, KeyVaultSecret
from azure.identity import VisualStudioCodeCredential

from lib import get_solutions


def get_config() -> ConfigParser:
    cfg = ConfigParser()

    cfg.read('config.ini')

    if len(cfg.sections()) == 0:
        cfg['keyvault'] = {}
        cfg['keyvault']['keyvaultname'] = '< keyvaultname >'
        cfg['keyvault']['githubusernamesecretname'] = '< githubusernamesecretname >'
        cfg['keyvault']['githubpasswordsecretname'] = '< githubpasswordsecretname >'
        with open('config.ini', 'w', encoding='utf-8') as configfile:
            cfg.write(configfile)
        print('Config file created, please configure and re-run.')
        sys.exit()

    return cfg


def get_keyvaultname(cfg: ConfigParser) -> str:
    return cfg['keyvault'].get('keyvaultname')


def get_githubusernamesecretname(cfg: ConfigParser) -> str:
    return cfg['keyvault'].get('githubusernamesecretname')


def get_githubpasswordsecretname(cfg: ConfigParser) -> str:
    return cfg['keyvault'].get('githubpasswordsecretname')


def get_keyvauluri(cfg: ConfigParser) -> str:
    return f"https://{get_keyvaultname(cfg)}.vault.azure.net"


def get_github_secrets() -> Tuple[KeyVaultSecret, KeyVaultSecret]:
    credential = VisualStudioCodeCredential()

    key_vault_uri = get_keyvauluri(get_config())

    client = SecretClient(vault_url=key_vault_uri, credential=credential)

    github_user_name_secret = client.get_secret(
        get_githubusernamesecretname(
            get_config()))
    github_password_secret = client.get_secret(
        get_githubpasswordsecretname(
            get_config()))

    return (github_user_name_secret, github_password_secret)


def authenticate_session() -> Session:
    print('Authenticating session with GitHub.')

    (uns, pws) = get_github_secrets()

    session = Session()

    response = session.get('https://adventofcode.com/auth/github')

    authenticity_token = re.findall(
        '"authenticity_token" value="([^"]+)"', response.text)[0]
    timestamp_secret = re.findall(
        '"timestamp_secret" value="([^"]+)"', response.text)[0]
    client_id = re.findall(
        'client_id=([^&]+)', response.url)[0]
    return_to = urllib.parse.unquote(
        re.findall('return_to=([^&]+)', response.url)[0])

    # Make the authentication request.
    session.post('https://github.com/session', data={
        'login': uns.value,
        'password': pws.value,
        'authenticity_token': authenticity_token,
        'return_to': return_to,
        'client_id': client_id,
        'timestamp_secret': timestamp_secret,
        'commit': 'Sign in'
    })

    return session


def download_day_input(session: Session, year: int, day: int) -> None:
    print(f'Downloading {year}.{day}...')

    input_request = session.get(
        f'https://adventofcode.com/{year}/day/{day}/input')

    if not os.path.exists(f'./inputs/{year}'):
        os.makedirs(f'./inputs/{year}')

    with open(f'./inputs/{year}/{day:02}.txt', 'w', encoding='utf-8') as input_file:
        input_file.write(input_request.text)
        print(input_file.name)


def download_missing_day_inputs() -> None:
    to_download_inputs = []

    for (_, _, year, day) in get_solutions():
        if not os.path.exists(f'./inputs/{year}/{day}.txt'):
            print(f'Adding input {year}.{day} to the download queue.')
            to_download_inputs.append((int(year), int(day)))

    if len(to_download_inputs) > 0:
        print('Downloading...')
        session = authenticate_session()
        for to_download in to_download_inputs:
            download_day_input(session, to_download[0], to_download[1])
