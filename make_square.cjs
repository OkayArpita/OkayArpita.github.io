const fs = require('fs');
const path = require('path');

const dir = 'src/pages/projects';
const files = fs.readdirSync(dir).filter(f => f.endsWith('.astro'));

for (const file of files) {
  const p = path.join(dir, file);
  let content = fs.readFileSync(p, 'utf8');
  
  // Replace the rectangular frame class with a square frame class.
  // The original has 'w-32 h-24' or similar. Let's find 'w-32 h-24' inside the flex-shrink-0 div.
  // We'll replace 'w-32 h-24' with 'w-24 h-24' to make it a perfect square.
  const updated = content.replace(
    /class="flex-shrink-0 bg-white w-32 h-24 rounded-xl/g,
    'class="flex-shrink-0 bg-white w-24 h-24 rounded-xl'
  );
  
  if (content !== updated) {
    fs.writeFileSync(p, updated);
    console.log(`Updated ${file}`);
  }
}
