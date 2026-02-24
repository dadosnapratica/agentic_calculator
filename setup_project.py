"""
Script de setup automático para a PoC
Executa: python setup_project.py
"""

import os
from pathlib import Path

PROJECT_FILES = {
    "config.yaml": """llm:
  provider: "ollama"
  endpoint: "http://localhost:11434"
  model: "mistral:7b-instruct"
  temperature: 0.1
  max_tokens: 1024

security:
  max_execution_time: 30
  allowed_operations:
    - "add"
    - "subtract"
    - "multiply"
    - "divide"
    - "sqrt"
    - "power"
    - "mean"
    - "median"
  sandbox_enabled: true

logging:
  level: "INFO"
  file: "logs/agent.log"
""",
    
    "requirements.txt": """pyyaml>=6.0
requests>=2.31.0
streamlit>=1.30.0
""",
    
    "README.md": """# 🧮 Calculadora Agentic - PoC

## Setup Rápido
```bash
# 1. Instalar Ollama
curl -fsSL https://ollama.ai/install.sh | sh
ollama pull mistral:7b-instruct

# 2. Instalar dependências
pip install -r requirements.txt

# 3. Executar CLI
python main.py

# 4. Executar UI
streamlit run app.py
```

## Exemplos
