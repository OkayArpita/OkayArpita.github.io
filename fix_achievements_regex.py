import os
import re

replacements = {
    'src/pages/achievements/hmel.astro': [
        (r'>\s*/\s*</span>\s*Achievement', '>/</span> Achievement Overview'),
        (r'>\s*/\s*</span>\s*Competition Journey', '>/</span> Competition Journey & Experience'),
        (r'>\s*/\s*</span>\s*My Contributions', '>/</span> Competition Journey & Experience'),
        (r'>\s*/\s*</span>\s*Winner\'s Experience', '>/</span> Competition Journey & Experience')
    ],
    'src/pages/achievements/technoxian.astro': [
        (r'>\s*/\s*</span>\s*Achievement', '>/</span> Achievement Overview'),
        (r'>\s*/\s*</span>\s*Challenge', '>/</span> The Challenge')
    ],
    'src/pages/achievements/betic/medha.astro': [
        (r'>\s*/\s*</span>\s*Challenge', '>/</span> The Challenge')
    ],
    'src/pages/achievements/betic/medic.astro': [
        (r'>\s*/\s*</span>\s*Challenge', '>/</span> The Challenge')
    ],
    'src/pages/achievements/e-yantra/2024-25.astro': [
        (r'>\s*/\s*</span>\s*Achievement', '>/</span> Achievement Overview'),
        (r'>\s*/\s*</span>\s*Competition Journey', '>/</span> Competition Journey & Experience'),
        (r'>\s*/\s*</span>\s*Challenge', '>/</span> The Challenge')
    ],
    'src/pages/achievements/e-yantra/2025-26.astro': [
        (r'>\s*/\s*</span>\s*Achievement', '>/</span> Achievement Overview'),
        (r'>\s*/\s*</span>\s*Competition Journey', '>/</span> Competition Journey & Experience'),
        (r'>\s*/\s*</span>\s*Challenge', '>/</span> The Challenge')
    ]
}

for file, replaces in replacements.items():
    if os.path.exists(file):
        with open(file, 'r', encoding='utf-8') as f:
            content = f.read()
        for old_pattern, new_text in replaces:
            content = re.sub(old_pattern, new_text, content)
            
            # also replace HTML comments
            old_comment_pattern = old_pattern.replace(r'>\s*/\s*</span>\s*', r'<!--\s*').replace(r'\'', r'\'?') + r'\s*-->'
            new_comment_text = new_text.replace('>/</span> ', '<!-- ') + ' -->'
            content = re.sub(old_comment_pattern, new_comment_text, content)
            
        with open(file, 'w', encoding='utf-8') as f:
            f.write(content)
print('Achievements headers standardized properly!')
