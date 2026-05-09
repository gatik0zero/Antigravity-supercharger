import os
import shutil
from pathlib import Path

def install():
    # Define source paths (relative to this script)
    repo_root = Path(__file__).parent.parent
    sops_src = repo_root / "SOPs"
    rules_src = repo_root / "rules"
    workflows_src = repo_root / "workflows"
    skills_src = repo_root / "skills"

    # Define destination paths (global environment)
    base_dest = Path.home() / ".gemini" / "antigravity"
    sops_dest = base_dest / "sops"
    rules_dest = base_dest / "rules"
    workflows_dest = base_dest / "workflows"
    skills_dest = base_dest / "skills"

    # Ensure destination directories exist
    for dest in [sops_dest, rules_dest, workflows_dest, skills_dest]:
        dest.mkdir(parents=True, exist_ok=True)

    print(f"Installing components to {base_dest}...")

    # Function to copy contents
    def copy_contents(src, dest):
        if not src.exists():
            print(f"Warning: Source {src} not found.")
            return
        
        count = 0
        for item in src.iterdir():
            dest_item = dest / item.name
            if item.is_dir():
                if dest_item.exists():
                    shutil.rmtree(dest_item)
                shutil.copytree(item, dest_item)
            else:
                shutil.copy2(item, dest_item)
            count += 1
        print(f"Synced {count} items from {src.name} to {dest.name}.")

    # Run sync
    copy_contents(sops_src, sops_dest)
    copy_contents(rules_src, rules_dest)
    copy_contents(workflows_src, workflows_dest)
    copy_contents(skills_src, skills_dest)

    print("\nInstallation complete! Restart your Antigravity IDE session to apply changes.")

if __name__ == "__main__":
    install()
