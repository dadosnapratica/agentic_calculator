import logging

logger = logging.getLogger(__name__)

class SecurityError(Exception):
    """Erro de segurança"""
    pass

class Sandbox:
    """Sandbox para execução segura de operações"""
    
    def __init__(self, config):
        self.max_execution_time = config.get('max_execution_time', 30)
        self.allowed_operations = set(config.get('allowed_operations', []))
        self.enabled = config.get('sandbox_enabled', True)
    
    def validate_operation(self, operation):
        """Valida se operação é permitida"""
        if not self.enabled:
            return True
        
        if operation not in self.allowed_operations:
            logger.warning(f"Operação bloqueada: {operation}")
            raise SecurityError(f"Operação '{operation}' não permitida")
        
        return True
    
    def execute_safe(self, func, *args, **kwargs):
        """Executa função (versão simplificada sem timeout)"""
        # Nota: Implementação completa com timeout requer signal (Unix)
        # Para Windows, usar threading.Timer
        return func(*args, **kwargs)
