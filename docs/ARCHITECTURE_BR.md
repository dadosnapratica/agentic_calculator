# 🏗️ Arquitetura - Calculadora Agentic PoC

**Documentação técnica detalhada da arquitetura multi-agente com LLM local**

---

> 🇧🇷 [Versão Original em Português (Brasil)](ARCHITECTURE_BR.md)  
> **Aviso:** Esta é a versão original da documentação técnica. Para máxima precisão conceitual e técnica, utilize preferencialmente esta versão.

> 🇺🇸 [English Version](ARCHITECTURE.md)  
> **Disclaimer:** This documentation is also available in English. For official technical reference, consult the Portuguese or English versions.

> 🇪🇸 [Documentación en Español](ARCHITECTURE_ES.md)  
> **Aviso:** La documentación también está disponible en español. Para mayor precisión técnica, consulte la versión original en portugués o la versión en inglés.

---


## 📋 Índice

- [Visão Geral](#-visão-geral)
- [Princípios de Design](#-princípios-de-design)
- [Componentes](#-componentes)
- [Fluxo de Dados](#-fluxo-de-dados)
- [Decisões Arquiteturais](#-decisões-arquiteturais)
- [Segurança](#-segurança)
- [Escalabilidade](#-escalabilidade)
- [Stack Tecnológica](#-stack-tecnológica)

---

## 🎯 Visão Geral

### Arquitetura em Camadas

```
┌─────────────────────────────────────────────────────────┐
│                  CAMADA DE APRESENTAÇÃO                 │
│  ┌─────────────┐              ┌─────────────┐          │
│  │  Streamlit  │              │     CLI     │          │
│  │     UI      │              │  Interface  │          │
│  └─────────────┘              └─────────────┘          │
└──────────────────────┬──────────────────────────────────┘
                       │
                       │ User Input (Natural Language)
                       │
┌──────────────────────▼──────────────────────────────────┐
│               CAMADA DE ORQUESTRAÇÃO                    │
│  ┌──────────────────────────────────────────────────┐  │
│  │         CalculatorOrchestrator                   │  │
│  │  • Parse de entrada                              │  │
│  │  • Planejamento (via LLM)                        │  │
│  │  • Validação de segurança                        │  │
│  │  • Execução de steps                             │  │
│  │  • Consolidação de resultados                    │  │
│  └──────────────────────────────────────────────────┘  │
└──────────────────────┬──────────────────────────────────┘
                       │
                       │ Delegação
                       │
┌──────────────────────▼──────────────────────────────────┐
│                CAMADA DE SPECIALISTS                    │
│  ┌──────────┐    ┌──────────┐    ┌──────────┐         │
│  │  Basic   │    │ Advanced │    │  Stats   │         │
│  │  Ops     │    │   Ops    │    │   Ops    │         │
│  │ +, -, *  │    │ √, ^, log│    │ μ, σ, Σ  │         │
│  └──────────┘    └──────────┘    └──────────┘         │
└──────────────────────┬──────────────────────────────────┘
                       │
                       │ LLM Calls
                       │
┌──────────────────────▼──────────────────────────────────┐
│                  CAMADA DE MODELO                       │
│  ┌──────────────────────────────────────────────────┐  │
│  │              LLMClient                           │  │
│  │  • Comunicação com Ollama                        │  │
│  │  • Prompt engineering                            │  │
│  │  • Parse de respostas                            │  │
│  └──────────────────────────────────────────────────┘  │
└──────────────────────┬──────────────────────────────────┘
                       │
                       │ HTTP API
                       │
┌──────────────────────▼──────────────────────────────────┐
│                CAMADA DE INFRAESTRUTURA                 │
│  ┌──────────────────────────────────────────────────┐  │
│  │              Ollama Server                       │  │
│  │  • Mistral 7B Instruct                           │  │
│  │  • GPU/CPU inference                             │  │
│  │  • Context window: 8K tokens                     │  │
│  └──────────────────────────────────────────────────┘  │
└─────────────────────────────────────────────────────────┘

┌─────────────────────────────────────────────────────────┐
│                 CAMADA TRANSVERSAL                      │
│  ┌──────────┐    ┌──────────┐    ┌──────────┐         │
│  │ Security │    │ Logging  │    │  Config  │         │
│  │  Sandbox │    │ Auditing │    │   YAML   │         │
│  └──────────┘    └──────────┘    └──────────┘         │
└─────────────────────────────────────────────────────────┘
```

---

## 🧩 Princípios de Design

### 1. Separation of Concerns

Cada componente tem **responsabilidade única**:

- **Orchestrator**: Coordenação e fluxo
- **LLMClient**: Comunicação com modelo
- **Specialists**: Execução de operações
- **Sandbox**: Validação de segurança

### 2. Open/Closed Principle

**Aberto para extensão, fechado para modificação**:

```python
# ✅ Adicionar novo specialist
class NewOperations:
    @staticmethod
    def new_op(x):
        return x

# Registrar sem modificar código existente
orchestrator.specialists['new_op'] = NewOperations.new_op
```

### 3. Dependency Injection

Componentes recebem dependências via construtor:

```python
class CalculatorOrchestrator:
    def __init__(self, config_path="config.yaml"):
        self.llm = LLMClient(self.config['llm'])
        self.sandbox = Sandbox(self.config['security'])
```

### 4. Fail-Safe

Sistema **falha graciosamente**:

```python
try:
    result = execute_operation()
except Exception as e:
    logger.error(f"Erro: {e}")
    return {"success": False, "error": str(e)}
```

---

## 🔧 Componentes

### 1. CalculatorOrchestrator

**Responsabilidade**: Coordenar todo o fluxo de execução

**Métodos principais**:

```python
class CalculatorOrchestrator:
    def execute(self, user_input: str) -> Dict[str, Any]:
        """
        Pipeline completo:
        1. Planning (LLM)
        2. Validation (Security)
        3. Execution (Specialists)
        4. Consolidation (Results)
        """
        
    def _execute_plan(self, steps: List[Dict]) -> List[float]:
        """Executa sequência de operações"""
        
    def _resolve_args(self, args: List, results: List[float]) -> List:
        """Resolve referências entre steps ($result_N)"""
```

**Diagrama de Estados**:

```
┌──────────┐
│  IDLE    │
└────┬─────┘
     │ user_input
     ▼
┌──────────┐
│ PLANNING │ ◄── LLM gera JSON de steps
└────┬─────┘
     │ plan_ready
     ▼
┌──────────┐
│VALIDATING│ ◄── Sandbox valida operações
└────┬─────┘
     │ validated
     ▼
┌──────────┐
│EXECUTING │ ◄── Loop sobre steps
└────┬─────┘
     │ all_steps_done
     ▼
┌──────────┐
│  DONE    │ → Retorna resultado
└──────────┘
```

---

### 2. LLMClient

**Responsabilidade**: Comunicação com modelo de linguagem

**Interface**:

```python
class LLMClient:
    def generate(self, prompt: str, system: str = None) -> str:
        """Gera resposta da LLM"""
        
    def plan_operations(self, user_input: str) -> Dict[str, Any]:
        """Converte linguagem natural em JSON de operações"""
```

**Prompt Engineering**:

```python
system_prompt = """Você é um assistente que converte pedidos em linguagem natural 
para uma sequência de operações matemáticas.

REGRAS:
1. Retorne APENAS um JSON válido
2. Cada operação deve ter: operation, args, description
3. Operações disponíveis: add, subtract, multiply, divide, sqrt, power, mean, median
4. Use números exatos (não arredonde)
5. A sequência deve ser executável em ordem

EXEMPLO:
Input: "Some 5 e 3, depois multiplique por 2"
Output:
{
  "steps": [
    {"operation": "add", "args": [5, 3], "description": "Somar 5 + 3"},
    {"operation": "multiply", "args": ["$result_0", 2], "description": "Multiplicar por 2"}
  ]
}

Use $result_N para referenciar resultado do step N."""
```

**Otimizações**:

- ✅ Temperature baixa (0.1) para determinismo
- ✅ Extração robusta de JSON da resposta
- ✅ Timeout de 60s
- ✅ Retry em caso de falha

---

### 3. Specialists

**Responsabilidade**: Executar operações específicas

**Design Pattern**: Strategy Pattern

```python
# Interface implícita (duck typing)
class Specialist:
    @staticmethod
    def operation(*args) -> float:
        """Executa operação e retorna resultado"""
```

**Implementações**:

#### BasicOperations

```python
class BasicOperations:
    @staticmethod
    def add(*args) -> float:
        """Soma N números"""
        return sum(args)
```

#### AdvancedOperations

```python
class AdvancedOperations:
    @staticmethod
    def sqrt(x) -> float:
        """Raiz quadrada com validação"""
        if x < 0:
            raise ValueError("Raiz de negativo")
        return math.sqrt(x)
```

#### StatisticsOperations

```python
class StatisticsOperations:
    @staticmethod
    def mean(*args) -> float:
        """Média aritmética"""
        return statistics.mean(args)
```

---

### 4. Sandbox

**Responsabilidade**: Garantir segurança na execução

**Mecanismos**:

```python
class Sandbox:
    def validate_operation(self, operation: str) -> bool:
        """Whitelist de operações permitidas"""
        if operation not in self.allowed_operations:
            raise SecurityError(f"Operação '{operation}' não permitida")
        return True
    
    def execute_safe(self, func: Callable, *args) -> Any:
        """Executa com timeout e isolamento"""
        # Implementação com signal.alarm (Unix) ou threading.Timer (Windows)
```

**Políticas de Segurança**:

1. ✅ Whitelist de operações
2. ✅ Timeout por operação (30s padrão)
3. ✅ Validação de argumentos
4. ✅ Logging de todas as execuções
5. ✅ Isolamento de erros

---

## 🔄 Fluxo de Dados

### Exemplo Completo: "Some 5 e 3, depois multiplique por 2"

```
┌─────────────────────────────────────────────┐
│ 1. USER INPUT                               │
│    "Some 5 e 3, depois multiplique por 2"   │
└──────────────┬──────────────────────────────┘
               │
               ▼
┌─────────────────────────────────────────────┐
│ 2. ORCHESTRATOR.execute()                   │
│    • Recebe string                          │
│    • Chama LLM para planejamento            │
└──────────────┬──────────────────────────────┘
               │
               ▼
┌─────────────────────────────────────────────┐
│ 3. LLM PLANNING                             │
│    Input: "Some 5 e 3, depois mult por 2"   │
│    System Prompt: [instruções de JSON]      │
│                                             │
│    LLM Response:                            │
│    {                                        │
│      "steps": [                             │
│        {"operation": "add",                 │
│         "args": [5, 3],                     │
│         "description": "Somar 5+3"},        │
│        {"operation": "multiply",            │
│         "args": ["$result_0", 2],           │
│         "description": "Mult por 2"}        │
│      ]                                      │
│    }                                        │
└──────────────┬──────────────────────────────┘
               │
               ▼
┌─────────────────────────────────────────────┐
│ 4. VALIDATION                               │
│    Sandbox.validate_operation("add") ✅     │
│    Sandbox.validate_operation("multiply") ✅ │
└──────────────┬──────────────────────────────┘
               │
               ▼
┌─────────────────────────────────────────────┐
│ 5. EXECUTION - Step 0                       │
│    operation: "add"                         │
│    args: [5, 3]                             │
│    resolved_args: [5, 3]                    │
│    ↓                                        │
│    specialist = BasicOperations.add         │
│    result = add(5, 3)                       │
│    result = 8.0 ✅                          │
│    results = [8.0]                          │
└──────────────┬──────────────────────────────┘
               │
               ▼
┌─────────────────────────────────────────────┐
│ 6. EXECUTION - Step 1                       │
│    operation: "multiply"                    │
│    args: ["$result_0", 2]                   │
│    ↓                                        │
│    _resolve_args():                         │
│      "$result_0" → results[0] = 8.0         │
│    resolved_args: [8.0, 2]                  │
│    ↓                                        │
│    specialist = BasicOperations.multiply    │
│    result = multiply(8.0, 2)                │
│    result = 16.0 ✅                         │
│    results = [8.0, 16.0]                    │
└──────────────┬──────────────────────────────┘
               │
               ▼
┌─────────────────────────────────────────────┐
│ 7. CONSOLIDATION                            │
│    final_result = results[-1] = 16.0        │
│    ↓                                        │
│    return {                                 │
│      "success": True,                       │
│      "input": "Some 5 e 3...",              │
│      "plan": {...},                         │
│      "steps_executed": 2,                   │
│      "intermediate_results": [8.0, 16.0],   │
│      "final_result": 16.0                   │
│    }                                        │
└──────────────┬──────────────────────────────┘
               │
               ▼
┌─────────────────────────────────────────────┐
│ 8. PRESENTATION                             │
│    Streamlit: "✅ Resultado: 16.0"          │
│    CLI: "🤖 Agente: 16.0"                   │
└─────────────────────────────────────────────┘
```

---

## 🎨 Decisões Arquiteturais

### Por Que LLM Local?

**Alternativas consideradas**:

| Opção | Prós | Contras | Decisão |
|-------|------|---------|---------|
| OpenAI API | Alta qualidade | Custo, privacidade | ❌ Rejeitado |
| Anthropic API | Excelente reasoning | Custo, latência | ❌ Rejeitado |
| **Ollama Local** | Privacidade, custo zero | Setup inicial | ✅ **Escolhido** |
| llama.cpp | Máximo controle | Complexidade | ⚠️ Alternativa |

**Justificativa**: Para uma PoC educacional e base para sistemas de trading, privacidade e custo zero são críticos.

---

### Por Que Streamlit?

**Alternativas consideradas**:

| Framework | Prós | Contras | Decisão |
|-----------|------|---------|---------|
| Flask + HTML/CSS | Controle total | Muito código | ❌ Overhead |
| FastAPI + React | Moderno, rápido | 2 stacks separadas | ❌ Complexo |
| **Streamlit** | Rápido, pythônico | Menos flexível | ✅ **Escolhido** |
| Gradio | Fácil, ML-focused | Menos customizável | ⚠️ Alternativa |

**Justificativa**: Para PoC, velocidade de desenvolvimento > flexibilidade.

---

### Por Que Arquitetura Multi-Agente?

**Alternativas**:

1. **Monolítico**: Tudo em um arquivo
   - ❌ Difícil de testar
   - ❌ Difícil de escalar
   - ❌ Acoplamento alto

2. **MVC Tradicional**: Model-View-Controller
   - ⚠️ Não captura conceito de "agentes"
   - ⚠️ Menos intuitivo para IA

3. **Multi-Agente**: Orchestrator + Specialists
   - ✅ Modular
   - ✅ Testável
   - ✅ Escalável
   - ✅ Reflete conceito de "delegação"

**Benefícios**:

```python
# ❌ Monolítico
def calculate(input):
    if "soma" in input:
        return do_addition()
    elif "multiplica" in input:
        return do_multiplication()
    # ... 50 linhas de if/elif

# ✅ Multi-Agente
orchestrator.execute(input)
# → LLM decide qual specialist chamar
# → Specialist executa
# → Orchestrator consolida
```

---

## 🔒 Segurança

### Camadas de Segurança

#### 1. Whitelist de Operações

```python
# config.yaml
security:
  allowed_operations:
    - "add"
    - "multiply"
    # "rm_file" ❌ NÃO na whitelist
```

#### 2. Validação de Argumentos

```python
def sqrt(x):
    if x < 0:
        raise ValueError("Raiz de negativo")
    if not isinstance(x, (int, float)):
        raise TypeError("Argumento deve ser número")
```

#### 3. Timeout de Execução

```python
def execute_safe(func, *args, timeout=30):
    signal.alarm(timeout)
    try:
        return func(*args)
    finally:
        signal.alarm(0)
```

#### 4. Logging Completo

```python
logger.info(f"EXEC: {operation}({args}) by user_id={user_id}")
# Auditoria de quem executou o que e quando
```

#### 5. Isolamento de Erros

```python
try:
    result = specialist.execute(args)
except Exception as e:
    logger.error(f"Erro isolado: {e}")
    # Sistema continua funcionando
```

---

### Modelo de Ameaças

| Ameaça | Mitigação | Status |
|--------|-----------|--------|
| **Prompt Injection** | Whitelist de operações | ✅ Mitigado |
| **Code Injection** | Sem eval/exec | ✅ Mitigado |
| **DoS** | Timeout por operação | ✅ Mitigado |
| **Data Exfiltration** | Operações isoladas | ✅ Mitigado |
| **Privilege Escalation** | Sem sudo/admin | ✅ Mitigado |

---

## 📈 Escalabilidade

### Scaling Vertical (Atual)

```
┌─────────────────────┐
│   Single Process    │
│  ┌───────────────┐  │
│  │ Orchestrator  │  │
│  └───────┬───────┘  │
│          │          │
│     ┌────┴────┐     │
│     │ LLM API │     │
│     └─────────┘     │
└─────────────────────┘
```

**Limites**:
- 1 request por vez
- CPU bound no LLM
- Memória limitada

---

### Scaling Horizontal (Futuro)

```
┌──────────────┐
│ Load Balancer│
└──────┬───────┘
       │
   ┌───┴───┐
   │       │
   ▼       ▼
┌────┐   ┌────┐
│Orch│   │Orch│  ← Múltiplas instâncias
│ 1  │   │ 2  │
└─┬──┘   └─┬──┘
  │        │
  └────┬───┘
       │
   ┌───▼───┐
   │  LLM  │  ← Pool de modelos
   │ Pool  │
   └───────┘
```

**Estratégias**:

1. **Queue-based**:
```python
# Redis Queue
queue.enqueue(orchestrator.execute, user_input)
```

2. **Microservices**:
```
API Gateway → Orchestrator Service → Specialist Services
                        ↓
                    LLM Service
```

3. **Async Processing**:
```python
async def execute(user_input):
    plan = await llm.plan(user_input)
    tasks = [specialist.execute(step) for step in plan]
    results = await asyncio.gather(*tasks)
```

---

### Distributed Tracing

```python
# OpenTelemetry
from opentelemetry import trace

tracer = trace.get_tracer(__name__)

with tracer.start_as_current_span("execute_operation"):
    with tracer.start_as_current_span("llm_planning"):
        plan = llm.plan(input)
    
    with tracer.start_as_current_span("execution"):
        result = execute_plan(plan)
```

---

## 🛠️ Stack Tecnológica

### Core Stack

```yaml
Backend:
  Linguagem: Python 3.9+
  Framework Async: asyncio (futuro)
  Config: YAML
  
LLM:
  Servidor: Ollama
  Modelo: Mistral 7B Instruct
  Context: 8K tokens
  Quantização: Q5_K_M
  
Frontend:
  Web: Streamlit 1.30+
  CLI: Click (futuro)
  
Infraestrutura:
  OS: Ubuntu 24 (WSL2)
  Containerização: Docker (futuro)
  Orquestração: Docker Compose (futuro)
```

### Dependencies

```txt
# Core
pyyaml>=6.0          # Configuração
requests>=2.31.0     # HTTP cliente

# UI
streamlit>=1.30.0    # Web interface

# Utilities (futuro)
redis>=4.5.0         # Queue/Cache
celery>=5.3.0        # Task queue
fastapi>=0.100.0     # API REST
```

---

## 🔄 Padrões de Design Utilizados

### 1. Strategy Pattern
```python
# Specialists são strategies
specialists = {
    'add': BasicOperations.add,
    'multiply': BasicOperations.multiply
}
```

### 2. Factory Pattern
```python
def create_specialist(operation: str):
    if operation in ['add', 'subtract']:
        return BasicOperations
    elif operation in ['sqrt', 'power']:
        return AdvancedOperations
```

### 3. Template Method
```python
class BaseOrchestrator:
    def execute(self, input):
        plan = self.plan(input)      # Hook
        validated = self.validate(plan)
        result = self.run(validated)
        return self.consolidate(result)
```

### 4. Observer Pattern (Logging)
```python
class LoggingObserver:
    def update(self, event):
        logger.info(f"Event: {event}")

orchestrator.attach(LoggingObserver())
```

---

## 📊 Métricas e Monitoramento

### Métricas Importantes

```python
# Performance
- latency_llm_planning_ms
- latency_execution_ms
- latency_total_ms

# Negócio
- operations_per_minute
- success_rate
- error_rate_by_type

# Recursos
- memory_usage_mb
- cpu_usage_percent
- llm_tokens_consumed
```

### Exemplo de Dashboard

```
┌─────────────────────────────────────┐
│  Calculadora PoC - Metrics          │
├─────────────────────────────────────┤
│  Requests/min: 45      ↑ 15%        │
│  Success Rate: 98.5%   ✅           │
│  Avg Latency:  2.1s    ↓ 0.3s       │
│  LLM Tokens:   15K     ↑ 2K         │
├─────────────────────────────────────┤
│  Top Operations:                    │
│  1. add         45%                 │
│  2. multiply    30%                 │
│  3. mean        15%                 │
└─────────────────────────────────────┘
```

---

## 🚀 Evolução Arquitetural

### Fase 1: PoC (Atual)
```
User → Streamlit → Orchestrator → LLM → Specialists
```

### Fase 2: Production-Ready
```
User → Nginx → Load Balancer → [Orchestrator1, Orchestrator2] 
                                      ↓
                                   LLM Pool
                                      ↓
                                  Redis Queue → Worker Pool
```

### Fase 3: Distributed
```
User → API Gateway → Orchestrator Cluster (K8s)
                           ↓
                    Service Mesh (Istio)
                           ↓
        [LLM Service] [Specialist Services] [Cache]
                           ↓
                    Message Broker (Kafka)
```

---

## 📚 Referências

### Papers e Artigos

- [ReAct: Synergizing Reasoning and Acting in Language Models](https://arxiv.org/abs/2210.03629)
- [Chain-of-Thought Prompting Elicits Reasoning](https://arxiv.org/abs/2201.11903)
- [AutoGPT: Building Agents with LLMs](https://arxiv.org/abs/2303.12712)

### Projetos Inspiradores

- [LangChain Agents](https://github.com/hwchase17/langchain)
- [AutoGen](https://github.com/microsoft/autogen)
- [CrewAI](https://github.com/joaomdmoura/crewAI)

---

## 🤝 Contribuindo para Arquitetura

### Como Propor Mudanças

1. Abra uma **ADR** (Architecture Decision Record)
2. Descreva o problema
3. Liste alternativas
4. Justifique decisão
5. Documente trade-offs

### Template ADR

```markdown
# ADR-001: Adicionar Cache de Planos LLM

## Status
Proposto

## Contexto
Queries repetidas geram custo desnecessário de LLM

## Decisão
Implementar Redis cache com TTL de 1h

## Consequências
+ 30% redução de chamadas LLM
+ Sub-100ms para queries cached
- Adiciona dependência Redis
- Necessita invalidação manual
```

---

**Feito com 🏗️ por Flavio Lopes | Arquitetura v1.0 | 2026**
