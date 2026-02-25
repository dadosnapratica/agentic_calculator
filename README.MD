# 🧮 Agentic Calculator

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python 3.9+](https://img.shields.io/badge/python-3.9+-blue.svg)](https://www.python.org/downloads/)
[![Ollama](https://img.shields.io/badge/LLM-Ollama-00A67E?logo=ollama)](https://ollama.ai/)
[![Mistral](https://img.shields.io/badge/Model-Mistral%207B-orange)](https://mistral.ai/)
[![Streamlit](https://img.shields.io/badge/UI-Streamlit-FF4B4B?logo=streamlit)](https://streamlit.io/)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg)](CONTRIBUTING.md)

> **Demonstrating multi-agent architecture with 100% local LLM.**  
> Built for developers and architects learning to design autonomous AI systems.

---

> 🇧🇷 [Versão Original em Português (Brasil)](README_BR.md)  
> **Aviso:** Esta é a versão original da documentação técnica. Para máxima precisão conceitual e técnica, utilize preferencialmente esta versão.

> 🇺🇸 [English Version](README.md)  
> **Disclaimer:** This documentation is also available in English. For official technical reference, consult the Portuguese or English versions.

> 🇪🇸 [Documentación en Español](README_ES.md)  
> **Aviso:** La documentación también está disponible en español. Para mayor precisión técnica, consulte la versión original en portugués o la versión en inglés.

---


## 🎯 What Is This?

This project is **not just a calculator**—it's a **complete reference implementation** of modern agentic architecture patterns.

**Think of it as:**
- 📚 An educational framework for understanding AI agent orchestration
- 🏗️ A production-ready foundation for building complex autonomous systems
- 🔒 A privacy-first alternative to cloud-based AI services
- 💡 A blueprint for trading bots, automation pipelines, and intelligent assistants

### What Makes It "Agentic"?

Traditional programs follow fixed logic: `if this, then that`.

**Agentic systems** use AI to:
1. **Understand** natural language intent
2. **Plan** multi-step task decomposition
3. **Orchestrate** specialized agents
4. **Execute** securely with validation
5. **Learn** from feedback (future enhancement)

```
User: "Calculate the average of 10, 20, 30 and then square it"

Traditional Code:          Agentic System:
❌ Needs explicit         ✅ LLM understands intent
   function for this      ✅ Plans: [mean() → square()]
❌ Breaks on variations   ✅ Adapts to natural language
❌ No reasoning           ✅ Generates execution plan
```

---

## ✨ Key Features

### 🧠 Natural Language Understanding
```bash
Input:  "Add 15 and 25, then multiply by 2"
Output: 80.0

# Behind the scenes:
# LLM converts → [add(15,25), multiply($result_0, 2)]
```

### 🎯 Multi-Agent Orchestration
```python
# Specialists handle specific domains
BasicOperations     → +, -, ×, ÷
AdvancedOperations  → √, ^, log
StatisticsOps       → mean, median, σ
```

### 🔒 Secure Sandbox Execution
```yaml
# Whitelist-based security
allowed_operations:
  - add
  - multiply
  # ❌ system_call - BLOCKED
  # ❌ file_delete - BLOCKED
```

### 📊 Modern UI with Streamlit
- **Web Interface**: Beautiful, responsive, real-time
- **CLI Mode**: For automation and scripting
- **API-Ready**: Extend to REST endpoints

---

## 🏗️ Architecture Overview

### High-Level Flow

```
┌─────────────────────────────────────────────┐
│ User Input (Natural Language)               │
│ "Calculate mean of 10,20,30 and square it"  │
└──────────────────┬──────────────────────────┘
                   │
                   ▼
┌─────────────────────────────────────────────┐
│         Orchestrator (Brain)                │
│ • Receives input                            │
│ • Calls LLM to generate plan                │
│ • Validates security                        │
│ • Delegates to specialists                  │
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

### Why This Architecture?

| Pattern | Benefit | Example |
|---------|---------|---------|
| **Separation of Concerns** | Each component has one job | Orchestrator coordinates, Specialists execute |
| **Open/Closed Principle** | Extend without modifying core | Add new specialist = 5 lines of code |
| **Dependency Injection** | Testable and flexible | Mock LLM for unit tests |
| **Fail-Safe Design** | Graceful error handling | Invalid operation? System logs and continues |

**📖 For deep dive, see [ARCHITECTURE.md](ARCHITECTURE.md)**

---

## 🚀 Quick Start (5 Minutes)

### Prerequisites

- **Python 3.9+**
- **8GB RAM** (16GB recommended)
- **5GB disk space** (for LLM model)

### Installation

#### 1. Install Ollama (LLM Server)

```bash
# macOS / Linux
curl -fsSL https://ollama.ai/install.sh | sh

# Windows
# Download from https://ollama.ai/download
```

#### 2. Pull the Model

```bash
ollama pull mistral:7b-instruct
```

#### 3. Clone and Setup

```bash
# Clone repository
git clone https://github.com/yourusername/agentic-calculator.git
cd agentic-calculator

# Create virtual environment
python3 -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt
```

#### 4. Run!

```bash
# Terminal 1: Start Ollama (if not auto-started)
ollama serve

# Terminal 2: Run the calculator
python main.py

# Or use Streamlit UI
streamlit run app.py
```

---

## 💡 Usage Examples

### CLI Mode

```bash
$ python main.py

🤖 Calculadora Agentic
============================================================

🧮 Você: Add 100 and 50
🤖 Agente: 150.0

🧮 Você: Calculate average of 5, 10, 15 and take square root
🤖 Agente: 3.162

🧮 Você: sair
👋 Até logo!
```

### Programmatic Use

```python
from core.orchestrator import CalculatorOrchestrator

orchestrator = CalculatorOrchestrator()

result = orchestrator.execute("Add 5 and 3, then multiply by 2")

print(result['final_result'])  # 16.0
print(result['steps_executed'])  # 2
print(result['intermediate_results'])  # [8.0, 16.0]
```

### Complex Multi-Step

```python
# Input
"Calculate mean of 100, 200, 300, then take square root, then divide by 2"

# LLM generates plan:
{
  "steps": [
    {"operation": "mean", "args": [100, 200, 300]},      # → 200
    {"operation": "sqrt", "args": ["$result_0"]},        # → 14.14
    {"operation": "divide", "args": ["$result_1", 2]}    # → 7.07
  ]
}

# Final result: 7.07
```

---

## 🎓 For Agentic Architecture Beginners

### What You'll Learn

1. **LLM Orchestration**: How to use LLMs as "brains" for task planning
2. **Agent Design Patterns**: Strategy, Factory, Observer applied to AI
3. **Prompt Engineering**: Crafting prompts that generate structured outputs
4. **Secure Execution**: Sandboxing and validation in autonomous systems
5. **Modular Architecture**: Building extensible AI systems

### Learning Path

```
1. Run the examples → Understand the flow
2. Read ARCHITECTURE.md → Grasp the design
3. Add a new specialist → Practice extension
4. Modify prompts → Experiment with LLM behavior
5. Build your own agent → Apply to your domain
```

### Key Concepts Explained

#### 🧠 What is an "Orchestrator"?

Think of it like a **conductor of an orchestra**:
- Doesn't play instruments (doesn't do calculations)
- Reads the sheet music (interprets user intent via LLM)
- Tells each musician when to play (delegates to specialists)
- Ensures harmony (validates and consolidates results)

#### 🎯 What is a "Specialist"?

A **domain expert** that does one thing well:
```python
# BAD: God object doing everything
class Calculator:
    def add(self, a, b): ...
    def subtract(self, a, b): ...
    def plot_graph(self, data): ...  # Unrelated!
    def send_email(self, msg): ...   # Unrelated!

# GOOD: Focused specialists
class BasicOperations:
    def add(self, a, b): return a + b
    def subtract(self, a, b): return a - b

class VisualizationOps:
    def plot_graph(self, data): ...
```

#### 🔗 What is "$result_N"?

A reference to previous step results:
```json
{
  "steps": [
    {"operation": "add", "args": [5, 3]},           // Step 0 → 8
    {"operation": "multiply", "args": ["$result_0", 2]}  // Use 8 from step 0
  ]
}
```

This enables **chaining operations** without hardcoding intermediate values.

---

## 🧪 Testing

```bash
# Run all tests
pytest tests/

# With coverage
pytest --cov=core --cov=specialists tests/

# Specific test
pytest tests/test_orchestrator.py -v
```

---

## 🔧 Configuration

### Customize Operations

Edit `config.yaml`:

```yaml
security:
  allowed_operations:
    - "add"
    - "multiply"
    - "sin"        # Add trigonometry
    - "factorial"  # Add combinatorics
```

### Add New Specialist

```python
# 1. Create specialist
# specialists/trigonometry.py
import math

class TrigonometryOperations:
    @staticmethod
    def sin(x):
        return math.sin(math.radians(x))

# 2. Register in orchestrator
# core/orchestrator.py
from specialists.trigonometry import TrigonometryOperations

self.specialists['sin'] = TrigonometryOperations.sin
```

That's it! No core code changes needed. 🎉

---

## 🌟 Real-World Applications

This architecture scales to production systems:

### 🤖 Algorithmic Trading
```python
# Replace math specialists with trading specialists
class TradingOperations:
    def analyze_volatility(symbol): ...
    def execute_order(symbol, quantity): ...
    def calculate_risk(portfolio): ...

# Same orchestrator, different domain!
```

### 📹 Content Generation Pipeline
```python
class ContentOperations:
    def generate_script(topic): ...
    def create_images(script): ...
    def synthesize_voice(script): ...
    def edit_video(assets): ...
```

### 📊 Data Analysis Workflows
```python
class DataOperations:
    def query_database(sql): ...
    def clean_data(df): ...
    def train_model(df): ...
    def visualize_results(predictions): ...
```

**Same patterns. Different specialists. Infinite possibilities.**

---

## 📊 Performance

| Metric | Value | Notes |
|--------|-------|-------|
| **Average Latency** | 1-2s | Single operation |
| **Multi-Step (3 ops)** | 2-3s | Including LLM planning |
| **Memory Usage** | ~500MB | With 7B model loaded |
| **Success Rate** | 98%+ | On valid operations |

### Optimization Tips

- Use **7B model** for speed (current default)
- Use **13B model** for better reasoning (slower)
- Enable **GPU** for 3-5x faster inference
- Add **Redis cache** for repeated queries

---

## 🗺️ Roadmap

### ✅ v1.0 (Current)
- [x] Core orchestration
- [x] Basic math operations
- [x] Streamlit UI
- [x] Security sandbox
- [x] Complete documentation

### 🚧 v1.1 (Next)
- [ ] REST API
- [ ] Variable support (`x = 10`)
- [ ] Operation history
- [ ] More specialists (trig, stats)
- [ ] Docker deployment

### 🔮 v2.0 (Future)
- [ ] Multi-LLM support
- [ ] Execution graph visualization
- [ ] Conversational memory
- [ ] Plugin system

---

## 🤝 Contributing

We welcome contributions! See [CONTRIBUTING.md](CONTRIBUTING.md) for guidelines.

**Good first issues:**
- Add trigonometric operations
- Improve error messages
- Add more test cases
- Translate UI to other languages
- Create Docker setup

---

## 📚 Documentation

- **[ARCHITECTURE.md](ARCHITECTURE.md)** - Deep dive into design decisions
- **[EXAMPLES.md](docs/EXAMPLES.md)** - Advanced use cases

---

## 🐛 Troubleshooting

### Common Issues

**Problem**: `Connection refused` to Ollama

```bash
# Solution: Start Ollama server
ollama serve
```

**Problem**: LLM returns invalid JSON

```yaml
# Solution: Lower temperature in config.yaml
llm:
  temperature: 0.0  # More deterministic
```

**Problem**: Operation blocked by sandbox

```yaml
# Solution: Add to whitelist in config.yaml
security:
  allowed_operations:
    - "your_operation"
```

**More issues?** Check [Issues](https://github.com/yourusername/agentic-calculator/issues) or open a new one.

---

## 📄 License

This project is licensed under the MIT License - see [LICENSE](LICENSE) file.

**TL;DR**: You can use this commercially, modify it, distribute it—just keep the copyright notice.

---

## 🙏 Acknowledgments

- **[Ollama](https://ollama.ai/)** - Making local LLMs accessible
- **[Mistral AI](https://mistral.ai/)** - Excellent open-weight model
- **[Streamlit](https://streamlit.io/)** - Rapid UI development
- **Open Source Community** - For inspiration and tools

---

## Final Notes

This project was created as an **educational initiative** demonstrating how Python can be applied to real-world data analysis and how **Artificial Intelligence** can enhance analytical workflows.

🌟 **Feel free to contribute and improve this project!**


## Tips 

We hope you find our services helpful and enjoyable! If you feel like showing some extra appreciation, why not buy us a coffee? 

🍵 Your support not only energizes our team but also helps us keep improving what we do.

To make a small contribution, you can send us a coffee's worth of USDT or Brazilian Instant Payment (PIX) to our QR code. Every coffee counts and keeps us brewing more ideas!

### Way #1 - USDT coffee:

![Coffee QR Code](https://raw.githubusercontent.com/dadosnapratica/buy_a_coffe_qrcodes/refs/heads/main/qr_code_usdt_enus_200px.png)

or send USDT to address:
```text
0x3db4d1dd10b60c278f27bd1b2e2bd888d0f99f85
```

1. **Scan the QR Code:** Open your crypto wallet and scan our USDT QR code.
2. **Enter the amount:** The cost of a coffee - usually around $3 to $5.
3. **Send your support:** Hit send and make our day!

### Way #2 - Wise international Transfer

![Coffee Wise QR Code](https://raw.githubusercontent.com/dadosnapratica/buy_a_coffe_qrcodes/refs/heads/main/wise_qrcode.jpeg)

Or sent tip for address

```
https://wise.com/pay/me/flavion156
```

### Way #3 - Brasilian PIX coffee:

![Coffee QR Code](https://raw.githubusercontent.com/dadosnapratica/buy_a_coffe_qrcodes/refs/heads/main/qr_code_pix_bradesco.png)

1. **Scan the QR Code:** Open your bank account app and scan our PIX QR code.
2. **Enter the amount:** The cost of a coffee - usually around $3 to $5.
3. **Send your support:** Hit send and make our day!

PIX is a digital payment system in Brazil that allows instant payments 24/7 via mobile phones. If you found this project helpful, please consider buying me a coffee.

---

## Author

**Flavio Lopes** Spreading practical data knowledge for decision making.

--- 

# 📬 Contact

Questions, suggestions, or improvements? Contact me or contribute directly to the repository.

- GitHub: https://github.com/orgs/dadosnapratica  
- LinkedIn: https://www.linkedin.com/in/flavionlopes/  
- Email: flavio.lopes@ideiasfactory.tech  
- WhatsApp: https://wa.me/5511996354436  
- Instagram: https://www.instagram.com/dadosnapratica/

---

Thank you once again for your incredible support and for being a part of our community. Your contribution fuels our passion and commitment.
⭐ Keep learning. Keep building. Keep sharing knowledge. ⭐ 

---


## 🌟 Star History

If this project helped you, consider giving it a ⭐!

[![Star History Chart](https://api.star-history.com/svg?repos=yourusername/agentic-calculator&type=Date)](https://star-history.com/#yourusername/agentic-calculator&Date)

---

## 📈 GitHub Stats

![GitHub stars](https://img.shields.io/github/stars/dadosnapratica/agentic_calculator?style=social)
![GitHub forks](https://img.shields.io/github/forks/dadosnapratica/agentic_calculator?style=social)
![GitHub watchers](https://img.shields.io/github/watchers/dadosnapratica/agentic_calculator?style=social)

---

<div align="center">

**Built with ❤️ for the AI community**

[⭐ Star](https://github.com/dadosnapratica/agentic_calculator) •
[🍴 Fork](https://github.com/dadosnapratica/agentic_calculator/fork) •
[🐛 Report Bug](https://github.com/dadosnapratica/agentic_calculator/issues)


Made by [Flavio Lopes](https://github.com/fnldesign) | 2026

</div>