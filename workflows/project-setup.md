---
name: Project Setup
description: "Initialize a new project with complete boilerplate, configuration, and best practices."
trigger: "/setup"
---

# Project Setup Workflow

## Step 1: Requirements
Determine from user:
- What type of project? (Web app, API, CLI, library, data analysis)
- What tech stack? (HTML/CSS/JS, React, Next.js, Node, Python)
- Any specific requirements? (Auth, database, deployment platform)

## Step 2: Initialize
Based on project type:

### Web App (Vite + React)
```bash
npx -y create-vite@latest ./ --template react
npm install
```

### Next.js App
```bash
npx -y create-next-app@latest ./ --ts --eslint --app --src-dir
npm install
```

### Node.js API
```bash
npm init -y
npm install express cors helmet dotenv
npm install -D nodemon
```

### Static HTML/CSS/JS
- Create `index.html`, `css/style.css`, `js/main.js`
- Set up modern CSS with custom properties
- Add responsive viewport meta tag

## Step 3: Configuration
- `.gitignore` with appropriate patterns
- `.env.example` with required environment variables
- `README.md` with setup instructions
- Linting/formatting config (ESLint, Prettier)

## Step 4: Agent Config
- Copy `rules/` and `skills/` folder structure from template
- Customize rules for the specific tech stack

## Step 5: First Commit
```bash
git init
git add .
git commit -m "chore: initial project setup"
```

## Deliverable
- Working project that runs with `npm run dev`
- All configuration files in place
- README with clear getting-started instructions
