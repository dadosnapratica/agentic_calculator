# 🧮 Agentic Calculator

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python 3.9+](https://img.shields.io/badge/python-3.9+-blue.svg)](https://www.python.org/downloads/)
[![Ollama](https://img.shields.io/badge/LLM-Ollama-00A67E?logo=ollama)](https://ollama.ai/)
[![Mistral](https://img.shields.io/badge/Model-Mistral%207B-orange)](https://mistral.ai/)
[![Streamlit](https://img.shields.io/badge/UI-Streamlit-FF4B4B?logo=streamlit)](https://streamlit.io/)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg)](CONTRIBUTING.md)

> **Demostrando una arquitectura multiagente con LLM 100% local.**  
> Construido para desarrolladores y arquitectos que aprenden a diseñar sistemas autónomos de IA.

---

> 🇧🇷 [Versão Original em Português (Brasil)](README_BR.md)  
> **Aviso:** Esta es la versión original de la documentación técnica. Para máxima precisión conceptual y técnica, utilice preferentemente esta versión.

> 🇺🇸 [English Version](README.md)  
> **Disclaimer:** Esta documentación también está disponible en inglés. Para referencia técnica oficial, consulte las versiones en portugués o inglés.

> 🇪🇸 [Documentación en Español](README_ES.md)  
> **Aviso:** La documentación también está disponible en español. Para mayor precisión técnica, consulte la versión original en portugués o la versión en inglés.

---


## 🎯 ¿Qué es este proyecto?

Este proyecto no es solo una calculadora: es una implementación de referencia completa de patrones modernos de arquitectura agentic.

Piénsalo como:
- 📚 Un marco educativo para entender la orquestación de agentes de IA
- 🏗️ Una base lista para producción para construir sistemas autónomos complejos
- 🔒 Una alternativa centrada en la privacidad frente a servicios de IA en la nube
- 💡 Un modelo para bots de trading, pipelines de automatización y asistentes inteligentes

### ¿Qué lo hace "Agentic"?

Los programas tradicionales siguen lógica fija: if this, then that.

Los sistemas agentic usan IA para:
1. Entender la intención en lenguaje natural
2. Planificar la descomposición en pasos
3. Orquestar agentes especializados
4. Ejecutar de forma segura con validación
5. Aprender del feedback (mejora futura)

```
User: "Calculate the average of 10, 20, 30 and then square it"

Traditional Code:          Agentic System:
❌ Needs explicit         ✅ LLM understands intent
  function for this      ✅ Plans: [mean() → square()]
❌ Breaks on variations   ✅ Adapts to natural language
❌ No reasoning           ✅ Generates execution plan
```

---

## ✨ Características principales

### 🧠 Comprensión de Lenguaje Natural
```bash
Input:  "Add 15 and 25, then multiply by 2"
Output: 80.0

# Detrás de escena:
# LLM convierte → [add(15,25), multiply($result_0, 2)]
```

### 🎯 Orquestación Multi-Agente
```python
# Especialistas manejan dominios específicos
BasicOperations     → +, -, ×, ÷
AdvancedOperations  → √, ^, log
StatisticsOps       → mean, median, σ
```

### 🔒 Ejecución en Sandbox Segura
```yaml
# Seguridad basada en whitelist
allowed_operations:
  - add
  - multiply
  # ❌ system_call - BLOQUEADO
  # ❌ file_delete - BLOQUEADO
```

### 📊 Interfaz Moderna con Streamlit
- **Interfaz web**: bonita, responsiva, en tiempo real
- **Modo CLI**: para automatización y scripting
- **Listo para API**: extiende a endpoints REST

---

## 🏗️ Visión General de la Arquitectura

### Flujo de alto nivel

```
┌─────────────────────────────────────────────┐
│ User Input (Natural Language)               │
│ "Calculate mean of 10,20,30 and square it"  │
└──────────────────┬──────────────────────────┘
             │
             ▼
┌─────────────────────────────────────────────┐
│         Orchestrator (Brain)                │
│ • Recibe entrada                            │
│ • Llama al LLM para generar el plan         │
│ • Valida seguridad                          │
│ • Delegar a especialistas                   │
└──────────────┬──────────────────────────────┘
          │
   ┌──────────┼──────────┐
   ▼          ▼          ▼
┌────────┐ ┌────────┐ ┌────────┐
│ Basic  │ │Advanced│ │ Stats  │
│  Ops   │ │  Ops   │ │  Ops   │
└────────┘ └────────┘ └────────┘
          │
          ▼
      ┌─────────────┐
      │ LLM (Local) │
      │   Mistral   │
      └─────────────┘
```

### ¿Por qué esta arquitectura?

| Patrón | Beneficio | Ejemplo |
|--------|----------|---------|
| **Separación de responsabilidades** | Cada componente tiene un único trabajo | El orquestador coordina, los especialistas ejecutan |
| **Principio Open/Closed** | Extiende sin modificar el núcleo | Añadir un nuevo especialista = 5 líneas de código |
| **Inyección de dependencias** | Testeable y flexible | Mock del LLM para pruebas unitarias |
| **Diseño a prueba de fallos** | Manejo de errores elegante | ¿Operación inválida? El sistema registra y continúa |

**📖 Para más detalles, ver [ARCHITECTURE.md](ARCHITECTURE.md)**

---

## 🚀 Inicio Rápido (5 Minutos)

### Requisitos

- **Python 3.9+**
- **8GB RAM** (16GB recomendado)
- **5GB de disco** (para el modelo LLM)

### Instalación

#### 1. Instalar Ollama (Servidor LLM)

```bash
# macOS / Linux
curl -fsSL https://ollama.ai/install.sh | sh

# Windows
# Descargar desde https://ollama.ai/download
```

#### 2. Descargar el Modelo

```bash
ollama pull mistral:7b-instruct
```

#### 3. Clonar y Configurar

```bash
# Clonar repositorio
git clone https://github.com/yourusername/agentic-calculator.git
cd agentic-calculator

# Crear entorno virtual
python3 -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate

# Instalar dependencias
pip install -r requirements.txt
```

#### 4. ¡Ejecutar!

```bash
# Terminal 1: Iniciar Ollama (si no se inicia automáticamente)
ollama serve

# Terminal 2: Ejecutar la calculadora
python main.py

# O usar la UI de Streamlit
streamlit run app.py
```

---

## 💡 Ejemplos de Uso

### Modo CLI

```bash
$ python main.py

🤖 Calculadora Agentic
============================================================

🧮 Usted: Add 100 and 50
🤖 Agente: 150.0

🧮 Usted: Calculate average of 5, 10, 15 and take square root
🤖 Agente: 3.162

🧮 Usted: salir
👋 ¡Hasta luego!
```

### Uso Programático

```python
from core.orchestrator import CalculatorOrchestrator

orchestrator = CalculatorOrchestrator()

result = orchestrator.execute("Add 5 and 3, then multiply by 2")

print(result['final_result'])  # 16.0
print(result['steps_executed'])  # 2
print(result['intermediate_results'])  # [8.0, 16.0]
```

### Multi-Paso Complejo

```python
# Entrada
"Calculate mean of 100, 200, 300, then take square root, then divide by 2"

# El LLM genera el plan:
{
  "steps": [
   {"operation": "mean", "args": [100, 200, 300]},      # → 200
   {"operation": "sqrt", "args": ["$result_0"]},        # → 14.14
   {"operation": "divide", "args": ["$result_1", 2]}    # → 7.07
  ]
}

# Resultado final: 7.07
```

---

## 🎓 Para Principiantes en Arquitectura Agentic

### Qué aprenderás

1. **Orquestación con LLMs**: Cómo usar LLMs como "cerebros" para planificar tareas
2. **Patrones de diseño de agentes**: Strategy, Factory, Observer aplicados a IA
3. **Ingeniería de prompts**: Crear prompts que generen salidas estructuradas
4. **Ejecución segura**: Sandboxing y validación en sistemas autónomos
5. **Arquitectura modular**: Construir sistemas de IA extensibles

### Ruta de aprendizaje

```
1. Ejecutar los ejemplos → Entender el flujo
2. Leer ARCHITECTURE.md → Comprender el diseño
3. Añadir un nuevo especialista → Practicar la extensión
4. Modificar prompts → Experimentar con el comportamiento del LLM
5. Construir tu propio agente → Aplicar al dominio
```

### Conceptos clave explicados

#### 🧠 ¿Qué es un "Orchestrator"?

Piénsalo como un director de orquesta:
- No toca instrumentos (no realiza cálculos)
- Lee la partitura (interpreta la intención del usuario vía LLM)
- Indica a cada músico cuándo tocar (delegera a especialistas)
- Asegura la armonía (valida y consolida resultados)

#### 🎯 ¿Qué es un "Specialist"?

Un experto de dominio que hace una cosa bien:
```python
# MAL: Objeto dios que lo hace todo
class Calculator:
   def add(self, a, b): ...
   def subtract(self, a, b): ...
   def plot_graph(self, data): ...  # ¡No relacionado!
   def send_email(self, msg): ...   # ¡No relacionado!

# BIEN: Especialistas enfocados
class BasicOperations:
   def add(self, a, b): return a + b
   def subtract(self, a, b): return a - b

class VisualizationOps:
   def plot_graph(self, data): ...
```

#### 🔗 ¿Qué es "$result_N"?

Referencia a resultados de pasos previos:
```json
{
  "steps": [
   {"operation": "add", "args": [5, 3]},           // Paso 0 → 8
   {"operation": "multiply", "args": ["$result_0", 2]}  // Usa 8 del paso 0
  ]
}
```

Esto permite encadenar operaciones sin codificar valores intermedios.

---

## 🧪 Pruebas

```bash
# Ejecutar todas las pruebas
pytest tests/

# Con coverage
pytest --cov=core --cov=specialists tests/

# Prueba específica
pytest tests/test_orchestrator.py -v
```

---

## 🔧 Configuración

### Personalizar operaciones

Editar `config.yaml`:

```yaml
security:
  allowed_operations:
   - "add"
   - "multiply"
   - "sin"        # Añadir trigonometría
   - "factorial"  # Añadir combinatoria
```

### Añadir nuevo especialista

```python
# 1. Crear especialista
# specialists/trigonometry.py
import math

class TrigonometryOperations:
   @staticmethod
   def sin(x):
      return math.sin(math.radians(x))

# 2. Registrar en el orquestador
# core/orchestrator.py
from specialists.trigonometry import TrigonometryOperations

self.specialists['sin'] = TrigonometryOperations.sin
```

¡Eso es todo! No se requieren cambios en el núcleo. 🎉

---

## 🌟 Aplicaciones en el Mundo Real

Esta arquitectura escala a sistemas de producción:

### 🤖 Trading Algorítmico
```python
# Reemplazar especialistas matemáticos por especialistas de trading
class TradingOperations:
   def analyze_volatility(symbol): ...
   def execute_order(symbol, quantity): ...
   def calculate_risk(portfolio): ...

# ¡Mismo orquestador, dominio diferente!
```

### 📹 Pipeline de Generación de Contenido
```python
class ContentOperations:
   def generate_script(topic): ...
   def create_images(script): ...
   def synthesize_voice(script): ...
   def edit_video(assets): ...
```

### 📊 Flujos de Trabajo de Análisis de Datos
```python
class DataOperations:
   def query_database(sql): ...
   def clean_data(df): ...
   def train_model(df): ...
   def visualize_results(predictions): ...
```

Mismos patrones. Diferentes especialistas. Posibilidades infinitas.

---

## 📊 Rendimiento

| Métrica | Valor | Notas |
|--------|-------|-------|
| **Latencia promedio** | 1-2s | Operación simple |
| **Multi-Paso (3 ops)** | 2-3s | Incluye planificación LLM |
| **Uso de memoria** | ~500MB | Con modelo 7B cargado |
| **Tasa de éxito** | 98%+ | En operaciones válidas |

### Consejos de optimización

- Usar modelo **7B** para velocidad (por defecto)
- Usar modelo **13B** para mejor razonamiento (más lento)
- Habilitar **GPU** para inferencia 3-5x más rápida
- Añadir **cache en Redis** para consultas repetidas

---

## 🗺️ Hoja de Ruta

### ✅ v1.0 (Actual)
- [x] Orquestación central
- [x] Operaciones matemáticas básicas
- [x] UI en Streamlit
- [x] Sandbox de seguridad
- [x] Documentación completa

### 🚧 v1.1 (Siguientes)
- [ ] API REST
- [ ] Soporte de variables (`x = 10`)
- [ ] Historial de operaciones
- [ ] Más especialistas (trig, stats)
- [ ] Despliegue con Docker

### 🔮 v2.0 (Futuro)
- [ ] Soporte Multi-LLM
- [ ] Visualización del grafo de ejecución
- [ ] Memoria conversacional
- [ ] Sistema de plugins

---

## 🤝 Contribuciones

¡Se aceptan contribuciones! Ver [CONTRIBUTING.md](CONTRIBUTING.md) para guías.

Buenas primeras issues:
- Añadir operaciones trigonométricas
- Mejorar mensajes de error
- Añadir más casos de prueba
- Traducir la UI a otros idiomas
- Crear setup con Docker

---

## 📚 Documentación

- **[ARCHITECTURE.md](ARCHITECTURE.md)** - Profundización en decisiones de diseño
- **[EXAMPLES.md](docs/EXAMPLES.md)** - Casos de uso avanzados

---

## 🐛 Solución de Problemas

### Problemas comunes

**Problema**: `Connection refused` a Ollama

```bash
# Solución: Iniciar el servidor Ollama
ollama serve
```

**Problema**: El LLM devuelve JSON inválido

```yaml
# Solución: Reducir la temperatura en config.yaml
llm:
  temperature: 0.0  # Más determinista
```

**Problema**: Operación bloqueada por el sandbox

```yaml
# Solución: Añadir a la whitelist en config.yaml
security:
  allowed_operations:
   - "your_operation"
```

¿Más problemas? Revisa [Issues](https://github.com/yourusername/agentic-calculator/issues) o abre uno nuevo.

---

## 📄 Licencia

Este proyecto está licenciado bajo MIT License - ver archivo [LICENSE](LICENSE).

**TL;DR**: Puedes usarlo comercialmente, modificarlo y distribuirlo—solo conserva el aviso de copyright.

---

## 🙏 Agradecimientos

- **[Ollama](https://ollama.ai/)** - Haciendo accesibles los LLMs locales
- **[Mistral AI](https://mistral.ai/)** - Excelente modelo de pesos abiertos
- **[Streamlit](https://streamlit.io/)** - Desarrollo rápido de UI
- **Comunidad Open Source** - Por la inspiración y herramientas

---

## Notas Finales

Este proyecto fue creado como una iniciativa educativa que demuestra cómo Python puede aplicarse al análisis de datos real y cómo la Inteligencia Artificial puede mejorar los flujos analíticos.

🌟 ¡Siéntete libre de contribuir y mejorar este proyecto!

## Tips 

Esperamos que nuestros servicios te resulten útiles y agradables. Si quieres mostrar un apoyo extra, ¿por qué no invitarnos a un café?

🍵 Tu apoyo no solo nos anima, sino que nos ayuda a seguir mejorando.

Para una pequeña contribución, puedes enviar USDT o un pago instantáneo brasileño (PIX) a nuestro código QR. ¡Cada café cuenta!

### Forma #1 - USDT:

![Coffee QR Code](https://raw.githubusercontent.com/dadosnapratica/buy_a_coffe_qrcodes/refs/heads/main/qr_code_usdt_enus_200px.png)

o enviar USDT a la dirección:
```text
0x3db4d1dd10b60c278f27bd1b2e2bd888d0f99f85
```

1. **Escanea el QR:** Abre tu wallet y escanea el QR de USDT.  
2. **Introduce el monto:** El precio de un café, alrededor de $3–$5.  
3. **Envía tu apoyo:** Confirma la transacción.

### Forma #2 - Wise transferencia internacional

![Coffee Wise QR Code](https://raw.githubusercontent.com/dadosnapratica/buy_a_coffe_qrcodes/refs/heads/main/wise_qrcode.jpeg)

O enviar pago a la dirección

```
https://wise.com/pay/me/flavion156
```

### Forma #3 - PIX (Brasil):

![Coffee QR Code](https://raw.githubusercontent.com/dadosnapratica/buy_a_coffe_qrcodes/refs/heads/main/qr_code_pix_bradesco.png)

1. **Escanea el QR:** Abre la app bancaria y escanea el QR de PIX.  
2. **Introduce el monto:** Aprox. $3–$5.  
3. **Envía tu apoyo:** Confirma el pago.

PIX es un sistema de pago digital en Brasil para pagos instantáneos 24/7. Si este proyecto te ayudó, considera comprarme un café.

---

## Autor

**Flavio Lopes** Difundiendo conocimiento práctico de datos para la toma de decisiones.

--- 

# 📬 Contacto

¿Preguntas, sugerencias o mejoras? Contáctame o contribuye directamente al repositorio.

- GitHub: https://github.com/orgs/dadosnapratica  
- LinkedIn: https://www.linkedin.com/in/flavionlopes/  
- Email: flavio.lopes@ideiasfactory.tech  
- WhatsApp: https://wa.me/5511996354436  
- Instagram: https://www.instagram.com/dadosnapratica/

---

Gracias nuevamente por tu increíble apoyo y por formar parte de nuestra comunidad. Tu contribución alimenta nuestra pasión y compromiso.  
⭐ Sigue aprendiendo. Sigue construyendo. Sigue compartiendo conocimiento. ⭐

---

## 🌟 Historial de Stars

Si este proyecto te ayudó, considera darle una ⭐!

[![Star History Chart](https://api.star-history.com/svg?repos=yourusername/agentic-calculator&type=Date)](https://star-history.com/#yourusername/agentic-calculator&Date)

---

## 📈 Estadísticas de GitHub

![GitHub stars](https://img.shields.io/github/stars/dadosnapratica/agentic_calculator?style=social)
![GitHub forks](https://img.shields.io/github/forks/dadosnapratica/agentic_calculator?style=social)
![GitHub watchers](https://img.shields.io/github/watchers/dadosnapratica/agentic_calculator?style=social)

---

<div align="center">

**Construido con ❤️ para la comunidad de IA**

[⭐ Star](https://github.com/dadosnapratica/agentic_calculator) •
[🍴 Fork](https://github.com/dadosnapratica/agentic_calculator/fork) •
[🐛 Reportar Bug](https://github.com/dadosnapratica/agentic_calculator/issues)


Hecho por [Flavio Lopes](https://github.com/fnldesign) | 2026

</div>
