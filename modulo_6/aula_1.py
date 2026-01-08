# Dataframes e Carregamento
import pandas as pd

# Carregando um arquivo CSV
df = pd.read_csv("./modulo_6/messages.csv")

# Carregando um arquivo Excel
# df = pd.read_excel("data.xlsx")

# Carregando um arquivo JSON
# df = pd.read_json("data.json")

# Mostrando as primeiras linhas do dataframe
print(df.head(5))

# Mostrando as últimas linhas do dataframe
print(df.tail(5))

# Mostrando as colunas do dataframe
print(df.columns)

# Mostrando as dimensões do dataframe
print(df.shape)

# Mostrando o tipo de cada coluna
print(df.dtypes)

# Mostrando as informações do dataframe
print(df.info())

# Mostrando as estatísticas do dataframe
print(df.describe())

# Valores únicos de uma coluna
print(df["sender"].unique())
