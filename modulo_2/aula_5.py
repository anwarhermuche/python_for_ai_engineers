# Manipulação de arquivos (Input/Output) & Context Managers

## Abrindo um arquivo para escrita
with open("./modulo_2/aula_5.txt", "w") as arquivo:
    arquivo.write("Human: Hello AI!")

## Abrindo um arquivo para leitura
with open("./modulo_2/aula_5.txt", "r") as arquivo:
    print(arquivo.read())

## Abrindo um arquivo para leitura e escrita
with open("./modulo_2/aula_5.txt", "r+") as arquivo:
    arquivo.write("\nAI: Hello Human!")
    print(arquivo.read())

## Abrindo um arquivo com appending (adicionar ao final do arquivo)
with open("./modulo_2/aula_5.txt", "a") as arquivo:
    arquivo.write("\nHuman: How are you?")