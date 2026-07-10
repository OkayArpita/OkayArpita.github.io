const fs = require('fs');
const path = require('path');

const dir = 'src/pages/projects';
const files = fs.readdirSync(dir).filter(f => f.endsWith('.astro'));

const dataMap = {
  'balancing-bot.astro': {
    logo: '/eYantra.png',
    org: 'e-Yantra Robotics Competition',
    location: 'IIT Bombay, India',
    role: 'Competitor',
    extra: '(4th Place Internationally)',
    project: 'Balancing Builder Bot',
    guides: 'N/A',
    date: '2024-25 Season'
  },
  'blood-smear.astro': {
    logo: '/IIT_Bombay.png',
    org: 'Biomedical Engineering and Technology Innovation Centre (BETIC)',
    location: 'IIT Bombay, India',
    role: 'Summer Research Internship',
    extra: '(Full Time - On Site)',
    project: 'Beat Back - automatic blood smear device for sickle cell anemia detection',
    guides: 'Prof. Parag Bhargava and Dr. Bhanupratap Gaur',
    date: '19 May - 11 July 2025'
  },
  'infusion.astro': {
    logo: '/IIT_Madras.png',
    org: 'Healthcare Technology Innovation Centre (HTIC)',
    location: 'IIT Madras, India',
    role: 'Academic Research Internship',
    extra: '(Onsite - Full Time)',
    project: 'Beat Back - Ex Vivo Heart Revival and Preservation Platform',
    guides: 'Prof. Jayaraj Joseph and Dr. Nabeel P. M.',
    date: 'N/A'
  },
  'oph.astro': {
    logo: '/EPFL.png',
    org: 'CREATE Lab, EPFL',
    location: 'Remote',
    role: 'Research Internship',
    extra: '',
    project: 'Open Parametric Hand',
    guides: 'Prof. Josie Hughes',
    date: 'Mar \'26 - May \'26'
  },
  'maze-solver.astro': {
    logo: '/eYantra.png',
    org: 'e-Yantra Robotics Competition',
    location: 'IIT Bombay, India',
    role: 'Competitor',
    extra: '(Stage 2)',
    project: 'Maze Solver Bot',
    guides: 'N/A',
    date: '2025-26 Season'
  },
  'posture-belt.astro': {
    logo: '/placeholder.jpeg',
    org: 'MEDHA 2024 Innovation Challenge',
    location: 'India',
    role: 'Lead R&D',
    extra: '',
    project: 'Posture Pro Belt',
    guides: 'N/A',
    date: '2024'
  },
  'line-follower.astro': {
    logo: '/placeholder.jpeg',
    org: 'Robotics Competition',
    location: 'India',
    role: 'Developer',
    extra: '',
    project: 'Fastest Line Follower Robot',
    guides: 'N/A',
    date: '2023'
  },
  'scanner.astro': {
    logo: '/placeholder.jpeg',
    org: 'Academic / Internship Project',
    location: 'India',
    role: 'Hardware Engineer',
    extra: '',
    project: 'Dental Intra Oral Scanner',
    guides: 'N/A',
    date: '2024'
  }
};

for (const file of files) {
  const p = path.join(dir, file);
  let content = fs.readFileSync(p, 'utf8');
  
  // 1. Remove existing "Demonstrated At" blocks.
  // Replace from <!-- Demonstrated At --> down to the next <!-- or </section>
  const regex = /^\s*<!-- Demonstrated At -->[\s\S]*?(?=^\s*(<!--|<\/section>))/m;
  content = content.replace(regex, '');

  // Double check in case of variations
  const regex2 = /^\s*<!-- Demonstrated At -->[\s\S]*?<\/div>\s*<\/div>\s*<\/div>/m;
  content = content.replace(regex2, '');

  // 2. Generate new block
  const d = dataMap[file];
  if (!d) continue;

  let newBlock = `
    <!-- Demonstrated At -->
    <div class="space-y-4">
      <h2 class="text-2xl md:text-3xl font-heading font-bold text-maintext flex items-center gap-3">
        <span class="text-accent">/</span> Demonstrated At
      </h2>
      <div class="bg-accent/5 border border-accent/10 rounded-2xl p-6 md:p-8 flex flex-col md:flex-row items-center md:items-start gap-6">
        <div class="flex-shrink-0 bg-white w-24 h-24 rounded-xl shadow-md border border-accent/20 overflow-hidden flex items-center justify-center p-0">
          <img src="${d.logo}" alt="Logo" class="w-full h-full object-cover" onerror="this.src='/placeholder.jpeg'; this.onerror=null;" />
        </div>
        <div class="text-center md:text-left pt-2">
          <p class="text-maintext font-heading text-xl md:text-2xl font-bold text-accent">
            ${d.org}
          </p>
          <p class="text-maintext font-body text-base md:text-lg mt-2">
            ${d.location}
          </p>
          <p class="text-subtext font-body text-base md:text-lg mt-2 font-semibold">
            ${d.role} ${d.extra ? `<span class="text-yellow-500">${d.extra}</span>` : ''}
          </p>`;
  
  if (d.project !== 'N/A' || d.guides !== 'N/A') {
    newBlock += `
          <p class="text-gray font-body text-base md:text-lg mt-1">`;
    if (d.project !== 'N/A') {
      newBlock += `
            <span class="font-semibold text-maintext">Project:</span> ${d.project}<br/>`;
    }
    if (d.guides !== 'N/A') {
      newBlock += `
            <span class="font-semibold text-maintext">Guides:</span> ${d.guides}`;
    }
    newBlock += `
          </p>`;
  }

  if (d.date !== 'N/A') {
    newBlock += `
          <p class="text-subtext font-body text-base md:text-lg mt-2 font-semibold">
            ${d.date}
          </p>`;
  }

  newBlock += `
        </div>
      </div>
    </div>
`;

  // 3. Insert new block directly after <!-- Content Sections --> \n <section...>
  const injectRegex = /(<!-- Content Sections -->\s*<section[^>]*>)/;
  if (injectRegex.test(content)) {
    content = content.replace(injectRegex, `$1\n${newBlock}`);
    fs.writeFileSync(p, content, 'utf8');
    console.log(`Updated ${file}`);
  } else {
    console.log(`Failed to find injection point in ${file}`);
  }
}
