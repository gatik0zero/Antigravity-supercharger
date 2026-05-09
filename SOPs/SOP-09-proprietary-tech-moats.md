# SOP 09: Proprietary Technology & AI Integration

## 1. Objective
To build defensible "moats" through the integration of specialized ML/AI models, custom algorithms, and unique data pipelines, moving beyond wrapper applications.

## 2. Scope
Applies to AI feature integration, data processing logic, and backend algorithmic development.

## 3. Directives
### 3.1. Deep Tech Integration
- Do not rely solely on basic LLM API calls. Build proprietary orchestration layers, custom RAG (Retrieval-Augmented Generation) pipelines, or fine-tuned local models.
- Utilize the `/ml-training` workflow to train specialized models on proprietary data rather than relying purely on zero-shot inference.

### 3.2. The Data Moat
- Architect systems to continuously capture high-quality, proprietary data from user interactions. This data must be structured to train future models, creating an insurmountable advantage over time.

### 3.3. Algorithmic Supremacy
- When solving a complex problem (e.g., routing, matching, ranking), write highly optimized, bespoke algorithms rather than relying on generic, off-the-shelf libraries that competitors can also use.

## 4. Executable Actions
- Always propose setting up a Vector Database or Knowledge Graph alongside relational databases for AI-first applications.
- Utilize `mcp_sqlite` or `mcp_postgres` to structure prompt feedback loops and telemetry data.
