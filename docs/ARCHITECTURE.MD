
# 🏗️ Architecture - Agentic Calculator PoC

**Detailed technical documentation of the multi-agent architecture with local LLM**

---

> 🇧🇷 [Versão Original em Português (Brasil)](ARCHITECTURE_BR.md)  
> **Aviso:** Esta é a versão original da documentação técnica. Para máxima precisão conceitual e técnica, utilize preferencialmente esta versão.

> 🇺🇸 [English Version](ARCHITECTURE.md)  
> **Disclaimer:** This documentation is also available in English. For official technical reference, consult the Portuguese or English versions.

> 🇪🇸 [Documentación en Español](ARCHITECTURE_ES.md)  
> **Aviso:** La documentación también está disponible en español. Para mayor precisión técnica, consulte la versión original en portugués o la versión en inglés.

---


## 📋 Index

- Overview
- Design Principles
- Components
- Data Flow
- Architectural Decisions
- Security
- Scalability
- Technology Stack

---

## 🎯 Overview

### Layered Architecture

Presentation Layer → Orchestration Layer → Specialists Layer → Model Layer → Infrastructure Layer

Cross-cutting Layer: Security, Logging, Configuration.

---

## 🧩 Design Principles

### 1. Separation of Concerns
Each component has a **single responsibility**:
- Orchestrator: Coordination and flow
- LLMClient: Model communication
- Specialists: Operation execution
- Sandbox: Security validation

### 2. Open/Closed Principle
Open for extension, closed for modification.

### 3. Dependency Injection
Components receive dependencies via constructor.

### 4. Fail-Safe
The system fails gracefully and returns structured errors.

---

## 🔧 Components

### CalculatorOrchestrator
Responsible for coordinating the full execution pipeline:
1. Planning (LLM)
2. Validation (Security)
3. Execution (Specialists)
4. Result consolidation

### LLMClient
Handles communication with the language model:
- Generates responses
- Converts natural language into structured operation plans

### Specialists
Execute domain‑specific operations using the Strategy Pattern:
- Basic Operations
- Advanced Operations
- Statistical Operations

### Sandbox
Ensures safe execution through:
- Operation whitelist
- Execution timeout
- Argument validation
- Execution logging
- Error isolation

---

## 🔄 Data Flow

Example:
User input → Orchestrator → LLM planning → Validation → Execution → Consolidation → UI output

Example result:
Final result returned together with execution metadata and intermediate results.

---

## 🎨 Architectural Decisions

### Why Local LLM?
Chosen for:
- Privacy
- Zero operational cost
- Local experimentation capability

### Why Streamlit?
Chosen for:
- Rapid development
- Python-native workflow
- Ideal for PoC environments

### Why Multi-Agent Architecture?
Benefits:
- Modular design
- Easier testing
- Better scalability
- Natural delegation model aligned with AI agents

---

## 🔒 Security

Security mechanisms include:
- Operation whitelist
- Argument validation
- Execution timeout
- Full audit logging
- Error isolation

Threats mitigated:
- Prompt injection
- Code injection
- Denial of Service
- Data exfiltration
- Privilege escalation

---

## 📈 Scalability

### Current (Vertical Scaling)
Single orchestrator process handling requests sequentially.

### Future (Horizontal Scaling)
- Load balancer
- Multiple orchestrator instances
- LLM pool
- Queue-based processing
- Async execution

Distributed tracing supported via OpenTelemetry.

---

## 🛠️ Technology Stack

Backend:
- Python 3.9+
- YAML configuration
- asyncio (future)

LLM:
- Ollama
- Mistral 7B Instruct
- 8K context window

Frontend:
- Streamlit
- CLI (future)

Infrastructure:
- Ubuntu / WSL2
- Docker (future)
- Docker Compose (future)

---

## 🔄 Design Patterns Used

- Strategy Pattern
- Factory Pattern
- Template Method
- Observer Pattern

---

## 📊 Metrics & Monitoring

Key metrics:
- Total latency
- LLM planning latency
- Success rate
- Error rate
- Resource usage
- Operations per minute

---

## 🚀 Architectural Evolution

Phase 1: PoC  
User → Streamlit → Orchestrator → LLM → Specialists

Phase 2: Production Ready  
Load Balancer + Multiple Orchestrators + Worker Pool

Phase 3: Distributed  
API Gateway + Kubernetes + Service Mesh + Message Broker

---

## 📚 References

- ReAct Paper
- Chain-of-Thought Prompting
- AutoGPT Agents

Inspired by:
- LangChain
- AutoGen
- CrewAI

---

## 🤝 Contributing

Changes should follow ADR (Architecture Decision Record) process.

Example:
ADR-001: Add LLM Plan Cache using Redis with TTL.

---

**Created with 🏗️ by Flavio Lopes | Architecture v1.0 | 2026**
