# Limpeza de Dados
import pandas as pd

## Tratando valores nulos
## Carregando o dataframe
df = pd.read_csv("./modulo_6/messages.csv")

## Total e percentual de valores nulos por coluna
print("Total de valores nulos por coluna:", df.isnull().sum())
print("Percentual de valores nulos por coluna:", df.isnull().mean())

## Preenchendo valores nulos de uma coluna específica
df[["input_tokens", "output_tokens"]] = df[["input_tokens", "output_tokens"]].fillna(0)
print(df.head())

# Deduplicação de dados
## Removendo duplicatas com base em todas as colunas
df = df.drop_duplicates()
print(df.head())

## Removendo duplicatas com base de uma coluna específica
df = df.drop_duplicates(subset=["content"])
print(df.head())

## Filtragem de dados
## Apenas onde 'sender' == 'human'
df = df[df["sender"] == "human"]
print(df.head())

## Apenas onde 'sender' == 'human' e 'input_tokens' > 0
df = df[(df["sender"] == "human") & (df["input_tokens"] > 0)]
print(df.head())