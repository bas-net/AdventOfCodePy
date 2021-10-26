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

    Write-Host ("Checking commit $hash at $date ...")

   

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