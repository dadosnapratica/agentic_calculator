# 🧮 Agentic Calculator

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python 3.9+](https://img.shields.io/badge/python-3.9+-blue.svg)](https://www.python.org/downloads/)
[![Ollama](https://img.shields.io/badge/LLM-Ollama-00A67E?logo=ollama)](https://ollama.ai/)
[![Mistral](https://img.shields.io/badge/Model-Mistral%207B-orange)](https://mistral.ai/)
[![Streamlit](https://img.shields.io/badge/UI-Streamlit-FF4B4B?logo=streamlit)](https://streamlit.io/)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg)](CONTRIBUTING.md)

> **Demonstrando arquitetura multiagente com LLM 100% local.**  
> Construído para desenvolvedores e arquitetos aprendendo a projetar sistemas autônomos de IA.

---

> 🇧🇷 [Versão Original em Português (Brasil)](README_BR.md)  
> **Aviso:** Esta é a versão original da documentação técnica. Para máxima precisão conceitual e técnica, utilize preferencialmente esta versão.

> 🇺🇸 [Versão em Inglês](README.md)  
> **Aviso:** Esta documentação também está disponível em inglês. Para referência técnica oficial, consulte a versão em português ou em inglês.

> 🇪🇸 [Documentación en Español](README_ES.md)  
> **Aviso:** A documentação também está disponível em espanhol. Para maior precisão técnica, consulte a versão original em português ou a versão em inglês.

---


## 🎯 O que é este projeto?

Este projeto não é apenas uma calculadora — é uma implementação de referência completa dos padrões modernos de arquitetura agentic.

Pense nisso como:
- 📚 Um framework educacional para entender a orquestração de agentes de IA
- 🏗️ Uma base pronta para produção para construir sistemas autônomos complexos
- 🔒 Uma alternativa com foco em privacidade aos serviços de IA na nuvem
- 💡 Um roteiro para bots de negociação, pipelines de automação e assistentes inteligentes

### O que o torna "Agentic"?

Programas tradicionais seguem lógica fixa: `se isto, então aquilo`.

Sistemas "agentic" usam IA para:
1. Entender intenção em linguagem natural
2. Planejar a decomposição de tarefas em múltiplos passos
3. Orquestrar agentes especializados
4. Executar com segurança e validação
5. Aprender com feedback (melhoria futura)

```
Usuário: "Calcule a média de 10, 20, 30 e então eleve ao quadrado"

Código Tradicional:        Sistema Agentic:
❌ Precisa de função       ✅ O LLM entende a intenção
  explícita para isso     ✅ Planeja: [mean() → square()]
❌ Falha com variações     ✅ Se adapta à linguagem natural
❌ Sem capacidade de       ✅ Gera um plano de execução
  raciocínio
```

---

### ✨ Principais Funcionalidades
Input:  "Some 15 e 25, então multiplique por 2"
Output: 80.0

# Nos bastidores:
# LLM converte → [add(15,25), multiply($result_0, 2)]
```

### 🎯 Orquestração Multiagente
```python
# Especialistas cuidam de domínios específicos
BasicOperations     → +, -, ×, ÷
AdvancedOperations  → √, ^, log
StatisticsOps       → mean, median, σ
```

### 🔒 Execução Segura em Sandbox
```yaml
# Segurança baseada em whitelist
allowed_operations:
  - add
  - multiply
  # ❌ system_call - BLOQUEADO
  # ❌ file_delete - BLOQUEADO
```

### 📊 UI Moderna com Streamlit
- **Interface Web**: Bonita, responsiva, em tempo real
- **Modo CLI**: Para automação e scripts
- **Pronta para API**: Fácil extensão para endpoints REST

---

## 🏗️ Visão Geral da Arquitetura

### Fluxo de Alto Nível

```
┌─────────────────────────────────────────────┐
│ Entrada do Usuário (Linguagem Natural)     │
│ "Calcule a média de 10,20,30 e eleve ao quadrado" │
└──────────────────┬──────────────────────────┘
                   │
                   ▼
┌─────────────────────────────────────────────┐
│         Orquestrador (Cérebro)              │
│ • Recebe a entrada                           │
│ • Chama o LLM para gerar o plano             │
│ • Valida segurança                           │
│ • Delegar para especialistas                 │
└──────────────┬──────────────────────────────┘
               │
    ┌──────────┼──────────┐
    ▼          ▼          ▼
┌────────┐ ┌────────┐ ┌────────┐
│Operações│ │Operações│ │Operações│
│Básicas  │ │Avançadas│ │Estatísticas│
└────────┘ └────────┘ └────────┘
               │
               ▼
        ┌─────────────┐
        │ LLM (Local) │
        │   Mistral   │
        └─────────────┘
```

### Por que esta arquitetura?

| Padrão | Benefício | Exemplo |
|--------|----------:|--------|
| **Separação de Responsabilidades** | Cada componente tem uma função | Orquestrador coordena, Especialistas executam |
| **Princípio Open/Closed** | Estende sem modificar o núcleo | Adicionar especialista = poucas linhas de código |
| **Injeção de Dependência** | Testável e flexível | Mock do LLM em testes unitários |
| **Design Fail-Safe** | Tratamento de erro gracioso | Operação inválida? Sistema registra e continua |

**📖 Para aprofundar, veja [ARCHITECTURE.md](ARCHITECTURE.md)**

---

## 🚀 Início Rápido (5 Minutos)

### Pré-requisitos

- **Python 3.9+**
- **8GB RAM** (16GB recomendado)
- **5GB de espaço em disco** (para o modelo LLM)

### Instalação

#### 1. Instalar o Ollama (Servidor LLM)

```bash
# macOS / Linux
curl -fsSL https://ollama.ai/install.sh | sh

# Windows
# Baixe em https://ollama.ai/download
```

#### 2. Baixar o Modelo

```bash
ollama pull mistral:7b-instruct
```

#### 3. Clonar e Configurar

```bash
# Clonar repositório
git clone https://github.com/yourusername/agentic-calculator.git
cd agentic-calculator

# Criar ambiente virtual
python3 -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate

# Instalar dependências
pip install -r requirements.txt
```

#### 4. Executar!

```bash
# Terminal 1: Iniciar Ollama (se não iniciar automaticamente)
ollama serve

# Terminal 2: Rodar a calculadora
python main.py

# Ou usar a UI Streamlit
streamlit run app.py
```

---

## 💡 Exemplos de Uso

### Modo CLI

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

### Modo Programático

```python
from core.orchestrator import CalculatorOrchestrator

orchestrator = CalculatorOrchestrator()

result = orchestrator.execute("Add 5 and 3, then multiply by 2")

print(result['final_result'])  # 16.0
print(result['steps_executed'])  # 2
print(result['intermediate_results'])  # [8.0, 16.0]
```

### Multi-etapa Complexo

```python
# Entrada
"Calculate mean of 100, 200, 300, then take square root, then divide by 2"

# LLM gera o plano:
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

## 🎓 Para Iniciantes em Arquitetura Agentic

### O que você vai aprender

1. **Orquestração com LLMs**: Como usar LLMs como "cérebros" para planejamento de tarefas
2. **Padrões de Projeto para Agentes**: Strategy, Factory, Observer aplicados à IA
3. **Prompt Engineering**: Como criar prompts que gerem saídas estruturadas
4. **Execução Segura**: Sandbox e validação em sistemas autônomos
5. **Arquitetura Modular**: Construir sistemas extensíveis de IA

### Caminho de Aprendizado

```
1. Execute os exemplos → Entenda o fluxo
2. Leia ARCHITECTURE.md → Compreenda o design
3. Adicione um novo especialista → Pratique a extensão
4. Modifique prompts → Experimente o comportamento do LLM
5. Construa seu próprio agente → Aplique ao seu domínio
```

### Conceitos-chave Explicados

#### 🧠 O que é um "Orquestrador"?

Pense nele como um **maestro de uma orquestra**:
- Não toca instrumentos (não faz cálculos)
- Lê a partitura (interpreta a intenção do usuário via LLM)
- Diz a cada músico quando tocar (delegar para especialistas)
- Garante harmonia (valida e consolida resultados)

#### 🎯 O que é um "Especialista"?

Um **especialista de domínio** que faz bem uma coisa:
```python
# RUIM: Objeto "Deus" fazendo tudo
class Calculator:
    def add(self, a, b): ...
    def subtract(self, a, b): ...
    def plot_graph(self, data): ...  # Não relacionado!
    def send_email(self, msg): ...   # Não relacionado!

# BOM: Especialistas focados
class BasicOperations:
    def add(self, a, b): return a + b
    def subtract(self, a, b): return a - b

class VisualizationOps:
    def plot_graph(self, data): ...
```

#### 🔗 O que é "$result_N"?

Uma referência a resultados de passos anteriores:
```json
{
  "steps": [
    {"operation": "add", "args": [5, 3]},           // Passo 0 → 8
    {"operation": "multiply", "args": ["$result_0", 2]}  // Usa 8 do passo 0
  ]
}
```

Isso permite **encadear operações** sem hardcode de valores intermediários.

---

## 🧪 Testes

```bash
# Execute todos os testes
pytest tests/

# Com coverage
pytest --cov=core --cov=specialists tests/

# Teste específico
pytest tests/test_orchestrator.py -v
```

---

## 🔧 Configuração

### Personalizar Operações

Edite `config.yaml`:

```yaml
security:
  allowed_operations:
    - "add"
    - "multiply"
    - "sin"        # Adicionar trigonometria
    - "factorial"  # Adicionar combinatória
```

### Adicionar Novo Especialista

```python
# 1. Criar especialista
# specialists/trigonometry.py
import math

class TrigonometryOperations:
    @staticmethod
    def sin(x):
        return math.sin(math.radians(x))

# 2. Registrar no orquestrador
# core/orchestrator.py
from specialists.trigonometry import TrigonometryOperations

self.specialists['sin'] = TrigonometryOperations.sin
```

Pronto! Nenhuma alteração no código núcleo necessária. 🎉

---

## 🌟 Aplicações no Mundo Real

Esta arquitetura escala para sistemas de produção:

### 🤖 Trading Algorítmico
```python
# Substitua especialistas matemáticos por especialistas de trading
class TradingOperations:
    def analyze_volatility(symbol): ...
    def execute_order(symbol, quantity): ...
    def calculate_risk(portfolio): ...

# Mesmo orquestrador, domínio diferente!
```

### 📹 Pipeline de Geração de Conteúdo
```python
class ContentOperations:
    def generate_script(topic): ...
    def create_images(script): ...
    def synthesize_voice(script): ...
    def edit_video(assets): ...
```

### 📊 Workflows de Análise de Dados
```python
class DataOperations:
    def query_database(sql): ...
    def clean_data(df): ...
    def train_model(df): ...
    def visualize_results(predictions): ...
```

**Mesmos padrões. Diferentes especialistas. Possibilidades infinitas.**

---

## 📊 Performance

| Métrica | Valor | Observações |
|--------|-------|-------------|
| **Latência média** | 1-2s | Operação única |
| **Multi-etapa (3 ops)** | 2-3s | Inclui planejamento do LLM |
| **Uso de memória** | ~500MB | Com modelo 7B carregado |
| **Taxa de sucesso** | 98%+ | Em operações válidas |

### Dicas de Otimização

- Use **modelo 7B** para velocidade (default atual)
- Use **modelo 13B** para melhor raciocínio (mais lento)
- Ative **GPU** para inferência 3-5x mais rápida
- Adicione **cache Redis** para consultas repetidas

---

## 🗺️ Roadmap

### ✅ v1.0 (Atual)
- [x] Orquestração core
- [x] Operações matemáticas básicas
- [x] UI em Streamlit
- [x] Sandbox de segurança
- [x] Documentação completa

### 🚧 v1.1 (Próximo)
- [ ] REST API
- [ ] Suporte a variáveis (`x = 10`)
- [ ] Histórico de operações
- [ ] Mais especialistas (trig, stats)
- [ ] Deploy com Docker

### 🔮 v2.0 (Futuro)
- [ ] Suporte a múltiplos LLMs
- [ ] Visualização do grafo de execução
- [ ] Memória conversacional
- [ ] Sistema de plugins

---

## 🤝 Contribuindo

Contribuições são bem-vindas! Veja [CONTRIBUTING.md](CONTRIBUTING.md) para orientações.

**Bons primeiros problemas:**
- Adicionar operações trigonométricas
- Melhorar mensagens de erro
- Adicionar mais casos de teste
- Traduzir a UI para outros idiomas
- Criar setup Docker

---

## 📚 Documentação

- **[ARCHITECTURE.md](ARCHITECTURE.md)** - Mergulho profundo nas decisões de design
- **[EXAMPLES.md](docs/EXAMPLES.md)** - Casos de uso avançados

---

## 🐛 Solução de Problemas

### Problemas Comuns

**Problema**: `Connection refused` ao Ollama

```bash
# Solução: Inicie o servidor Ollama
ollama serve
```

**Problema**: LLM retorna JSON inválido

```yaml
# Solução: Reduza a temperatura em config.yaml
llm:
  temperature: 0.0  # Mais determinístico
```

**Problema**: Operação bloqueada pelo sandbox

```yaml
# Solução: Adicione à whitelist em config.yaml
security:
  allowed_operations:
    - "your_operation"
```

**Mais problemas?** Veja [Issues](https://github.com/yourusername/agentic-calculator/issues) ou abra uma nova.

---

## 📄 Licença

Este projeto está licenciado sob a Licença MIT - veja o arquivo [LICENSE](LICENSE).

**Resumo**: Você pode usar comercialmente, modificar e distribuir — apenas mantenha o aviso de copyright.

---

## 🙏 Agradecimentos

- **[Ollama](https://ollama.ai/)** - Tornando LLMs locais acessíveis
- **[Mistral AI](https://mistral.ai/)** - Excelente modelo de pesos abertos
- **[Streamlit](https://streamlit.io/)** - Desenvolvimento rápido de UI
- **Comunidade Open Source** - Pela inspiração e ferramentas

---

## Notas Finais

Este projeto foi criado como uma **iniciativa educacional** demonstrando como Python pode ser aplicado à análise de dados do mundo real e como a **Inteligência Artificial** pode aprimorar fluxos analíticos.

🌟 **Sinta-se à vontade para contribuir e melhorar este projeto!**


## Dicas

Esperamos que nossos serviços sejam úteis e agradáveis! Se quiser demonstrar um pouco de apreço, que tal comprar-nos um café?

🍵 Seu apoio não só energiza a equipe como também nos ajuda a continuar melhorando.

Para uma pequena contribuição, você pode enviar USDT ou um pagamento instantâneo PIX para o nosso QR code. Cada cafezinho conta!

### Forma #1 - Café em USDT:

![Coffee QR Code](https://raw.githubusercontent.com/dadosnapratica/buy_a_coffe_qrcodes/refs/heads/main/qr_code_usdt_enus_200px.png)

ou envie USDT para o endereço:
```text
0x3db4d1dd10b60c278f27bd1b2e2bd888d0f99f85
```

1. **Escaneie o QR Code:** Abra sua carteira cripto e escaneie o QR code de USDT.
2. **Digite o valor:** O preço de um café — geralmente entre $3 e $5.
3. **Envie seu apoio:** Confirme o envio e nos faça felizes!

### Forma #2 - Transferência internacional via Wise

![Coffee Wise QR Code](https://raw.githubusercontent.com/dadosnapratica/buy_a_coffe_qrcodes/refs/heads/main/wise_qrcode.jpeg)

Ou envie pela URL

```
https://wise.com/pay/me/flavion156
```

### Forma #3 - Café via PIX (Brasil):

![Coffee QR Code](https://raw.githubusercontent.com/dadosnapratica/buy_a_coffe_qrcodes/refs/heads/main/qr_code_pix_bradesco.png)

1. **Escaneie o QR Code:** Abra o app do seu banco e escaneie o QR code PIX.
2. **Digite o valor:** Entre R$3 e R$25 (ou o que preferir).
3. **Envie seu apoio:** Confirme o pagamento e obrigado!

PIX é um sistema de pagamentos instantâneos no Brasil disponível 24/7. Se este projeto foi útil, considere comprar-me um café.

---

## Autor

**Flavio Lopes** — Compartilhando conhecimento prático de dados para apoio à tomada de decisão.

--- 

# 📬 Contato

Dúvidas, sugestões ou melhorias? Entre em contato ou contribua diretamente no repositório.

- GitHub: https://github.com/orgs/dadosnapratica  
- LinkedIn: https://www.linkedin.com/in/flavionlopes/  
- Email: flavio.lopes@ideiasfactory.tech  
- WhatsApp: https://wa.me/5511996354436  
- Instagram: https://www.instagram.com/dadosnapratica/

---

Obrigado mais uma vez pelo apoio incrível e por fazer parte da nossa comunidade. Sua contribuição alimenta nossa paixão e compromisso.
⭐ Continue aprendendo. Continue construindo. Continue compartilhando conhecimento. ⭐ 

---


## 🌟 Histórico de Stars

Se este projeto te ajudou, considere dar um ⭐!

[![Gráfico de Star History](https://api.star-history.com/svg?repos=yourusername/agentic-calculator&type=Date)](https://star-history.com/#yourusername/agentic-calculator&Date)

---

## 📈 Estatísticas do GitHub

![GitHub stars](https://img.shields.io/github/stars/dadosnapratica/agentic_calculator?style=social)
![GitHub forks](https://img.shields.io/github/forks/dadosnapratica/agentic_calculator?style=social)
![GitHub watchers](https://img.shields.io/github/watchers/dadosnapratica/agentic_calculator?style=social)

---

<div align="center">

**Construído com ❤️ para a comunidade de IA**

[⭐ Star](https://github.com/dadosnapratica/agentic_calculator) •
[🍴 Fork](https://github.com/dadosnapratica/agentic_calculator/fork) •
[🐛 Reportar Bug](https://github.com/dadosnapratica/agentic_calculator/issues)


Feito por [Flavio Lopes](https://github.com/fnldesign) | 2026

</div>