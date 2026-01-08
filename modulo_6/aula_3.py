# Manipulação de texto
import pandas as pd
messages = pd.read_csv("./modulo_6/messages.csv")

## Normalizando texto
messages["content"] = messages["content"].str.lower()
print(messages.head())

## Removendo pontuação
messages["content"] = messages["content"].str.replace(r"[^\w\s]", "")
print(messages.head())

## Removendo stop words
messages["content"] = messages["content"].str.replace(r"\b(e|a|o|os|as|mas|se|senão|então)\b", "")
print(messages.head())

## Removendo emojis
messages["content"] = messages["content"].str.replace(r"[:;][-]?[)(<>]?", "")
print(messages.head())

## Removendo URLs
messages["content"] = messages["content"].str.replace(r"https?://\S+", "")
print(messages.head())

# Exportando para JSONL (Json Lines)
messages.to_json("./modulo_6/messages.jsonl", orient="records", lines=True)
