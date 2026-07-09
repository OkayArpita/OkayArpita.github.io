const fs = require('fs');
const path = require('path');

function walk(dir) {
  fs.readdirSync(dir).forEach(file => {
    const p = path.join(dir, file);
    if (fs.statSync(p).isDirectory()) walk(p);
    else if (p.endsWith('.astro')) {
      let content = fs.readFileSync(p, 'utf8');
      if (content.includes('\u2014') || content.includes('\u2013')) {
        content = content.replace(/\u2014/g, '-');
        content = content.replace(/\u2013/g, '-');
        fs.writeFileSync(p, content, 'utf8');
        console.log(`Replaced dashes in ${p}`);
      }
    }
  });
}
walk('src');
