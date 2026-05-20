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
            try:
                if item.is_dir():
                    if dest_item.exists():
                        def remove_readonly(func, path, exc):
                            import stat
                            try:
                                os.chmod(path, stat.S_IWRITE)
                                func(path)
                            except Exception:
                                pass
                        shutil.rmtree(dest_item, onexc=remove_readonly)
                    
                    # Ignore .git, node_modules, tests, and testing folders to avoid path issues and speed up
                    def ignore_patterns(path, names):
                        ignored = []
                        for name in names:
                            if name in ['.git', 'node_modules', '__pycache__', 'testing', 'tests']:
                                ignored.append(name)
                        return ignored
                    
                    shutil.copytree(item, dest_item, ignore=ignore_patterns)
                else:
                    shutil.copy2(item, dest_item)
                count += 1
            except Exception as e:
                print(f"Warning: Failed to sync {item.name}: {e}")
        print(f"Synced {count} items from {src.name} to {dest.name}.")

    # Run sync
    copy_contents(sops_src, sops_dest)
    copy_contents(rules_src, rules_dest)
    copy_contents(workflows_src, workflows_dest)
    copy_contents(skills_src, skills_dest)

    # Update Manifest
    manifest_path = base_dest / "skills" / ".antigravity-install-manifest.json"
    if manifest_path.exists():
        import json
        from datetime import datetime
        
        try:
            with open(manifest_path, 'r', encoding='utf-8') as f:
                manifest = json.load(f)
            
            # The supercharger itself is the main component
            supercharger_name = "antigravity-supercharger"
            if supercharger_name not in manifest.get("entries", []):
                manifest.setdefault("entries", []).append(supercharger_name)
                manifest["entries"].sort()
                manifest["updatedAt"] = datetime.utcnow().isoformat() + "Z"
                
                with open(manifest_path, 'w', encoding='utf-8') as f:
                    json.dump(manifest, f, indent=2)
                print(f"Manifest updated with {supercharger_name}.")
            else:
                print("Manifest already up-to-date.")
        except Exception as e:
            print(f"Error updating manifest: {e}")
    else:
        print(f"Warning: Manifest not found at {manifest_path}")

    print("\nInstallation complete! Restart your Antigravity IDE session to apply changes.")

if __name__ == "__main__":
    install()
