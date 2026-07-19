$files = @(
    "betic.astro",
    "e-yantra.astro",
    "hmel.astro",
    "technoxian.astro",
    "medha.astro",
    "medic.astro",
    "2024-25.astro",
    "2025-26.astro"
)

$urlMap = @{
    "betic.astro" = "https://www.betic.org/"
    "medha.astro" = "https://www.betic.org/"
    "medic.astro" = "https://www.betic.org/"
    "e-yantra.astro" = "https://www.e-yantra.org/"
    "2024-25.astro" = "https://www.e-yantra.org/"
    "2025-26.astro" = "https://www.e-yantra.org/"
    "hmel.astro" = "https://www.hmel.in/"
    "technoxian.astro" = "https://www.technoxian.com/"
}

$dir = "e:\Job Hunt\GitHub\OkayArpita.github.io\src\pages\achievements"

foreach ($file in $files) {
    $path = Join-Path $dir $file
    if (-not (Test-Path $path)) {
        Write-Host "File not found: $path"
        continue
    }

    $content = Get-Content $path -Raw
    $url = $urlMap[$file]

    # Simple regex to capture the img src
    $pattern = '(?s)<div class="relative group mb-2 reveal-content" style="animation-delay: 100ms;">\s*<div class="balloon-float[^>]+>\s*<img src="([^"]+)"[^>]+>\s*</div>\s*<div class="balloon-float absolute -z-10 top-0 left-0 w-full h-full bg-accent rounded-full blur-\[80px\] opacity-30"></div>\s*</div>'

    if ($content -match $pattern) {
        $imgSrc = $matches[1]
        
        $replacement = @"
    <div class="relative group mb-2 reveal-content" style="animation-delay: 100ms;">
      <a href="$url" target="_blank" rel="noopener noreferrer" class="block cursor-pointer">
        <div class="balloon-float w-40 h-40 md:w-56 md:h-56 rounded-full border-2 border-accent overflow-hidden shadow-[0_0_50px_color-mix(in_srgb,var(--color-accent)_33%,transparent)] bg-background flex items-center justify-center hover:scale-105 transition-transform duration-300">
          <img src="$imgSrc" alt={title} class="w-full h-full object-cover" onerror="this.src='/placeholder.jpeg'; this.onerror=null;" />
        </div>
        <div class="balloon-float absolute -z-10 top-0 left-0 w-full h-full bg-accent rounded-full blur-[80px] opacity-30 group-hover:opacity-60 transition-opacity duration-500"></div>
      </a>
    </div>
"@
        
        $newContent = $content -replace $pattern, $replacement
        Set-Content $path $newContent -NoNewline
        Write-Host "Updated $file"
    } else {
        Write-Host "Pattern not matched in $file"
    }
}
