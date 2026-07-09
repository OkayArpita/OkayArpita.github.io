const fs = require('fs');
const path = require('path');

const dir = 'src/pages/projects';
const files = fs.readdirSync(dir).filter(f => f.endsWith('.astro'));

for (const file of files) {
  const p = path.join(dir, file);
  let content = fs.readFileSync(p, 'utf8');
  
  // Apply all mappings
  // "Technology used", "Tech stacks" -> "Tech Stack"
  content = content.replace(/<\/span>\s*(?:Technology used|Tech stacks)\s*<\/h2>/g, '</span> Tech Stack\n      </h2>');
  
  // "Researched At" -> "Demonstrated At"
  content = content.replace(/<\/span>\s*Researched At\s*<\/h2>/g, '</span> Demonstrated At\n      </h2>');

  // "Hardware details" etc -> "Hardware Stack"
  content = content.replace(/<\/span>\s*Hardware details\s*<\/h2>/g, '</span> Hardware Stack\n      </h2>');

  fs.writeFileSync(p, content);
  
  // Log all h2 tags
  const matches = [...content.matchAll(/<span class="text-accent">\/<\/span>\s*(.*?)\s*<\/h2>/g)];
  console.log(`${file}: ${matches.map(m => m[1].trim()).join(', ')}`);
}
