# bas-net AoC in Python

## Virtual Env.
https://docs.microsoft.com/en-us/azure/developer/python/configure-local-development-environment?tabs=cmd#use-python-virtual-environments
`.\.venv\Scripts\activate`

https://code.visualstudio.com/docs/python/environments#_manually-specify-an-interpreter

Authenticating via Visual Studio Code

DefaultAzureCredential and VisualStudioCodeCredential can authenticate as the user signed in to Visual Studio Code's Azure Account extension. After installing the extension, sign in to Azure in Visual Studio Code by pressing F1 to open the command palette and running the Azure: Sign In command.

Visual Studio Code Account Sign In

Required to make a new AAD account (like a service account) and use that to sign in.


## Test files
powershell.
`'./tests/2021/01/2/' | %{ $path=$_; 1..1 | %{ @($("$($path)in/{0:00}.txt" -f $_),$("$($path)out/{0:00}.txt" -f $_)) }} | %{ new-item $_  -Force } | Out-Null`

## Day files
```ps
$year = '2021'
$day = '01'
$path = "./src/solutions/y$($year)/d$($day).py"

New-Item -ItemType File -Path $path -Force | Out-Null

"import solutions.y$($year).lib$($year)


def p1(input_string: str) -> str:
    pass


def p2(input_string: str) -> str:
    pass
" -replace "`r`n","`n" -replace "`n","`r`n" | Set-Content -Force -Path $path -NoNewline
```

## Code duplicity
`pylint --disable=all --enable=duplicate-code src/`


## Line count script

With my GitTools module
Run `New-GitLineCountPerCommitFile -IncludePatterns '*.py','*.ps1','*json' -ExcludePatterns '*.vscode*' -OutputFileName 'filecounts.csv'`
