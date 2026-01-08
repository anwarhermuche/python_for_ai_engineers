import numpy as np
from typing import Dict, Any

class VectorStore:
    def __init__(self):
        self.documents = []
        self.vectors = []

    def add_document(self, document: Dict[str, Any], vector: np.array):
        self.documents.append(document)
        self.vectors.append(vector)

    def query(self, query: np.array, k: int) -> list:
        distances = []
        for document, vector in zip(self.documents, self.vectors):
            # Cálculo da distância de cosseno
            distance = 1 - (np.dot(query, vector) / (np.linalg.norm(query) * np.linalg.norm(vector)))
            distances.append((distance, document))
        
        # Ordenação dos resultados por similaridade (menor -> maior)
        distances.sort(key=lambda x: x[0])
        return [(distance[1], distance[0]) for distance in distances[:k]]