---
name: master-azure-ai
description: "Unified entry point for all Azure AI services (Speech, Vision, Translation, Content Safety, Document Intelligence, and OpenAI)."
category: cloud-ai
tags: [azure, ai, ml, cloud]
---

# Master Azure AI Skills

## Overview
This master skill provides consolidated access to Azure AI SDKs and endpoints. Use this to avoid loading dozens of individual language-specific skills.

## Available Services & SDKs

### 1. Azure OpenAI & Agents
- **Persistent Agents**: `dotnet`, `java`. Use for long-running stateful AI agents.
- **OpenAI Service**: `dotnet`. Standard GPT-4o/o1 model access.
- **AI Projects**: `dotnet`, `java`, `py`, `ts`. Management of Azure AI Foundry projects.

### 2. Vision & Content Understanding
- **Image Analysis**: `java`, `py`. OCR, object detection, and captioning.
- **Content Understanding**: `py`. Structured data extraction from documents/media.
- **Form/Document Intelligence**: `dotnet`, `java`, `ts`. Specialized document processing.

### 3. Language & Safety
- **Content Safety**: `java`, `py`, `ts`. Moderation and jailbreak detection.
- **Text Analytics**: `py`. Sentiment, PII, and entity extraction.
- **Translation**: `py` (Document/Text), `ts`.

### 4. Speech & Audio
- **Transcription**: `py`. Batch and real-time speech-to-text.
- **Voice Live**: `dotnet`, `java`, `py`, `ts`. Real-time multimodal voice interactions.
- **Anomaly Detector**: `java`.

## Trigger Protocols
- For **Python** development: Reference specific `.py` SDK sections.
- For **JavaScript/TypeScript**: Reference `.ts` SDK sections.
- For **Enterprise (.NET/Java)**: Reference `.dotnet` or `.java` sections.

## Efficiency Tip
Only load the specific code block or configuration needed for the current task. Do not request the full documentation for all services.
