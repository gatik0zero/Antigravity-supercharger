"""
sync_to_repo.py - Syncs global environment components back INTO the repository.

This is the REVERSE of install.py. It ensures the GitHub repo contains
all free, shareable components from the global environment so that
public users get the full Supercharger experience.

Components synced:
  1. Integrated rules (3rd-party SECURITY.md, CONTRIBUTING.md, CODE_OF_CONDUCT.md)
  2. Integrated tools (lean entry-point scripts only, NOT full source trees)
  3. MCP config example (sanitized, no secrets)

Components NOT synced (already in repo via other means):
  - SOPs (manually authored in repo/SOPs/)
  - Core rules (manually authored in repo/rules/)
  - Skills (too large, users install via install.py from skill repos)
"""

import os
import shutil
from pathlib import Path

def sync_to_repo():
    repo_root = Path(__file__).parent.parent
    global_base = Path.home() / ".gemini" / "antigravity"

    # --- 1. Sync integrated rules (3rd-party) ---
    global_rules = global_base / "rules"
    repo_rules = repo_root / "rules"
    repo_rules.mkdir(exist_ok=True)

    synced = 0
    if global_rules.exists():
        for f in global_rules.iterdir():
            if not f.is_file():
                continue
            # Only sync 3rd-party integrated rules (pattern: reponame_FILENAME.md)
            # Skip SOPs that were misplaced into rules/, skip manifests
            if f.name.startswith("SOP-") or f.name.startswith(".") or f.name.startswith("0"):
                continue
            # Check if it's a 3rd-party integrated rule (contains underscore separator)
            if "_" in f.name and f.suffix == ".md":
                dest = repo_rules / f.name
                if not dest.exists() or f.stat().st_mtime > dest.stat().st_mtime:
                    shutil.copy2(f, dest)
                    synced += 1

    print(f"Synced {synced} integrated rules to repo.")

    # --- 2. Sync tools directory (lean) ---
    global_tools = global_base / "tools"
    repo_tools = repo_root / "tools"

    tools_synced = 0
    if global_tools.exists():
        for tool_dir in global_tools.iterdir():
            if not tool_dir.is_dir():
                continue
            dest_dir = repo_tools / tool_dir.name
            dest_dir.mkdir(parents=True, exist_ok=True)

            for root, dirs, files in os.walk(tool_dir):
                # Limit depth to 2 levels to keep it lean
                depth = len(Path(root).relative_to(tool_dir).parts)
                if depth > 2:
                    continue
                for fname in files:
                    src = Path(root) / fname
                    rel = src.relative_to(tool_dir)
                    dest = dest_dir / rel
                    dest.parent.mkdir(parents=True, exist_ok=True)
                    if not dest.exists() or src.stat().st_mtime > dest.stat().st_mtime:
                        shutil.copy2(src, dest)
                        tools_synced += 1

    print(f"Synced {tools_synced} tool files to repo.")

    # --- 3. Verify MCP config example is up to date ---
    mcp_example = repo_root / "mcp_config.example.json"
    if mcp_example.exists():
        import json
        with open(mcp_example, "r") as f:
            config = json.load(f)

        servers = config.get("mcpServers", {})
        issues = []

        # Verify DuckDuckGo is present (not Brave)
        if "brave-search" in servers:
            issues.append("WARNING: mcp_config.example.json still has brave-search (should be duckduckgo)")
        if "duckduckgo" not in servers:
            issues.append("WARNING: mcp_config.example.json missing duckduckgo server")

        # Verify no real secrets leaked
        raw = mcp_example.read_text()
        if "ghp_" in raw or any(len(v) > 30 and v.startswith("ghp_") for v in raw.split()):
            issues.append("CRITICAL: Real GitHub PAT detected in example config!")

        if issues:
            for issue in issues:
                print(f"  ⚠ {issue}")
        else:
            print("MCP config example verified: clean and up-to-date.")

    print(f"\nSync complete. Total: {synced + tools_synced} files synced to repo.")

if __name__ == "__main__":
    sync_to_repo()
