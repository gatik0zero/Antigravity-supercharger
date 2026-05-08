import os
import shutil

repos = [
    "financial-services", "n8n", "snipe-it", "akaunting", "chatwoot", 
    "openproject", "dolibarr", "erpnext", "coolify", "outline", 
    "openboxes", "mautic", "superset"
]

base_path = os.path.join(os.path.expanduser("~"), ".gemini", "antigravity")
skills_path = os.path.join(base_path, "skills")
tools_path = os.path.join(base_path, "tools")
workflows_path = os.path.join(base_path, "workflows")
rules_path = os.path.join(base_path, "rules")

os.makedirs(tools_path, exist_ok=True)
os.makedirs(workflows_path, exist_ok=True)
os.makedirs(rules_path, exist_ok=True)

integrated_count = 0

for repo in repos:
    repo_path = os.path.join(skills_path, repo)
    if not os.path.exists(repo_path):
        continue
        
    print(f"Integrating components from {repo}...")
    
    # 1. Integrate CLIs, Tools, and Logic
    tool_dest = os.path.join(tools_path, repo)
    os.makedirs(tool_dest, exist_ok=True)
    
    for folder in ["scripts", "bin", "cli", "packages/cli", "tools", "docker", "setup", "utils"]:
        src = os.path.join(repo_path, folder)
        if os.path.exists(src) and os.path.isdir(src):
            dest = os.path.join(tool_dest, folder.replace("/", "_"))
            if not os.path.exists(dest):
                shutil.copytree(src, dest)
                integrated_count += 1
                
    # Copy standalone executable files or scripts from root
    for file in os.listdir(repo_path):
        if file.endswith((".py", ".sh", ".js", ".ts", ".bat", ".cmd")) or file in ["Makefile", "Dockerfile", "docker-compose.yml"]:
            src = os.path.join(repo_path, file)
            if os.path.isfile(src):
                shutil.copy(src, os.path.join(tool_dest, file))
                integrated_count += 1

    # 2. Integrate Workflows (CI/CD, internal logic workflows)
    for folder in [".github/workflows", "workflows", "actions", ".gitlab-ci.yml"]:
        src = os.path.join(repo_path, folder)
        if os.path.exists(src):
            if os.path.isdir(src):
                for file in os.listdir(src):
                    if file.endswith((".yml", ".yaml", ".md")):
                        dest_file = os.path.join(workflows_path, f"{repo}_native_{file}")
                        if not os.path.exists(dest_file):
                            shutil.copy(os.path.join(src, file), dest_file)
                            integrated_count += 1
            elif os.path.isfile(src):
                dest_file = os.path.join(workflows_path, f"{repo}_native_{os.path.basename(src)}")
                if not os.path.exists(dest_file):
                    shutil.copy(src, dest_file)
                    integrated_count += 1
                        
    # 3. Integrate Rules (Guidelines, code standards, security)
    for file in ["CODE_OF_CONDUCT.md", "CONTRIBUTING.md", "SECURITY.md", "ARCHITECTURE.md", "STYLEGUIDE.md"]:
        src = os.path.join(repo_path, file)
        if os.path.exists(src) and os.path.isfile(src):
            dest_file = os.path.join(rules_path, f"{repo}_{file}")
            if not os.path.exists(dest_file):
                shutil.copy(src, dest_file)
                integrated_count += 1

print(f"Successfully integrated {integrated_count} distinct tools, workflows, CLIs, and rule components into the global environment.")
