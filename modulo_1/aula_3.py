# Recebendo input do usuário
nome_usuario = input("Digite seu nome: ")

# Construindo um prompt usando f-strings
prompt = f"""
Você é um atendente de uma empresa de tecnologia e está conversando com o {nome_usuario}.

"""
print(prompt)

# Métodos de manipulação de strings
## Limpar espaços em branco - strip()
prompt_limpo = prompt.strip()
print(prompt_limpo)

## Converter para maiúsculas - upper()
prompt_maiusculo = prompt.upper()
print(prompt_maiusculo)

## Converter para minúsculas - lower()
prompt_minusculo = prompt.lower()
print(prompt_minusculo)

## Substituir um texto - replace()
prompt_substituido = prompt.replace("tecnologia", "materiais de construção")
print(prompt_substituido)

## Caracteres de escape (\n e \t)
prompt_com_quebra_de_linha = "Olá, como você está?\n\tEstou bem, obrigado!"
print(prompt_com_quebra_de_linha)

## Comprimento da string - len()
comprimento_string = len(prompt)
print(comprimento_string)