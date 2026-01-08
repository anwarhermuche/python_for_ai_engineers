# Numpy
## NumPy é uma biblioteca de computação científica em Python.

## Criando um array do numpy
import numpy as np

array = np.array([1, 2, 3, 4, 5])
print(array)

## Criando um array do numpy com zeros
array = np.zeros(10)
print(array)

## Criando um array do numpy com intervalo
array = np.arange(10)
print(array)

## Criando uma matriz 3x3 com uns
array = np.ones((3, 3))
print(array)


# Aritmética de arrays
## Multiplicando um array por um escalar
array = array * 2
print(array)

## Multiplicando um array por um array
array = array * array
print(array)

## Somando um array com um escalar
array = array + 1
print(array)

## Somando um array com um array
array = array + array
print(array)


# Performance
## Arrays do numpy X Listas do Python (tempos de execução)
import time
import numpy as np

N = 10_000_000

# Python puro
data_py = list(range(N))
t0 = time.time()
s = 0
for x in data_py:
    s += x * 2
t_py = time.time() - t0

# NumPy
data_np = np.arange(N)
t0 = time.time()
s = np.sum(data_np * 2)
t_np = time.time() - t0

print(f"Python puro: {t_py:.4f}s")
print(f"NumPy:       {t_np:.4f}s")
print(f"Quanto mais rápido?     {t_py / t_np:.1f}x")