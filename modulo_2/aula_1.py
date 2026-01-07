# Listas
messages = ["Human: Hello AI!", "AI: Hello Human!", "Human: How are you?", "AI: I'm fine, thank you!"]

# Acessando elementos da lista
## Índice
print(messages[0])

## Índice negativo
print(messages[-1])

# Slicing
## Início e fim - sem incluir o fim
print(messages[0:2])

## Double slicing - pulando de 2 em 2
print(messages[::2])

## Reverse slicing - invertendo a lista
print(messages[::-1])

# Adicionando elementos à lista
## Adicionar no final
messages.append("Human: good!")
print(messages)

## Adicionar em um índice específico
messages.insert(0, "Human: What's your name?")
print(messages)

## Adicionar vários elementos
messages.extend(["AI: My name is AI!", "Humano: What's your favorite color?"])
print(messages)

## Split em strings
messages_split = "Human: Hello AI!\nAI: Hello Human!\nHuman: How are you?\nAI: I'm fine, thank you!".split("\n")
print(messages_split)

# Tuplas (imutável)
messages_tuple = ("Human: Hello AI!", "AI: Hello Human!", "Human: How are you?", "AI: I'm fine, thank you!")
print(messages_tuple)

# Acessando elementos da tupla
print(messages_tuple[0])

# Slicing
print(messages_tuple[0:2])

# Adicionando elementos à tupla
messages_tuple.append("Human: good!")