import os
import json
from pathlib import Path

def main():
    paths = [
        Path("C:/Users/Canada/.gemini/antigravity/mcp_config.json"),
        Path("C:/Users/Canada/.gemini/antigravity-ide/mcp_config.json"),
        Path("C:/Users/Canada/.gemini/config/mcp_config.json")
    ]
    
    # Dynamically resolve GITHUB PAT to avoid hardcoding secrets in repo files
    pat = os.environ.get("GITHUB_PERSONAL_ACCESS_TOKEN") or os.environ.get("GITHUB_PAT")
    
    # If not in env, try to read from existing local config file
    if not pat:
        for p in paths:
            if p.exists():
                try:
                    with open(p, "r", encoding="utf-8") as f:
                        old_config = json.load(f)
                    old_pat = old_config.get("mcpServers", {}).get("github", {}).get("env", {}).get("GITHUB_PERSONAL_ACCESS_TOKEN")
                    if old_pat and old_pat != "YOUR_GITHUB_PAT_HERE" and not old_pat.startswith("ghp_YOUR_"):
                        pat = old_pat
                        break
                except Exception:
                    pass
                    
    # Fallback to placeholder if none found
    if not pat:
        pat = "YOUR_GITHUB_PAT_HERE"
        
    # Define offline config
    config = {
      "mcpServers": {
        "context7": {
          "command": "npx",
          "args": [
            "--no-install",
            "@upstash/context7-mcp"
          ]
        },
        "sequential-thinking": {
          "command": "npx",
          "args": [
            "--no-install",
            "@modelcontextprotocol/server-sequential-thinking"
          ]
        },
        "memory": {
          "command": "npx",
          "args": [
            "--no-install",
            "@modelcontextprotocol/server-memory"
          ]
        },
        "filesystem": {
          "command": "npx",
          "args": [
            "--no-install",
            "@modelcontextprotocol/server-filesystem",
            "c:\\Users\\Canada\\Documents\\Antigravity"
          ]
        },
        "playwright": {
          "command": "npx",
          "args": [
            "--no-install",
            "@playwright/mcp"
          ]
        },
        "puppeteer": {
          "command": "npx",
          "args": [
            "--no-install",
            "@modelcontextprotocol/server-puppeteer"
          ]
        },
        "github": {
          "command": "npx",
          "args": [
            "--no-install",
            "@modelcontextprotocol/server-github"
          ],
          "env": {
            "GITHUB_PERSONAL_ACCESS_TOKEN": pat
          }
        },
        "duckduckgo": {
          "command": "uvx",
          "args": [
            "--offline",
            "duckduckgo-mcp-server"
          ]
        },
        "sqlite": {
          "command": "uvx",
          "args": [
            "--offline",
            "mcp-server-sqlite",
            "--db-path",
            "c:\\Users\\Canada\\Documents\\Antigravity\\database.db"
          ]
        },
        "postgres": {
          "command": "npx",
          "args": [
            "--no-install",
            "@modelcontextprotocol/server-postgres",
            "postgresql://localhost/mydb"
          ]
        },
        "fetch": {
          "command": "uvx",
          "args": [
            "--offline",
            "mcp-server-fetch"
          ]
        }
      }
    }
    
    for p in paths:
        try:
            if not p.parent.exists():
                p.parent.mkdir(parents=True, exist_ok=True)
            
            # If it's a symbolic link/junction, we write to the target or overwrite it
            if p.is_symlink() or p.exists():
                try:
                    p.unlink()
                except Exception:
                    pass
            
            with open(p, "w", encoding="utf-8") as f:
                json.dump(config, f, indent=2)
            print("mcp_config.json updated successfully at:", p)
        except Exception as e:
            print(f"Error updating {p}: {e}")

if __name__ == "__main__":
    main()
