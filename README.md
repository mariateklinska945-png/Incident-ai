# 🔎 IncidentAI — AI Incident Investigator

IncidentAI is an AI agent that investigates software incidents by gathering evidence from multiple system sources before identifying the most likely root cause.

Instead of asking an LLM to guess why something failed, IncidentAI gives the model tools to inspect transaction data, application logs, deployments, and code changes.

> **Example question:**
> *"Why are payments failing?"*

The agent decides what evidence it needs, calls the relevant tools, correlates the results, and produces a structured root cause analysis.

---

## 🎯 The Problem

When a production incident happens, engineers often need to manually inspect multiple sources:

* transaction metrics
* application logs
* recent deployments
* configuration and code changes

An LLM alone cannot reliably investigate these incidents because it does not have access to the underlying system state.

IncidentAI demonstrates how an AI agent can use **tool calling** to gather real evidence before reaching a conclusion.

---

## 🧠 How It Works

```text
User
 │
 │ "Why are payments failing?"
 ▼
┌──────────────────────────┐
│   LangChain AI Agent     │
│                          │
│  Decides what evidence   │
│  should be investigated  │
└────────────┬─────────────┘
             │
             ▼
┌─────────────────────────────────────────┐
│                Tools                    │
│                                         │
│  check_transactions()                   │
│  check_logs()                           │
│  check_deployments()                    │
│  check_code_changes()                   │
└───────────────────┬─────────────────────┘
                    │
                    ▼
          Evidence correlation
                    │
                    ▼
┌──────────────────────────┐
│    Root Cause Report     │
│                          │
│ • What happened          │
│ • Most likely cause      │
│ • Evidence               │
│ • Confidence level       │
└──────────────────────────┘
```

The LLM does not receive all incident data directly in the prompt.

Instead, the agent decides which tools to call during the investigation.

This separates **reasoning** from **data retrieval** and makes the investigation more grounded and auditable.

---

## 🛠 Available Tools

### `check_transactions`

Reads recent payment transactions and calculates the transaction failure rate.

### `check_logs`

Inspects application logs for errors that may explain the incident.

### `check_deployments`

Checks recent software deployments and their timing.

### `check_code_changes`

Inspects changes associated with deployed versions.

Each tool is implemented as a normal Python function and exposed to the agent through LangChain's `@tool` decorator.

---

## 🧪 Example Incident

The repository currently contains a simulated payment incident.

A new version of the payment API is deployed:

```text
payment-api v2.4.1
09:30
```

Shortly afterwards, payment failures begin to increase.

Application logs report:

```text
Database connection pool exhausted
Payment request timeout
```

The deployment contains the following configuration change:

```text
DB_POOL_SIZE: 50 → 10
```

IncidentAI correlates these signals and identifies the reduced database connection pool as the most likely root cause.

---

## 💬 Example Investigation

Run the application:

```bash
python3 main.py
```

Ask:

```text
Why are payments failing?
```

The agent autonomously selects and executes investigation tools.

Example:

```text
Tools used:

✓ check_transactions
✓ check_logs
✓ check_deployments
✓ check_code_changes
```

It then produces a report similar to:

```text
What happened:
Payments are experiencing a high failure rate.

Most likely root cause:
The database connection pool was reduced from 50 to 10
during deployment v2.4.1.

Evidence:
- 50% transaction failure rate
- Database connection pool exhausted errors
- Payment request timeouts
- Deployment immediately preceding the failures
- DB_POOL_SIZE changed from 50 to 10

Confidence:
High
```

---

## 🏗 Project Structure

```text
incident-ai/
├── app/
│   ├── agent.py
│   ├── tools.py
│   ├── graph.py
│   └── models.py
│
├── data/
│   ├── transactions.csv
│   ├── logs.json
│   ├── deployments.json
│   └── code_changes.json
│
├── main.py
├── requirements.txt
├── .env.example
└── README.md
```

---

## ⚙️ Tech Stack

* **Python**
* **LangChain**
* **OpenAI**
* **LangGraph**
* **Tool Calling**
* **Structured incident data**

---

## 🚀 Running Locally

Clone the repository:

```bash
git clone git@github.com:mariateklinska945-png/incident-ai.git
cd incident-ai
```

Create a virtual environment:

```bash
python3 -m venv .venv
source .venv/bin/activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Create a `.env` file:

```text
OPENAI_API_KEY=your_openai_api_key
```

Run IncidentAI:

```bash
python3 main.py
```

---

## 🔐 Security

API keys and other secrets are never committed to the repository.

The local `.env` file is excluded through `.gitignore`.

`.env.example` documents the required environment variables without exposing credentials.

---

## 🗺 Roadmap

IncidentAI is being extended toward a more complete agentic incident-response workflow.

Planned improvements include:

* **LangGraph workflow** — explicit investigation stages and state management
* **RAG** — search previous incidents and operational runbooks
* **Multiple incident scenarios** — database failures, external provider outages, bad deployments, and traffic spikes
* **Structured outputs** — typed incident reports using Pydantic
* **Human-in-the-loop** — approval before potentially risky remediation actions
* **Evaluation** — test whether the agent identifies known root causes correctly
* **Observability** — trace tool calls and investigation paths

---

## 💡 Why This Project

IncidentAI explores a core pattern for production AI systems:

> **LLMs should not guess when they can investigate.**

By combining LLM reasoning with deterministic tools and structured system data, an AI agent can gather evidence, form hypotheses, and explain how it reached its conclusion.

The same architecture can be extended beyond incident response to areas such as fraud investigation, compliance operations, infrastructure debugging, and security analysis.

