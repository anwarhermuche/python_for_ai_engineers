"""
# PROJETO — FINE-TUNING DATASET PREPPER

## Objetivo:
Criar um pipeline simples de ETL para preparar dados de conversas de suporte
para uso em treinamento de modelos de linguagem.

## Estrutura do projeto:
- main.py            → ponto de entrada e orquestração (esse arquivo)
- etl.py             → classe responsável por extração, limpeza e transformação

## Input:
- Arquivo CSV "sujo" contendo logs de suporte ao cliente (./modulo_6/support_logs_dirty.csv)

## Responsabilidades da classe ETL:
- Carregar o CSV usando pandas
- Limpar e normalizar os dados:
  - padronizar sender para "human" ou "ai"
  - remover linhas inválidas, vazias ou curtas demais (menos de 15 caracteres)
  - Remover PIIs (email, telefone, CPF)
  - limpar conteúdo textual (espaços, quebras de linha, HTML simples)
  - tratar timestamps inválidos
  - remover duplicatas
- Transformar os dados:
  - ordenar mensagens por chat e tempo
  - Agrupar por chat_id e montar exemplos no formato JSONL:
    {"messages":[{"role":"user","content":"..."},{"role":"assistant","content":"..."}]}
  - Apenas exportar pares válidos user→assistant (sem buracos)
- Exportar o resultado final em formato JSONL

## Regras obrigatórias:
- Toda a lógica de ETL deve estar encapsulada em uma classe
- main.py não pode conter regras de limpeza ou transformação
- O pipeline deve ser reutilizável para outros arquivos CSV

## Output:
- Arquivo training_data.jsonl pronto para uso
"""

# Importando o pandas
import pandas as pd
file_path = "./modulo_6/support_logs_dirty.csv"

# Carregando o arquivo CSV
df = pd.read_csv(file_path)
pd.set_option('display.max_columns', None)

# Importando a classe ETL
from etl import ETL
etl = ETL(file_path)

# Executando o pipeline
df = etl.pipeline()

print(df)

