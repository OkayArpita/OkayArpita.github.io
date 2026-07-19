$files = Get-ChildItem -Path "e:\Job Hunt\GitHub\OkayArpita.github.io\src" -Recurse -Include *.astro

foreach ($file in $files) {
    $content = Get-Content $file.FullName -Raw
    
    $original = $content

    # Replace Pattern A
    $content = $content -replace "badgeX \+= \(mouseX - badgeX\) \* [0-9.]+;\s*badgeY \+= \(mouseY - badgeY\) \* [0-9.]+;", "badgeX = mouseX;`n      badgeY = mouseY;"
    
    # Replace Pattern B
    $content = $content -replace "const dx = mouseX - badgeX;\s*const dy = mouseY - badgeY;\s*badgeX \+= dx \* [0-9.]+;\s*badgeY \+= dy \* [0-9.]+;", "badgeX = mouseX;`n      badgeY = mouseY;"

    if ($content -ne $original) {
        Set-Content $file.FullName $content -NoNewline
        Write-Host "Updated $($file.Name)"
    }
}
