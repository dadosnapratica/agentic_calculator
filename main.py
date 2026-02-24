import logging
import sys
from pathlib import Path

from core.orchestrator import CalculatorOrchestrator

# Setup logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('logs/agent.log'),
        logging.StreamHandler(sys.stdout)
    ]
)

def main():
    """Entry point"""
    
    # Criar diretórios necessários
    Path('logs').mkdir(exist_ok=True)
    
    # Inicializar orchestrator
    print("🤖 Iniciando Calculadora Agentic...")
    print("=" * 60)
    
    orchestrator = CalculatorOrchestrator()
    
    # Exemplos de teste
    test_cases = [
        "Some 15 e 25",
        "Multiplique 7 por 8",
        "Calcule a média de 10, 20, 30 e 40",
        "Some 5 e 3, depois multiplique por 2",
        "Calcule a raiz quadrada de 144",
        "Eleve 2 à potência de 8",
    ]
    
    print("\\n📋 Executando casos de teste...\\n")
    
    for i, test in enumerate(test_cases, 1):
        print(f"\\n{'─' * 60}")
        print(f"Teste {i}/{len(test_cases)}")
        print(f"{'─' * 60}")
        
        result = orchestrator.execute(test)
        
        if result['success']:
            print(f"✅ Sucesso!")
            print(f"   Entrada: {result['input']}")
            print(f"   Resultado: {result['final_result']}")
            print(f"   Steps: {result['steps_executed']}")
        else:
            print(f"❌ Falha!")
            print(f"   Erro: {result['error']}")
    
    # Modo interativo
    print(f"\\n{'=' * 60}")
    print("💬 Modo interativo (digite 'sair' para encerrar)")
    print(f"{'=' * 60}\\n")
    
    while True:
        try:
            user_input = input("\\n🧮 Você: ").strip()
            
            if user_input.lower() in ['sair', 'exit', 'quit']:
                print("\\n👋 Até logo!")
                break
            
            if not user_input:
                continue
            
            result = orchestrator.execute(user_input)
            
            if result['success']:
                print(f"\\n🤖 Agente: {result['final_result']}")
            else:
                print(f"\\n❌ Erro: {result['error']}")
                
        except KeyboardInterrupt:
            print("\\n\\n👋 Até logo!")
            break
        except Exception as e:
            print(f"\\n❌ Erro inesperado: {e}")

if __name__ == "__main__":
    main()
