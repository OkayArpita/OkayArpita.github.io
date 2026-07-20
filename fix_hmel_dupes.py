import os
import re

with open('src/pages/achievements/hmel.astro', 'r', encoding='utf-8') as f:
    c = f.read()

# I want to find the SECOND occurrence of Competition Journey & Experience header and remove it.
matches = list(re.finditer(r'<!-- Competition Journey & Experience -->.*?</h2>', c, re.DOTALL))
if len(matches) > 1:
    c = c[:matches[1].start()] + '<!-- My Contributions -->' + c[matches[1].end():]

with open('src/pages/achievements/hmel.astro', 'w', encoding='utf-8') as f:
    f.write(c)

print('done')
