"""
# PROJETO — SIMPLE VECTOR STORE

## Objetivo:
Criar uma estrutura orientada a objeto que armazena vetores numéricos em memória
e permite realizar buscas matemáticas por similaridade.

## O programa deve:
- Definir uma classe responsável por gerenciar documentos vetoriais
- Armazenar documentos e seus vetores associados em memória
- Expor um método de busca (query) que:
  - Recebe um vetor de consulta (NumPy array)
  - Recebe um parâmetro K
  - Retorna os K documentos mais similares matematicamente
- Expor um método para adicionar documentos e seus vetores associados

## Formato do documento:
{
"page_content": "...",
"metadata": {"source": "...", "page": 3}
}

## Formato do vetor:
np.array([0.0, 0.2, ...])

## Regras obrigatórias:
- Os vetores devem ser representados com NumPy arrays
- A similaridade deve ser calculada usando distância de cosseno
- A função de similaridade deve ser implementada manualmente com NumPy
- O método query deve ordenar os resultados por similaridade (maior → menor)
- Não é permitido o uso de bibliotecas prontas de busca ou similaridade

## Estruturas que devem ser utilizadas:
- Classe com atributos para armazenar os dados
- Dicionário ou lista para armazenar documentos e vetores
- NumPy para operações vetoriais

## Estrutura mínima esperada:
- src/
  - vector_store.py
  - main.py

## Esse projeto deve retornar:
- Uma lista com os K documentos mais similares
- O valor de similaridade associado a cada documento
"""
import numpy as np

documentos = {
    "doc_1": {
        "page_content": "Python e engenharia de dados",
        "metadata": {"source": "doc_1", "page": 1}
    },
    "doc_2": {
        "page_content": "Modelos de linguagem e IA generativa",
        "metadata": {"source": "doc_2", "page": 2}
    },
    "doc_3": {
        "page_content": "Banco de dados e SQL",
        "metadata": {"source": "doc_3", "page": 3}
    }
}

vetores = {
    "doc_1": np.array([0.9, 0.1, 0.0, 0.2]),
    "doc_2": np.array([0.1, 0.8, 0.6, 0.0]),
    "doc_3": np.array([0.0, 0.2, 0.1, 0.9])
}

# Instanciando a classe VectorStore
from vector_store import VectorStore
vector_store = VectorStore()

# Adicionando os documentos
for k in range(len(documentos)):
    vector_store.add_document(documentos[f"doc_{k+1}"], vetores[f"doc_{k+1}"])

# Buscando os documentos mais similares
resultados = vector_store.query(np.array([0.2, 0.7, 0.5, 0.1]), 3)
print(resultados)