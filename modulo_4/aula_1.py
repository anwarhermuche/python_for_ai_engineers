# Introdução à POO (Programação Orientada a Objetos)

## Classes vs Objetos
## Classe é o molde do objeto
## Objeto é a instância da classe

## Criando uma classe
class ModeloIA:
    def __init__(self, nome: str, temperatura: float):
        self.nome = nome
        self.temperatura = temperatura

    def gerar_resposta(self, prompt: str) -> str:
        resposta = f"A resposta para o prompt {prompt} usando o modelo {self.nome} com temperatura {self.temperatura}"
        return resposta

## Criando um objeto
modelo = ModeloIA("gpt-5.1", 0.5)
resposta = modelo.gerar_resposta("Qual é a temperatura?")
print(resposta)