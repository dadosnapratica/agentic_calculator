import streamlit as st
import logging
from pathlib import Path

from core.orchestrator import CalculatorOrchestrator

# Setup
Path('logs').mkdir(exist_ok=True)
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[logging.FileHandler('logs/agent.log')]
)

st.set_page_config(
    page_title="Calculadora Agentic",
    page_icon="🧮",
    layout="wide"
)

# CSS customizado
st.markdown("""
<style>
    .main-header {
        font-size: 3rem;
        font-weight: bold;
        text-align: center;
        margin-bottom: 0;
    }
    .sub-header {
        text-align: center;
        color: #666;
        margin-top: 0;
    }
    .stButton>button {
        width: 100%;
    }
</style>
""", unsafe_allow_html=True)

# Título
st.markdown('<p class="main-header">🧮 Calculadora Agentic</p>', unsafe_allow_html=True)
st.markdown('<p class="sub-header">Powered by LLM Local + Multi-Agent System</p>', unsafe_allow_html=True)

# Inicializar orchestrator (cache)
@st.cache_resource
def get_orchestrator():
    return CalculatorOrchestrator()

try:
    orchestrator = get_orchestrator()
except Exception as e:
    st.error(f"❌ Erro ao inicializar: {e}")
    st.info("Verifique se o Ollama está rodando: `ollama serve`")
    st.stop()

# Sidebar com exemplos
with st.sidebar:
    st.header("📋 Exemplos")
    st.markdown("Clique para usar:")
    
    examples = [
        "Some 15 e 25",
        "Multiplique 7 por 8",
        "Calcule a média de 10, 20, 30",
        "Some 5 e 3, depois multiplique por 2",
        "Raiz quadrada de 144",
        "2 elevado a 8",
        "Média de 100, 200, 300 e tire a raiz quadrada",
    ]
    
    for ex in examples:
        if st.button(ex, key=ex, use_container_width=True):
            st.session_state.user_input = ex
    
    st.markdown("---")
    st.markdown("### ℹ️ Sobre")
    st.markdown("""
    **Arquitetura:**
    - LLM: Mistral 7B (local)
    - Orchestrator: Python
    - Specialists: Módulos dedicados
    
    **Features:**
    - ✅ Planejamento multi-step
    - ✅ Execução segura
    - ✅ Logging completo
    """)

# Input principal
st.markdown("### 💬 Digite seu cálculo")

user_input = st.text_input(
    "Em linguagem natural:",
    value=st.session_state.get('user_input', ''),
    placeholder="Ex: Some 10 e 20, depois multiplique por 3",
    label_visibility="collapsed"
)

col1, col2, col3 = st.columns([3, 1, 1])

with col1:
    calculate_btn = st.button("🚀 Calcular", type="primary", use_container_width=True)

with col2:
    clear_btn = st.button("🗑️ Limpar", use_container_width=True)

with col3:
    if st.button("📊 Logs", use_container_width=True):
        st.session_state.show_logs = not st.session_state.get('show_logs', False)

if clear_btn:
    st.session_state.user_input = ''
    st.rerun()

# Processar
if calculate_btn and user_input:
    with st.spinner("🧠 Processando com LLM..."):
        result = orchestrator.execute(user_input)
    
    if result['success']:
        # Resultado principal
        st.success(f"### ✅ Resultado: `{result['final_result']}`")
        
        # Métricas
        col1, col2, col3 = st.columns(3)
        with col1:
            st.metric("Steps Executados", result['steps_executed'])
        with col2:
            st.metric("Operações", len(result['plan'].get('steps', [])))
        with col3:
            st.metric("Status", "✅ Sucesso")
        
        # Detalhes expansíveis
        with st.expander("🔍 Ver Detalhes da Execução"):
            st.markdown("**Plano Gerado pela LLM:**")
            st.json(result['plan'])
            
            if len(result['intermediate_results']) > 1:
                st.markdown("**Resultados Intermediários:**")
                for i, r in enumerate(result['intermediate_results']):
                    st.code(f"Step {i}: {r}", language="python")
    else:
        st.error(f"❌ Erro: {result['error']}")
        
        with st.expander("🔍 Ver Detalhes do Erro"):
            st.code(str(result), language="json")

# Logs (se ativado)
if st.session_state.get('show_logs', False):
    st.markdown("---")
    st.markdown("### 📜 Logs Recentes")
    
    try:
        with open('logs/agent.log', 'r') as f:
            logs = f.readlines()[-50:]  # Últimas 50 linhas
        
        st.code(''.join(logs), language="log")
    except FileNotFoundError:
        st.info("Nenhum log disponível ainda")

# Footer
st.markdown("---")
st.caption("🤖 PoC: Agentic Layer | Flavio Lopes | 2026")
