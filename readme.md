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
`3..9 | %{ New-Item ('./tests/2015/01/1/out/{0:00}.txt' -f $_) }`
