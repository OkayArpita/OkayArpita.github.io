$files = Get-ChildItem -Path "e:\Job Hunt\GitHub\OkayArpita.github.io\src" -Recurse -Include *.astro

foreach ($file in $files) {
    $content = Get-Content $file.FullName -Raw
    $original = $content
    
    $content = $content -replace 'id="project-cursor-badge"', 'id="project-cursor-badge" style="display:none;"'
    
    # Career.astro has a slightly different setup: initCareerCursor
    $content = $content -replace 'const initCursorBadge = \(\) => \{', 'const initCursorBadge = () => { return;'
    $content = $content -replace 'const initCareerCursor = \(\) => \{', 'const initCareerCursor = () => { return;'

    if ($content -ne $original) {
        Set-Content $file.FullName $content -NoNewline
        Write-Host "Disabled old cursor in $($file.Name)"
    }
}
