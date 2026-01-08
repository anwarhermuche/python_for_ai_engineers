# Operações Vetoriais e Similaridade
import numpy as np
## Produto Escalar
## Fórmula: u.v = |u| * |v| * cos(theta)
## Onde:
## u.v é o produto escalar
## |u| é o módulo do vetor u
## |v| é o módulo do vetor v
## theta é o ângulo entre os vetores

## Módulo de um vetor
## Fórmula: |v| = sqrt(v1^2 + v2^2 + ... + vn^2)
## Onde:
## |v| é o módulo do vetor v
## v1, v2, ..., vn são os componentes do vetor

## Exemplo:
v = np.array([1, 2, 3])
print(f"Módulo do vetor v: {np.linalg.norm(v)}")

## Cálculo do produto escalar entre dois vetores
v1 = np.array([1, 0])
v2 = np.array([0, 1])
produto_escalar = np.dot(v1, v2)
print(f"Produto escalar: {produto_escalar}")

## Ângulo entre dois vetores (em graus)
angulo = np.arccos(produto_escalar / (np.linalg.norm(v1) * np.linalg.norm(v2)))
print(f"Ângulo: {angulo * 180 / np.pi} graus")

## Distância de cosseno
## Fórmula: d(u, v) = 1 - cos(theta)
## Onde:
## d(u, v) é a distância de cosseno entre os vetores u e v
## cos(theta) é o cosseno do ângulo entre os vetores

## Exemplo:
distancia_cosseno = 1 - np.cos(angulo)
print(f"Distância de cosseno: {distancia_cosseno}")