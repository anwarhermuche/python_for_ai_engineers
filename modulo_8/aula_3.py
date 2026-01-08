# Saídas Estruturadas
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from pydantic import BaseModel, Field
from datetime import datetime
from typing import Literal

# Carregando as variáveis de ambiente
load_dotenv()

# Classe da Saída Estruturada
class Resposta(BaseModel):
    nome: str = Field(description="O nome da pessoa")
    data: datetime = Field(description = "A data e hora do e-mail enviado pela pessoa")
    intencao: Literal["comercial", "suporte", "outros"] = Field(description = "A intenção do e-mail: comercial, suporte ou outros")

# Modelo de IA
modelo = ChatOpenAI(model="gpt-4o-mini", temperature=0)
modelo_estruturado = modelo.with_structured_output(Resposta)

# E-mail
email = """
enviado por fernandoalonso@gmail.com em 2026-01-08 às 10 da manhã.

Falaa, meu amigo! Tudo bom?

Cara, deixa eu te falar. Bora fazer um churrasco no final de semana?

Abração!
"""

# Resposta
resposta = modelo_estruturado.invoke(email)

## Exibindo os campos
print(f"Nome: {resposta.nome}")
print(f"Data: {resposta.data}")
print(f"Intenção: {resposta.intencao}")