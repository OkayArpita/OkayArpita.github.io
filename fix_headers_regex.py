import os
import re

replacements = {
    'src/pages/projects/blood-smear.astro': [
        (r'>\s*/\s*</span>\s*Engineering Challenges', '>/</span> Engineering Context & Challenges'),
        (r'>\s*/\s*</span>\s*Proof-of-Concept Results', '>/</span> Results & Contributions'),
        (r'>\s*/\s*</span>\s*Recognition', '>/</span> Certificates & Recognition'),
        (r'>\s*/\s*</span>\s*Certificate', '>/</span> Certificates & Recognition')
    ],
    'src/pages/projects/line-follower.astro': [
        (r'>\s*/\s*</span>\s*Engineering Challenges & Key Learnings', '>/</span> Engineering Context & Challenges'),
        (r'>\s*/\s*</span>\s*Certificate', '>/</span> Certificates & Recognition')
    ],
    'src/pages/projects/maze-solver.astro': [
        (r'>\s*/\s*</span>\s*Key Engineering Contributions', '>/</span> Results & Contributions'),
        (r'>\s*/\s*</span>\s*Competition Achievement', '>/</span> Results & Contributions'),
        (r'>\s*/\s*</span>\s*Certificate', '>/</span> Certificates & Recognition')
    ],
    'src/pages/projects/posture-belt.astro': [
        (r'>\s*/\s*</span>\s*Development Phases', '>/</span> Engineering Context & Challenges'),
        (r'>\s*/\s*</span>\s*Recognition', '>/</span> Certificates & Recognition'),
        (r'>\s*/\s*</span>\s*Certificates', '>/</span> Certificates & Recognition')
    ],
    'src/pages/projects/scanner.astro': [
        (r'>\s*/\s*</span>\s*Engineering Context', '>/</span> Engineering Context & Challenges'),
        (r'>\s*/\s*</span>\s*Recognition', '>/</span> Certificates & Recognition'),
        (r'>\s*/\s*</span>\s*Certificate', '>/</span> Certificates & Recognition')
    ],
    'src/pages/projects/balancing-bot.astro': [
        (r'>\s*/\s*</span>\s*Certificates', '>/</span> Certificates & Recognition')
    ],
    'src/pages/projects/infusion.astro': [
        (r'>\s*/\s*</span>\s*Certificates', '>/</span> Certificates & Recognition')
    ],
    'src/pages/projects/oph.astro': [
        (r'>\s*/\s*</span>\s*Certificate', '>/</span> Certificates & Recognition')
    ],
}

for file, replaces in replacements.items():
    if os.path.exists(file):
        with open(file, 'r', encoding='utf-8') as f:
            content = f.read()
        for old_pattern, new_text in replaces:
            content = re.sub(old_pattern, new_text, content)
            
            # also replace HTML comments
            old_comment_pattern = old_pattern.replace(r'>\s*/\s*</span>\s*', r'<!--\s*') + r'\s*-->'
            new_comment_text = new_text.replace('>/</span> ', '<!-- ') + ' -->'
            content = re.sub(old_comment_pattern, new_comment_text, content)
            
        with open(file, 'w', encoding='utf-8') as f:
            f.write(content)
print('Project headers standardized properly!')
