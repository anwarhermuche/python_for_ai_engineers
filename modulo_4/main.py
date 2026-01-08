"""
# PROJETO — MODEL PROVIDER SDK (SIMULADO)

## Objetivo:
Criar uma mini-SDK em Python que simula provedores de modelos de linguagem,
utilizando Programação Orientada a Objetos, herança, polimorfismo e variáveis de ambiente.

## O programa deve:
- Definir uma classe base genérica (ex: ModeloBase)
- Definir subclasses para provedores específicos (ex: OpenAIModel, LlamaModel)
- Cada classe deve:
  - Receber nome do modelo e temperatura no construtor
  - Expor um método comum chamado invoke() com parêmetro 'prompt' e 'api_key''
  - Verificar se api_key começa com "sk-" antes de dar uma resposta
    - Se começar, use o time.sleep() e dê a resposta
    - Se não começar, dê uma resposta de erro "API Key inválida"
- O comportamento deve ser intercambiável via polimorfismo

## Regras obrigatórias:
- A classe base não pode conhecer detalhes das subclasses
- As subclasses devem sobrescrever o método invoke()
- O método invoke() deve:
  - Simular latência usando time.sleep
  - Retornar um dicionário estruturado (ex: {"model": "...", "output": "...", "temperatura": ...})
- O programa deve ler duas variáveis de ambiente fictícias:
  - OPENAI_API_KEY
  - LLAMA_API_KEY
- As variáveis devem ser carregadas via python-dotenv
- O arquivo .env não pode ser versionado
- O main.py deve escolher dinamicamente qual modelo instanciar com base no input do usuário

## Estrutura mínima esperada:
- src/
  - models/
    - base.py
    - openai.py
    - llama.py
  - main.py

## Esse projeto deve retornar:
- A resposta estruturada do método invoke()
"""

# Escolha do modelo
modelo = input("Digite o nome do modelo (gpt ou llama): ")

# Importando classes
from models.openai import OpenAIModel
from models.llama import LlamaModel

# Instanciando o modelo
if modelo == "gpt":
    modelo = OpenAIModel("gpt-4o-mini", 0.5)
elif modelo == "llama":
    modelo = LlamaModel("llama-3.1-8b", 0.5)
else:
    print("Modelo inválido")

# Invocando o modelo
resposta = modelo.invoke("Qual é a temperatura?")
print(resposta)