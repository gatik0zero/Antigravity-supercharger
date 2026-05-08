const fs = require('fs');
const os = require('os');
const userHome = os.homedir();
const path = require('path').join(userHome, '.gemini', 'antigravity', 'skills', '.antigravity-install-manifest.json');
const manifest = JSON.parse(fs.readFileSync(path, 'utf8'));

const repos = [
    "financial-services", "n8n", "snipe-it", "akaunting", "chatwoot",
    "openproject", "dolibarr", "erpnext", "coolify", "outline",
    "openboxes", "mautic", "superset"
];

let changed = false;
for (const repo of repos) {
    if (!manifest.entries.includes(repo)) {
        manifest.entries.push(repo);
        changed = true;
    }
}

if (changed) {
    manifest.entries.sort();
    manifest.updatedAt = new Date().toISOString();
    fs.writeFileSync(path, JSON.stringify(manifest, null, 2));
    console.log("Manifest updated successfully.");
} else {
    console.log("Manifest already up-to-date.");
}
