# SOP 01: Project Initialization and Scaffolding

## 1. Objective
To establish a standardized procedure for initializing new projects, systems, or tools within the Antigravity IDE environment, ensuring consistency, high-quality aesthetics, and proper configuration from the very beginning.

## 2. Scope
This SOP applies to all AI agents and developers creating new repositories, web applications, or system components.

## 3. Directives

### 3.1. Invoking Project Setup Workflows
- **Always start with the `/project-setup` workflow.** 
- Before generating any code, use the `view_file` tool to read the `/project-setup` workflow if not fully familiar with it.
- Ensure all boilerplate, configuration, and best practices outlined in the setup workflow are executed.

### 3.2. Web Application Scaffolding
- If the user requests a complex web application, use a framework like Next.js or Vite.
- Use `npx -y` to automatically install the script and its dependencies in non-interactive mode.
- ALWAYS run the command with the `--help` flag first to see available options.
- Example command for Vite: `npx -y create-vite@latest ./ --template react-ts`
- Avoid TailwindCSS unless explicitly requested by the user. Prefer Vanilla CSS (`index.css`) for maximum flexibility and control.

### 3.3. Initial Design & Aesthetics
- Implement **Rich Aesthetics** from the get-go. Utilize modern web design practices: vibrant colors, dark modes, glassmorphism, and dynamic micro-animations.
- **Do not use generic colors.** Apply curated, harmonious color palettes (e.g., HSL tailored colors).
- Use modern typography (e.g., Inter, Roboto) over browser defaults.
- No placeholders! Use the `generate_image` tool to create functional, premium demonstration assets instead of empty placeholder blocks.

### 3.4. Required Files & Architecture
- **README.md**: Required for every project or module. Must document what the project does and how to run it.
- **.env.example**: Provide template environment variables. Never hardcode secrets.
- **.gitignore**: Must exclude node_modules, .env, and any OS-specific hidden files.

## 4. Executable Commands & Actions
- `npx -y create-<framework> ./` (Always check help first)
- `npm install` (To install dependencies)
- `generate_image` (For generating premium UI assets)

## 5. Situational Triggers
- **Trigger**: "Create a new app" or "Start a new project".
- **Action**: Execute this SOP. Initialize repository, scaffold with `npx`, apply premium CSS, generate a README.
