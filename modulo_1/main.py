# ============================================================================
# TEORIA DESTE MÓDULO:
# Acesse o Google Colab com todo o conteúdo teórico em:
# https://colab.research.google.com/drive/12byCah1WbnHsSdnsfnArDkm_UVfOIZ4t?usp=sharing
# ============================================================================

"""
# PROJETO 1 — PROMPT PACKER (BÁSICO)

## Criar um programa que recebe (via terminal):
- role
- tom de voz
- tarefa
- número máximo de palavras

## Regras obrigatórias:
- O programa deve montar um prompt final usando f-strings, no formato:
  - Role: ...
  - Tom de voz: ...
  - Tarefa: ...
  - Instruções: ...
- O programa deve estimar a quantidade de palavras do prompt final usando a heurística:
  - 1 palavra ≈ 6.11 caracteres
- O programa deve checar se a quantidade estimada de palavras ficou dentro de uma faixa aceitável:
  - entre (máximo de palavras - 10) e (máximo de palavras + 10)

## Esse programa deve retornar:
- prompt final (string)
- quantidade de palavras estimada (float ou int)
- está dentro do intervalo aceitável? (bool)
"""

# Inputs do usuário
role = input("Digite a role: ")
tom_de_voz = input("Digite o tom de voz: ")
tarefa = input("Digite a tarefa: ")
numero_maximo_de_palavras = int(input("Digite o número máximo de palavras: "))

# Outputs
## Prompt final
prompt_final = f"""
# Role
{role}

# Tom de voz
{tom_de_voz}

# Tarefa
{tarefa}

Pense passo a passo antes de responder.
"""

## Quantidade de palavras estimada
palavras_estimadas = len(prompt_final) // 6.11

## Está dentro do intervalo aceitável?
dentro_do_intervalo = numero_maximo_de_palavras - 10 <= palavras_estimadas <= numero_maximo_de_palavras + 10

# Outputs
print(f"Prompt final: {prompt_final}")
print(f"Quantidade de palavras estimada: {palavras_estimadas}")
print(f"Está dentro do intervalo aceitável? {dentro_do_intervalo}")