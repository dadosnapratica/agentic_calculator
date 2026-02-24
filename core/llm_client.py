import requests
import json
import logging

logger = logging.getLogger(__name__)

class LLMClient:
    """Cliente para interagir com LLM local (Ollama)"""
    
    def __init__(self, config):
        self.endpoint = config['endpoint']
        self.model = config['model']
        self.temperature = config.get('temperature', 0.1)
        self.max_tokens = config.get('max_tokens', 1024)
    
    def generate(self, prompt, system=None):
        """Gera resposta da LLM"""
        if system:
            full_prompt = f"{system}\\n\\n{prompt}"
        else:
            full_prompt = prompt
        
        try:
            response = requests.post(
                f"{self.endpoint}/api/generate",
                json={
                    "model": self.model,
                    "prompt": full_prompt,
                    "stream": False,
                    "options": {
                        "temperature": self.temperature,
                        "num_predict": self.max_tokens
                    }
                },
                timeout=60
            )
            response.raise_for_status()
            result = response.json()
            return result['response'].strip()
        except Exception as e:
            logger.error(f"Erro ao chamar LLM: {e}")
            raise
    
    def plan_operations(self, user_input):
        """Usa LLM para planejar sequência de operações"""
        
        system_prompt = """Você é um assistente que converte pedidos em linguagem natural 
para uma sequência de operações matemáticas.

REGRAS:
1. Retorne APENAS um JSON válido
2. Cada operação deve ter: operation, args, description
3. Operações disponíveis: add, subtract, multiply, divide, sqrt, power, mean, median
4. Use números exatos (não arredonde)
5. A sequência deve ser executável em ordem

EXEMPLO:
Input: "Some 5 e 3, depois multiplique por 2"
Output:
{
  "steps": [
    {"operation": "add", "args": [5, 3], "description": "Somar 5 + 3"},
    {"operation": "multiply", "args": ["$result_0", 2], "description": "Multiplicar resultado anterior por 2"}
  ]
}

Use $result_N para referenciar resultado do step N."""

        prompt = f"Input do usuário: {user_input}\\n\\nJSON de operações:"
        
        try:
            response = self.generate(prompt, system_prompt)
            
            # Extrair JSON (LLM pode adicionar texto extra)
            json_start = response.find('{')
            json_end = response.rfind('}') + 1
            
            if json_start == -1 or json_end == 0:
                raise ValueError("LLM não retornou JSON válido")
            
            json_str = response[json_start:json_end]
            plan = json.loads(json_str)
            
            logger.info(f"Plano gerado: {plan}")
            return plan
            
        except (json.JSONDecodeError, ValueError) as e:
            logger.error(f"Erro ao parsear resposta da LLM: {e}")
            logger.error(f"Resposta recebida: {response}")
            raise ValueError("LLM não conseguiu gerar plano válido")
