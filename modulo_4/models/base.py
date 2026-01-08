class ModeloBase:

    def __init__(self, nome: str, temperatura: float):
        self.nome = nome
        self.temperatura = temperatura

    def invoke(self, prompt: str, api_key: str) -> str:
        raise NotImplementedError("Subclasses devem implementar este método")