import os
from pathlib import Path

def main():
    repo_root = Path(__file__).parent.parent
    workflows_dir = repo_root / "workflows"
    native_dir = workflows_dir / "native"
    native_dir.mkdir(exist_ok=True)
    
    count = 0
    for item in workflows_dir.iterdir():
        if item.is_file() and "_native_" in item.name:
            dest = native_dir / item.name
            try:
                if dest.exists():
                    dest.unlink()
                item.rename(dest)
                count += 1
            except Exception as e:
                print(f"Failed to move {item.name}: {e}")
            
    print(f"Moved {count} native workflow files to workflows/native/.")

if __name__ == "__main__":
    main()
