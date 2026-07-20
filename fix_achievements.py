import os

replacements = {
    'src/pages/achievements/hmel.astro': [
        ('> /</span> Achievement', '> /</span> Achievement Overview'),
        ('> /</span> Competition Journey', '> /</span> Competition Journey & Experience'),
        ('> /</span> My Contributions', '> /</span> Competition Journey & Experience'),
        ('> /</span> Winner\'s Experience', '> /</span> Competition Journey & Experience')
    ],
    'src/pages/achievements/technoxian.astro': [
        ('> /</span> Achievement', '> /</span> Achievement Overview'),
        ('> /</span> Challenge', '> /</span> The Challenge')
    ],
    'src/pages/achievements/betic/medha.astro': [
        ('> /</span> Challenge', '> /</span> The Challenge')
    ],
    'src/pages/achievements/betic/medic.astro': [
        ('> /</span> Challenge', '> /</span> The Challenge')
    ],
    'src/pages/achievements/e-yantra/2024-25.astro': [
        ('> /</span> Achievement', '> /</span> Achievement Overview'),
        ('> /</span> Competition Journey', '> /</span> Competition Journey & Experience'),
        ('> /</span> Challenge', '> /</span> The Challenge')
    ],
    'src/pages/achievements/e-yantra/2025-26.astro': [
        ('> /</span> Achievement', '> /</span> Achievement Overview'),
        ('> /</span> Competition Journey', '> /</span> Competition Journey & Experience'),
        ('> /</span> Challenge', '> /</span> The Challenge')
    ]
}

for file, replaces in replacements.items():
    if os.path.exists(file):
        with open(file, 'r', encoding='utf-8') as f:
            content = f.read()
        for old, new in replaces:
            content = content.replace(old, new)
            
            # also replace HTML comments
            old_comment = old.replace('> /</span> ', '<!-- ').replace('\'', '') + ' -->'
            new_comment = new.replace('> /</span> ', '<!-- ') + ' -->'
            content = content.replace(old_comment, new_comment)
            
        with open(file, 'w', encoding='utf-8') as f:
            f.write(content)
print('Achievements headers standardized!')
