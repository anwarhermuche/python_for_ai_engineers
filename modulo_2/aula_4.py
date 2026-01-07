# Estruturas de Repetição
## For com range (início, fim, passo) - fim não é incluído
for i in range(10):
    print(i)

for i in range(1, 10):
    print(i)

for i in range(1, 10, 2):
    print(i)

for i in range(10, 0, -1):
    print(i)

## For com lista (iterável)
for i in [1, 2, 3, 4, 5]:
    print(i)

## For com dicionário
for key, value in {"name": "John", "age": 30}.items():
    print(key, value)

## For com enumerate
for indice, valor in enumerate(["a", "b", "c", "d", "e"]):
    print(indice, valor)

# List comprehension
numbers = [1, 2, 3, 4, 5]
numbers_squared = [number ** 2 for number in numbers]
print(numbers_squared)