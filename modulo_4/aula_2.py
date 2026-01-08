# Herança e Polimorfismo
# Aula 4.2: Herança e Polimorfismo (Base do LangChain)
# Criando uma classe base genérica (ex: ModeloIA).
# Criando subclasses específicas (OpenAIModel, LlamaModel).
# Por que frameworks de IA usam tanto isso?

## Herança
class ModeloIA:
    def __init__(self, nome: str, temperatura: float):
        self.nome = nome
        self.temperatura = temperatura

    def gerar_resposta(self, prompt: str) -> str:
        resposta = f"A resposta para o prompt {prompt} usando o modelo {self.nome} com temperatura {self.temperatura}"
        return resposta

# Subclasses
class OpenAIModel(ModeloIA):
    def __init__(self, nome: str, temperatura: float):
        super().__init__(nome, temperatura)

    def gerar_resposta_complexa(self, prompt: str) -> str:
        return f"Resposta complexa usando o modelo {self.nome} com temperatura {self.temperatura}"

# Subclasses
class LlamaModel(ModeloIA):
    def __init__(self, nome: str, temperatura: float):
        super().__init__(nome, temperatura)

    def gerar_resposta_complexa(self, prompt: str) -> str:
        return f"Resposta complexa usando o modelo {self.nome} com temperatura {self.temperatura}"

# Exceções personalizadas

class ApiKeyInvalidaError(Exception):
    pass

def gerar_resposta(modelo: ModeloIA, prompt: str) -> str:
    if not modelo.api_key.startswith("sk-"):
        raise ApiKeyInvalidaError("API Key inválida")
    return modelo.gerar_resposta(prompt)