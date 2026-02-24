import logging

logger = logging.getLogger(__name__)

class BasicOperations:
    """Especialista em operações básicas (+, -, *, /)"""
    
    @staticmethod
    def add(*args):
        """Soma N números"""
        result = sum(args)
        logger.info(f"ADD: {' + '.join(map(str, args))} = {result}")
        return result
    
    @staticmethod
    def subtract(a, b):
        """Subtrai b de a"""
        result = a - b
        logger.info(f"SUBTRACT: {a} - {b} = {result}")
        return result
    
    @staticmethod
    def multiply(*args):
        """Multiplica N números"""
        result = 1
        for num in args:
            result *= num
        logger.info(f"MULTIPLY: {' * '.join(map(str, args))} = {result}")
        return result
    
    @staticmethod
    def divide(a, b):
        """Divide a por b"""
        if b == 0:
            raise ValueError("Divisão por zero não permitida")
        result = a / b
        logger.info(f"DIVIDE: {a} / {b} = {result}")
        return result
