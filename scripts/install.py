import os
import sys
import shutil
import json
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

    # Load allowed subdirs if not --all
    allowed_skills = None
    if "--all" not in sys.argv:
        tiers_path = skills_src / ".skill-tiers.json"
        if tiers_path.exists():
            try:
                with open(tiers_path, "r", encoding="utf-8") as f:
                    tiers = json.load(f)
                allowed_skills = set(tiers.get("cores", []) + tiers.get("domains", []))
                print(f"Tiered Skill Loading: Syncing only {len(allowed_skills)} core/domain skills. (Use '--all' flag to sync all 1529+ skills).")
            except Exception as e:
                print(f"Warning: Failed to load .skill-tiers.json: {e}")

    # Function to copy contents incrementally (high-performance)
    def copy_contents(src, dest, allowed_subdirs=None):
        if not src.exists():
            print(f"Warning: Source {src} not found.")
            return
        
        count = 0
        skipped = 0
        
        if allowed_subdirs is not None:
            # 1. Sync files directly in the source directory (like manifests and configuration files)
            for item in src.iterdir():
                if item.is_file():
                    dest_file = dest / item.name
                    try:
                        dest_file.parent.mkdir(parents=True, exist_ok=True)
                        if not dest_file.exists() or item.stat().st_mtime > dest_file.stat().st_mtime or item.stat().st_size != dest_file.stat().st_size:
                            if dest_file.exists():
                                try:
                                    os.chmod(dest_file, 0o666)
                                except Exception:
                                    pass
                            shutil.copy2(item, dest_file)
                            count += 1
                        else:
                            skipped += 1
                    except Exception as e:
                        print(f"Warning: Failed to sync {item.name}: {e}")
            
            # 2. Sync only allowed subdirectories
            for subdir_name in allowed_subdirs:
                subdir_src = src / subdir_name
                if subdir_src.exists() and subdir_src.is_dir():
                    for root, dirs, files in os.walk(subdir_src):
                        dirs[:] = [d for d in dirs if d not in ['.git', 'node_modules', '__pycache__', 'testing', 'tests']]
                        for fname in files:
                            src_file = Path(root) / fname
                            rel = src_file.relative_to(src)
                            dest_file = dest / rel
                            try:
                                dest_file.parent.mkdir(parents=True, exist_ok=True)
                                if not dest_file.exists() or src_file.stat().st_mtime > dest_file.stat().st_mtime or src_file.stat().st_size != dest_file.stat().st_size:
                                    if dest_file.exists():
                                        try:
                                            os.chmod(dest_file, 0o666)
                                        except Exception:
                                            pass
                                    shutil.copy2(src_file, dest_file)
                                    count += 1
                                else:
                                    skipped += 1
                            except Exception as e:
                                print(f"Warning: Failed to sync {rel}: {e}")
        else:
            # Full traversal sync
            for root, dirs, files in os.walk(src):
                dirs[:] = [d for d in dirs if d not in ['.git', 'node_modules', '__pycache__', 'testing', 'tests']]
                for fname in files:
                    src_file = Path(root) / fname
                    rel = src_file.relative_to(src)
                    dest_file = dest / rel
                    try:
                        dest_file.parent.mkdir(parents=True, exist_ok=True)
                        if not dest_file.exists() or src_file.stat().st_mtime > dest_file.stat().st_mtime or src_file.stat().st_size != dest_file.stat().st_size:
                            if dest_file.exists():
                                try:
                                    os.chmod(dest_file, 0o666)
                                except Exception:
                                    pass
                            shutil.copy2(src_file, dest_file)
                            count += 1
                        else:
                            skipped += 1
                    except Exception as e:
                        print(f"Warning: Failed to sync {rel}: {e}")
                        
        print(f"Synced {src.name} to {dest.name}: {count} files copied, {skipped} files skipped (up-to-date).")

    # Run sync
    copy_contents(sops_src, sops_dest)
    copy_contents(rules_src, rules_dest)
    copy_contents(workflows_src, workflows_dest)
    copy_contents(skills_src, skills_dest, allowed_skills)

    # Update Manifest
    manifest_path = base_dest / "skills" / ".antigravity-install-manifest.json"
    if manifest_path.exists():
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
