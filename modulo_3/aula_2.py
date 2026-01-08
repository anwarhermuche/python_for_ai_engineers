# Erros e Exceções

## Erros
def dividir(a: int, b: int) -> float:
    return a / b

print(dividir(10, 0))

## Exceções
try:
    print(dividir(10, 0))
except ZeroDivisionError:
    print("Erro: divisão por zero")

## Criando função que lança uma exceção
def dividir(a: int, b: int) -> float:
    if b == 0:
        raise ValueError("Erro: divisão por zero")
    return a / b

## Principais tipos de exceções
# - ZeroDivisionError: divisão por zero
# - ValueError: valor inválido
# - TypeError: tipo inválido
# - IndexError: índice inválido
# - KeyError: chave inválida
# - FileNotFoundError: arquivo não encontrado
# - PermissionError: permissão negada
# - ImportError: erro ao importar módulo
# - NameError: nome inválido
# - AttributeError: atributo inválido