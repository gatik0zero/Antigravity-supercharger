---
name: IoT Simulation
description: "Workflow for mocking, ingesting, and analyzing IoT telemetry data."
trigger: "/iot"
---

# IoT Simulation Workflow

## Step 1: Mock & Ingest
- Define device schemas (temperature, GPS) and generate synthetic telemetry (JSON/SQLite).
- Use **Fetch MCP Server** to query REST APIs from live or mock devices. Validate schemas.

## Step 2: Analyze & Alert
- Analyze stream for anomalies (e.g. temperature spikes) and log critical alerts.
- Aggregate telemetry data by time windows.

## Tools
- **Fetch MCP**: Make HTTP requests to device APIs.
- **Context7**: Look up `paho-mqtt` or IoT framework documentation.
- **Python**: Write bridging scripts for hardware protocols.
