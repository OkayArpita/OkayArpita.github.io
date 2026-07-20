import re
import os

# fix blood-smear
with open('src/pages/projects/blood-smear.astro', 'r', encoding='utf-8') as f:
    c = f.read()
# Replace the second 'Certificates & Recognition' header
c = c.replace('<!-- Certificates & Recognition -->\n    <div class="space-y-4">\n      <h2 class="text-2xl md:text-3xl font-heading font-bold text-maintext flex items-center gap-3">\n        <span class="text-accent">/</span> Certificates & Recognition\n      </h2>', '<!-- Certificates -->\n    <div class="space-y-4">')
with open('src/pages/projects/blood-smear.astro', 'w', encoding='utf-8') as f:
    f.write(c)

# fix posture-belt
with open('src/pages/projects/posture-belt.astro', 'r', encoding='utf-8') as f:
    c = f.read()
c = c.replace('<!-- Certificates & Recognition -->\n    <div class="space-y-4">\n      <h2 class="text-2xl md:text-3xl font-heading font-bold text-maintext flex items-center gap-3">\n        <span class="text-accent">/</span> Certificates & Recognition\n      </h2>', '<!-- Certificates -->\n    <div class="space-y-4">')
with open('src/pages/projects/posture-belt.astro', 'w', encoding='utf-8') as f:
    f.write(c)

# fix maze-solver
with open('src/pages/projects/maze-solver.astro', 'r', encoding='utf-8') as f:
    c = f.read()
c = c.replace('<!-- Results & Contributions -->\n    <div class="space-y-4">\n      <h2 class="text-2xl md:text-3xl font-heading font-bold text-maintext flex items-center gap-3">\n        <span class="text-accent">/</span> Results & Contributions\n      </h2>', '<!-- Competition Achievement -->\n    <div class="space-y-4">')
with open('src/pages/projects/maze-solver.astro', 'w', encoding='utf-8') as f:
    f.write(c)

print('Duplicate headers merged!')
