"""
# PROJETO — TOKEN COST CALCULATOR

## Objetivo:
Criar uma mini-biblioteca em Python para estimar custo mensal de uso de modelos de linguagem,
seguindo padrões profissionais de projeto (Poetry, modularização e tipagem).

## O programa deve:
- Receber do usuário:
  - nome do modelo (ex: "gpt-4", "claude-3-opus")
  - tokens no system prompt
  - média de tokens de input
  - média de tokens de output
  - média de mensagens por dia
- Calcular o custo mensal com base em uma tabela de preços definida no código
- Exibir o resultado de forma clara no terminal
- Registrar cada cálculo em um arquivo de log (.txt)

## Regras obrigatórias:
- Os preços dos modelos devem ser armazenados em um dicionário
- A lógica de cálculo deve estar isolada em funções tipadas
- A janela de contexto deve ser considerada
- O módulo de cálculo não pode conter input() nem print()
- O main.py deve apenas orquestrar entradas, saídas e chamadas de função
- Cada execução deve registrar:
  - modelo
  - tokens informados
  - custo calculado
- O log deve ser escrito utilizando context manager (with open)

## Estrutura mínima esperada:
- modulo_3/
  - calculadora.py
  - main.py

## Esse projeto deve retornar:
- custo total estimado (float)
"""

# Recebendo os inputs do usuário
modelo = input("Digite o nome do modelo: ")
tokens_system_prompt = int(input("Digite a quantidade de tokens no system prompt: "))
media_tokens_input = int(input("Digite a média de tokens de input: "))
media_tokens_output = int(input("Digite a média de tokens de output: "))
media_mensagens_por_dia = int(input("Digite a média de mensagens por dia: "))

# Calculando o custo mensal
from calculadora import calcular_custo_total
custo_mensal = calcular_custo_total(modelo, tokens_system_prompt, media_tokens_input, media_tokens_output, media_mensagens_por_dia)

# Exibindo o resultado
print(f"O custo mensal é de {custo_mensal} dólares")