# Princípio DRY (Don't Repeat Yourself)

## Antes de usar uma função
idade = 18
if idade >= 60:
    print("Você é um idoso")
elif idade >= 18:
    print("Você é um adulto")
else:
    print("Você é um criança")

## Depois de usar uma função
def verificar_idade(idade: int) -> str:
    if idade >= 60:
        return "Você é um idoso"
    elif idade >= 18:
        return "Você é um adulto"
    else:
        return "Você é um criança"

resultado = verificar_idade(18)
print(resultado)

# Função recursiva
def fatorial(n: int) -> int:
    if n == 0:
        return 1
    else:
        return n * fatorial(n - 1)

print(fatorial(5))

# Função lambda
soma = lambda x: x + 1
print(soma(1))