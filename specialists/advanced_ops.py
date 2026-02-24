import math
import logging

logger = logging.getLogger(__name__)

class AdvancedOperations:
    """Especialista em operações avançadas"""
    
    @staticmethod
    def sqrt(x):
        """Raiz quadrada"""
        if x < 0:
            raise ValueError("Raiz quadrada de número negativo")
        result = math.sqrt(x)
        logger.info(f"SQRT: √{x} = {result}")
        return result
    
    @staticmethod
    def power(base, exponent):
        """Potenciação"""
        result = base ** exponent
        logger.info(f"POWER: {base}^{exponent} = {result}")
        return result
