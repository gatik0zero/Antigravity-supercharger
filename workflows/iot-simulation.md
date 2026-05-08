---
name: IoT Simulation
description: "Workflow for mocking, ingesting, and analyzing IoT telemetry data."
trigger: "/iot"
---

# IoT Simulation Workflow

## Step 1: Telemetry Mocking
- Define device schemas (e.g., temperature sensors, GPS trackers)
- Scaffold Python scripts to generate synthetic telemetry data
- Output simulated data to JSON or SQLite

## Step 2: Data Ingestion & Bridging
- Use the **Fetch MCP Server** to query REST APIs from live or mock devices.
- Optionally write scripts to connect to an MQTT broker (`paho-mqtt`).
- Validate incoming data schemas against expected formats.

## Step 3: Real-Time Analysis
- Analyze stream for anomalies (e.g., temperature spikes)
- Log critical alerts
- Aggregate data by time windows

## Tools
- **Fetch MCP**: Make HTTP requests to device APIs
- **Context7**: Look up `paho-mqtt` or IoT framework documentation
- **Python**: Write bridging scripts for hardware protocols
