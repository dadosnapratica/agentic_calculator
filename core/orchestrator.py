import logging
import yaml
from pathlib import Path

from core.llm_client import LLMClient
from core.security import Sandbox, SecurityError
from specialists.basic_ops import BasicOperations
from specialists.advanced_ops import AdvancedOperations
from specialists.stats_ops import StatisticsOperations

logger = logging.getLogger(__name__)

class CalculatorOrchestrator:
    """
    Agente orquestrador que:
    1. Recebe linguagem natural
    2. Consulta LLM para planejar
    3. Delega para specialists
    4. Consolida resultado
    """
    
    def __init__(self, config_path="config.yaml"):
        # Carregar config
        with open(config_path) as f:
            self.config = yaml.safe_load(f)
        
        # Inicializar componentes
        self.llm = LLMClient(self.config['llm'])
        self.sandbox = Sandbox(self.config['security'])
        
        # Registrar specialists
        self.specialists = {
            # Basic
            'add': BasicOperations.add,
            'subtract': BasicOperations.subtract,
            'multiply': BasicOperations.multiply,
            'divide': BasicOperations.divide,
            
            # Advanced
            'sqrt': AdvancedOperations.sqrt,
            'power': AdvancedOperations.power,
            
            # Statistics
            'mean': StatisticsOperations.mean,
            'median': StatisticsOperations.median,
        }
        
        logger.info("Orchestrator inicializado com sucesso")
    
    def execute(self, user_input):
        """Pipeline principal"""
        logger.info(f"📥 Input: {user_input}")
        
        try:
            # FASE 1: Planning
            logger.info("🧠 Planejando com LLM...")
            plan = self.llm.plan_operations(user_input)
            
            if 'steps' not in plan:
                raise ValueError("Plano inválido: sem campo 'steps'")
            
            # FASE 2: Execution
            logger.info(f"⚙️  Executando {len(plan['steps'])} operações...")
            results = self._execute_plan(plan['steps'])
            
            # FASE 3: Consolidation
            logger.info("📊 Consolidando resultado...")
            final_result = results[-1] if results else None
            
            summary = {
                'success': True,
                'input': user_input,
                'plan': plan,
                'steps_executed': len(results),
                'intermediate_results': results,
                'final_result': final_result
            }
            
            logger.info(f"✅ Resultado final: {final_result}")
            return summary
            
        except Exception as e:
            logger.error(f"❌ Erro: {e}", exc_info=True)
            return {
                'success': False,
                'input': user_input,
                'error': str(e)
            }
    
    def _execute_plan(self, steps):
        """Executa sequência de operações"""
        results = []
        
        for i, step in enumerate(steps):
            operation = step['operation']
            args = step['args']
            description = step.get('description', '')
            
            logger.info(f"  Step {i}: {description}")
            
            # Validar segurança
            self.sandbox.validate_operation(operation)
            
            # Resolver referências a resultados anteriores
            resolved_args = self._resolve_args(args, results)
            
            # Obter specialist
            if operation not in self.specialists:
                raise ValueError(f"Operação desconhecida: {operation}")
            
            specialist_func = self.specialists[operation]
            
            # Executar com sandbox
            try:
                result = self.sandbox.execute_safe(
                    specialist_func,
                    *resolved_args
                )
                results.append(result)
                logger.info(f"    → Resultado: {result}")
                
            except Exception as e:
                logger.error(f"Erro no step {i}: {e}")
                raise
        
        return results
    
    def _resolve_args(self, args, results):
        """Resolve referências como $result_0, $result_1"""
        resolved = []
        
        for arg in args:
            if isinstance(arg, str) and arg.startswith('$result_'):
                idx = int(arg.split('_')[1])
                if idx >= len(results):
                    raise ValueError(f"Referência inválida: {arg}")
                resolved.append(results[idx])
            else:
                resolved.append(arg)
        
        return resolved
