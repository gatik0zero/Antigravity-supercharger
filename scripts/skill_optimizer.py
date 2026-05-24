import os
import sys
import json
from pathlib import Path

def optimize_skill_file(file_path: Path):
    """Optimizes a SKILL.md markdown file by cleaning up duplicate blank lines,
    trimming trailing whitespaces, and flagging massive content blocks."""
    if not file_path.exists():
        return False, "File does not exist"
    
    try:
        content = file_path.read_text(encoding="utf-8")
        lines = content.splitlines()
        
        # Performance check
        original_line_count = len(lines)
        if original_line_count > 300:
            print(f"  [!] WARNING: {file_path.parent.name} is extremely bloated ({original_line_count} lines). Suggest refactoring.")
            
        # Clean double blank lines & trailing whitespaces
        optimized_lines = []
        last_was_blank = False
        for line in lines:
            trimmed = line.rstrip()
            if not trimmed:
                if not last_was_blank:
                    optimized_lines.append("")
                    last_was_blank = True
            else:
                optimized_lines.append(trimmed)
                last_was_blank = False
                
        optimized_content = "\n".join(optimized_lines) + "\n"
        
        # Save back only if changed
        if optimized_content != content:
            file_path.write_text(optimized_content, encoding="utf-8")
            saved = original_line_count - len(optimized_lines)
            return True, f"Optimized from {original_line_count} to {len(optimized_lines)} lines (Saved {saved} lines)"
        
        return False, "Already fully optimized"
    except Exception as e:
        return False, f"Error: {e}"

def main():
    repo_root = Path(__file__).parent.parent
    skills_dir = repo_root / "skills"
    
    if not skills_dir.exists():
        print("Error: skills directory not found.")
        sys.exit(1)
        
    print("Starting Antigravity Skill Optimizer...")
    
    # Read tiers to prioritize core & domain skills
    tiers_path = skills_dir / ".skill-tiers.json"
    target_skills = []
    
    if tiers_path.exists():
        try:
            with open(tiers_path, "r", encoding="utf-8") as f:
                tiers = json.load(f)
            target_skills = tiers.get("cores", []) + tiers.get("domains", [])
            print(f"Loaded {len(target_skills)} core/domain target skills from .skill-tiers.json")
        except Exception as e:
            print(f"Error reading skill-tiers: {e}")
            
    if not target_skills:
        # Fallback to scanning all directories in skills/
        target_skills = [d.name for d in skills_dir.iterdir() if d.is_dir()]
        print(f"Scanning all {len(target_skills)} skills...")
        
    optimized_count = 0
    for skill_name in target_skills:
        skill_path = skills_dir / skill_name
        skill_file = skill_path / "SKILL.md"
        
        if skill_file.exists():
            print(f"Optimizing: {skill_name} ...")
            changed, msg = optimize_skill_file(skill_file)
            if changed:
                print(f"  [+] {msg}")
                optimized_count += 1
            else:
                print(f"  [-] {msg}")
                
    print(f"\nSkill optimization complete. Total skills optimized: {optimized_count}")

if __name__ == "__main__":
    main()
