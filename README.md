# KK AI Chat

## A modern AI chatbot   designed   by   KJ_28

---


Prompt Engine
↓

Memory Engine
↓

Pipeline

↓

LLM Client


---

## Quick Start
### Prerequisites

Before getting started, make sure you have:

- Python 3.13+
- Git
- A DeepSeek API Key


1. Clone the repository
git clone https://github.com/19916576769-hash/AI-chatbot.git
cd AI-chatbot


2. Create a virtual environment

Windows

python -m venv .venv
.venv\Scripts\activate

macOS / Linux

python3 -m venv .venv
source .venv/bin/activate


3. Install dependencies
pip install -r requirements.txt


4. Configure environment variables

Create a .env file in the project root.

Example:

DEEPSEEK_API_KEY=your_api_key_here

如果你的项目还有其他环境变量，例如：

MODEL_NAME=deepseek-chat
BASE_URL=https://api.deepseek.com

也可以一起写出来。

5. Run the server
uvicorn app:app --reload

启动成功后应该看到类似：

INFO: Uvicorn running on http://127.0.0.1:8000


6. Open your browser

Visit:

http://127.0.0.1:8000

开始和 KK Chat 对话。











## Feature

- prompt engine
- modular architecture
- prompt pipeline
- memory system
- prompt metadata
- version management
- extendable framework





## 框架设计原则 Framework Design Principles

1. Single Responsibility
2. Open / Closed
3. Pipeline First
4. Configuration over Code
5. Stable Public API
6. Low Coupling




---




## Architecture
                KK AI Framework

                       │
                 Chat Pipeline
                       │
        ┌──────────────┴──────────────┐
        ▼                             ▼
 Prompt Engine                  Memory Engine
        │
        ▼
 Prompt Builder
        │
        ▼
 Prompt Stages




---



## Project Structure

 KK-Chatbot/

├── chatbot.py
├── pipeline.py
│
├── prompt/
│
├── memory/
│
├── logs/
│
├── tests/
│
├── docs/
│
├── README.md
└── requirements.txt




---



v1.0  -  v1.4  Basic AI Chat

↓

v1.5  memory_prompt

↓

v1.6 better prompt

↓

v1.7  Prompt Pipeline

↓

v1.8  AI Framework

↓

v1.9  Open Source

↓

v2.0  Secure AI

↓

v3.0  RAG

↓

v4.0  Agent
