# Chat Models
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv

# Carregando as variáveis de ambiente
load_dotenv()

# Modelo
modelo = ChatOpenAI(model="gpt-4o-mini", temperature=0, logprobs = True)

## Prompt como string
prompt = "Qual é a capital do Brasil?"

## Resposta
# resposta = modelo.invoke(prompt)
# print(resposta)

## Prompt conversacional
from langchain_core.messages import SystemMessage,HumanMessage, AIMessage

messages = [
    SystemMessage(content="Você é um assistente de IA que responde perguntas sobre o Brasil. Mas só vale resposta errada."),
    HumanMessage(content="Qual é a capital do Brasil?"),
    AIMessage(content="A capital do Brasil é Belo Horizonte."),
    HumanMessage(content="Qual é a capital de São Paulo?")
]

resposta = modelo.invoke(messages)

# Elementos da resposta
print(f"Conteúdo textual: {resposta.content}")
print(f"Uso de tokens: {resposta.response_metadata['token_usage']}")
print(f"Logprobs: {resposta.response_metadata['logprobs']['content']}")

# ADICIONAL: perplexidade
import numpy as np
logprobs = [token['logprob'] for token in resposta.response_metadata['logprobs']['content']]
perplexity = np.exp(-np.mean(logprobs))
print(f"Perplexidade: {perplexity}")