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
`'./tests/2015/11/1/' | %{ $path=$_; 1..2 | %{ @($("$($path)in/{0:00}.txt" -f $_),$("$($path)out/{0:00}.txt" -f $_)) }} | %{ new-item $_  -Force } | Out-Null`

## Day files
```ps
$year = '2015'
$day = '11'
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

```ps


# git log --pretty=format:"%H;%cd"

# git ls-tree -r e6313e57e61a1eab332b69a581416d304426ad21 --name-only

# $(git show e6313e57e61a1eab332b69a581416d304426ad21:readme.md) -split "`n" |`
#     % { ('line {0}' -f $_) } 

$header = '"Commit";"Date";"File";"LineCount"' 
$header| Out-File 'filecounts.csv' -Force
# %y-%M-%dT%H:%m:%s
$(git log --pretty=format:"%H;%ad" --date=format:"%Y-%m-%d %H:%M") -split "`n" | `
    # Select -Last 4 | `
    % {
    $split = $($_ -split ";")
    $hash = $split[0]
    $date = $split[1]

    # Write-Host $date

   

    $(git ls-tree -r $hash --name-only) -split "`n" | `
        ? { $_ -notlike '*.txt' } | `
        ? { $_ -notlike '*.json' } | `
        ? { $_ -notlike '*.git*' } | `
        ? { $_ -notlike '*.vscode*' } | `
        ? { $_ -notlike '*.md' } | `
        ? { $_ -notlike '*.pylintrc' } | `
        # ? { $_ -like 'src/solutions/y2015/d01.py' } | `
        % {
        $file = $_
        # Write-Host $file
        
        $nonEmptyLineCount = $($($(git show "$($hash):$($file)") -split "`n") | `
                ? { $_ -and $_.Length -gt 0 } | `
                Measure-Object).Count
        
        @{File = $file; LineCount = $nonEmptyLineCount }
    } | % {
        # Write-Host "L: $_"
        @{Commit = $hash; Date = $date; File = $_.File; LineCount = $_.LineCount }
    } | Select Commit, Date, File, LineCount | `
        ConvertTo-Csv -Delimiter ";"   | `
        ? { $_ -notlike $header } `
    | Out-File 'filecounts.csv' -Append
}

```