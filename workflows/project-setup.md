---
name: Project Setup
description: "Initialize a new project with complete boilerplate, configuration, and best practices."
trigger: "/setup"
---

# Project Setup Workflow

## Step 1: Scaffolding
Select stack and run:
- **Vite + React**: `npx -y create-vite@latest ./ --template react && npm install`
- **Next.js**: `npx -y create-next-app@latest ./ --ts --eslint --app --src-dir && npm install`
- **Node.js**: `npm init -y && npm install express cors helmet dotenv && npm install -D nodemon`
- **Static HTML**: Create semantic `index.html`, responsive viewport, `css/style.css`, `js/main.js`.

## Step 2: Configure & Commit
- Set up `.gitignore`, `.env.example`, `README.md`, ESLint, and Prettier.
- Copy `rules/` and `skills/` templates; customize rules.
- Run `git init && git add . && git commit -m "chore: initial project setup"`.

## Deliverables
- Working project running via `npm run dev`, proper config, and clear README setup instructions.
