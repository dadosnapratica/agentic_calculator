import statistics
import logging

logger = logging.getLogger(__name__)

class StatisticsOperations:
    """Especialista em estatística"""
    
    @staticmethod
    def mean(*args):
        """Média aritmética"""
        if len(args) == 0:
            raise ValueError("Precisa de pelo menos 1 número")
        result = statistics.mean(args)
        logger.info(f"MEAN: mean({args}) = {result}")
        return result
    
    @staticmethod
    def median(*args):
        """Mediana"""
        if len(args) == 0:
            raise ValueError("Precisa de pelo menos 1 número")
        result = statistics.median(args)
        logger.info(f"MEDIAN: median({args}) = {result}")
        return result
