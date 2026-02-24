
# 🏗️ Arquitectura - Calculadora Agentic PoC

**Documentación técnica detallada de la arquitectura multi‑agente con LLM local**

---

> 🇧🇷 [Versão Original em Português (Brasil)](ARCHITECTURE_BR.md)  
> **Aviso:** Esta é a versão original da documentação técnica. Para máxima precisão conceitual e técnica, utilize preferencialmente esta versão.

> 🇺🇸 [English Version](ARCHITECTURE.md)  
> **Disclaimer:** This documentation is also available in English. For official technical reference, consult the Portuguese or English versions.

> 🇪🇸 [Documentación en Español](ARCHITECTURE_ES.md)  
> **Aviso:** La documentación también está disponible en español. Para mayor precisión técnica, consulte la versión original en portugués o la versión en inglés.

---


## 📋 Índice

- Visión General
- Principios de Diseño
- Componentes
- Flujo de Datos
- Decisiones Arquitectónicas
- Seguridad
- Escalabilidad
- Stack Tecnológico

---

## 🎯 Visión General

### Arquitectura en Capas

Capa de Presentación → Capa de Orquestación → Capa de Especialistas → Capa de Modelo → Capa de Infraestructura  

Capa Transversal: Seguridad, Logging y Configuración.

---

## 🧩 Principios de Diseño

### 1. Separación de Responsabilidades
Cada componente posee una **responsabilidad única**:

- Orchestrator: Coordinación y flujo
- LLMClient: Comunicación con el modelo
- Specialists: Ejecución de operaciones
- Sandbox: Validación de seguridad

### 2. Principio Abierto/Cerrado
El sistema está abierto para extensiones y cerrado para modificaciones.

### 3. Inyección de Dependencias
Los componentes reciben sus dependencias mediante el constructor.

### 4. Fail‑Safe
El sistema falla de forma controlada y devuelve errores estructurados.

---

## 🔧 Componentes

### CalculatorOrchestrator
Responsable de coordinar todo el pipeline:

1. Planificación (LLM)
2. Validación (Seguridad)
3. Ejecución (Specialists)
4. Consolidación de resultados

### LLMClient
Gestiona la comunicación con el modelo de lenguaje:

- Generación de respuestas
- Conversión de lenguaje natural a operaciones estructuradas

### Specialists
Ejecutan operaciones específicas siguiendo el **Strategy Pattern**:

- Operaciones básicas
- Operaciones avanzadas
- Operaciones estadísticas

### Sandbox
Garantiza la ejecución segura mediante:

- Lista blanca de operaciones
- Timeout de ejecución
- Validación de argumentos
- Registro de auditoría
- Aislamiento de errores

---

## 🔄 Flujo de Datos

Entrada del usuario → Orchestrator → Planificación LLM → Validación → Ejecución → Consolidación → Presentación.

El resultado final incluye:
- Resultado final
- Resultados intermedios
- Plan ejecutado
- Metadatos de ejecución

---

## 🎨 Decisiones Arquitectónicas

### ¿Por qué un LLM Local?

Seleccionado por:

- Privacidad
- Costo operativo cero
- Experimentación local
- Base para sistemas sensibles como trading

### ¿Por qué Streamlit?

Elegido debido a:

- Desarrollo rápido
- Integración nativa con Python
- Ideal para Proof of Concept

### ¿Por qué Arquitectura Multi‑Agente?

Beneficios:

- Diseño modular
- Facilidad de pruebas
- Escalabilidad
- Modelo natural de delegación entre agentes

---

## 🔒 Seguridad

Mecanismos principales:

- Lista blanca de operaciones
- Validación estricta de argumentos
- Timeout por operación
- Logging completo
- Aislamiento de fallos

Amenazas mitigadas:

- Prompt Injection
- Code Injection
- Denegación de servicio
- Exfiltración de datos
- Escalada de privilegios

---

## 📈 Escalabilidad

### Escalado Vertical (Actual)
Un único proceso de orquestación maneja las solicitudes.

### Escalado Horizontal (Futuro)

- Balanceador de carga
- Múltiples orquestadores
- Pool de modelos LLM
- Procesamiento basado en colas
- Ejecución asíncrona

Soporte para trazabilidad distribuida mediante OpenTelemetry.

---

## 🛠️ Stack Tecnológico

Backend:
- Python 3.9+
- Configuración YAML
- asyncio (futuro)

LLM:
- Ollama
- Mistral 7B Instruct
- Ventana de contexto de 8K tokens

Frontend:
- Streamlit
- CLI (futuro)

Infraestructura:
- Ubuntu / WSL2
- Docker (futuro)
- Docker Compose (futuro)

---

## 🔄 Patrones de Diseño Utilizados

- Strategy Pattern
- Factory Pattern
- Template Method
- Observer Pattern

---

## 📊 Métricas y Monitorización

Métricas clave:

- Latencia total
- Latencia del LLM
- Tasa de éxito
- Tasa de errores
- Uso de recursos
- Operaciones por minuto

---

## 🚀 Evolución Arquitectónica

Fase 1 — PoC  
Usuario → Streamlit → Orchestrator → LLM → Specialists

Fase 2 — Producción  
Balanceador + múltiples orquestadores + workers

Fase 3 — Arquitectura Distribuida  
API Gateway + Kubernetes + Service Mesh + Message Broker

---

## 📚 Referencias

- ReAct Paper
- Chain‑of‑Thought Prompting
- AutoGPT

Inspirado en:

- LangChain
- AutoGen
- CrewAI

---

## 🤝 Contribuciones

Los cambios deben seguir el proceso ADR (Architecture Decision Record).

Ejemplo:
ADR‑001 — Implementar caché de planes LLM usando Redis con TTL.

---

**Creado con 🏗️ por Flavio Lopes | Arquitectura v1.0 | 2026**
