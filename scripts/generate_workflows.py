import os

workflows = [
    ("financial-services", "Financial Services Integration", "Manage and deploy financial services logic.", "/financial-services"),
    ("n8n", "n8n Automation", "Workflow automation and custom n8n node development.", "/n8n"),
    ("snipe-it", "Snipe-IT Asset Management", "IT asset management and API integration workflow.", "/snipe-it"),
    ("akaunting", "Akaunting Setup", "Open source accounting integration and module development.", "/akaunting"),
    ("chatwoot", "Chatwoot Customer Engagement", "Customer engagement CRM and chatbot integration.", "/chatwoot"),
    ("openproject", "OpenProject Management", "Project management integration and API tooling.", "/openproject"),
    ("dolibarr", "Dolibarr ERP & CRM", "ERP and CRM setup, module configuration, and integration.", "/dolibarr"),
    ("erpnext", "ERPNext Implementation", "Frappe framework integration, ERPNext customization.", "/erpnext"),
    ("coolify", "Coolify PaaS", "Self-hosting PaaS deployment and infrastructure workflow.", "/coolify"),
    ("outline", "Outline Knowledge Base", "Team knowledge base setup and markdown documentation.", "/outline"),
    ("openboxes", "OpenBoxes Supply Chain", "Supply chain and inventory management integration.", "/openboxes"),
    ("mautic", "Mautic Marketing Automation", "Marketing automation and campaign integration.", "/mautic"),
    ("superset", "Apache Superset BI", "Data visualization and business intelligence dashboarding.", "/superset")
]

base_path = os.path.join(os.path.expanduser("~"), ".gemini", "antigravity", "workflows")

for filename, name, desc, trigger in workflows:
    content = f"""---
name: {name}
description: "{desc}"
trigger: "{trigger}"
---

# {name} Workflow

## Overview
This workflow utilizes the globally integrated `@{filename}` skill to interact with the repository.

## Step 1: Environment Analysis
- Locate the configured instance or local repository in the global skills directory.
- Verify API keys or environment variables required for connection.

## Step 2: Deployment & Configuration
- Set up the application infrastructure.
- Apply configurations or seed databases.

## Step 3: API & Extensibility
- Integrate custom scripts via the application's REST/GraphQL API.
- Create custom plugins/modules using the repository's framework.

## Tools
- **Filesystem MCP**: Browse the cloned repository locally.
- **Fetch MCP**: Connect to the running instance's API.
- **Postgres/SQLite MCP**: Interact with the application's database.
"""
    with open(os.path.join(base_path, f"{filename}.md"), "w") as f:
        f.write(content)
print("Workflows generated successfully.")
