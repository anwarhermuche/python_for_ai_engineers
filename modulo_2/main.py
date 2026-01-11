# ============================================================================
# TEORIA DESTE MÓDULO:
# Acesse o Google Colab com todo o conteúdo teórico em:
# https://colab.research.google.com/drive/150bsJNuuPEhTeUqUp0UzQu0mVb348Meg?usp=sharing
# ============================================================================

"""
# PROJETO 2 — CHAT COM MEMÓRIA PERSISTENTE

## Criar um programa que simula um chat via terminal entre o usuário e um sistema.

## O programa deve:
- Ler um histórico de mensagens salvo em arquivo `.txt` no início da execução
- Exibir todo o histórico no terminal antes de iniciar a nova conversa
- Entrar em um loop contínuo de conversa
- Receber mensagens do usuário
- Gerar uma resposta simples e determinística do sistema (sem uso de IA)
- Encerrar a conversa quando o usuário digitar "/stop"

## Regras obrigatórias:
- Cada mensagem do usuário e cada resposta do sistema devem ser salvas em uma nova linha do arquivo `.txt`
- O programa não pode perder o histórico ao ser encerrado
- O histórico deve ser reaproveitado em execuções futuras
- Dicionários para representar mensagens (ex: {"role": "human", "content": "..."} )
"""

# Obtendo o histórico
with open("./modulo_2/conversation_history.txt", "r") as historico_conversa:
    messages = historico_conversa.read().split("\n")
    messages = [{"role": message.split(": ")[0].lower(),
                "content": message.split(": ")[1]}
                for message in messages if message]

# Exibindo o histórico
print("# Histórico")
for message in messages:
    print(f"- {message}")

# Entrando em um loop contínuo de conversa
print("# Novas mensagens")
while True:
    new_messages = []
    user_message = input("Você: ")
    
    # Condição de parada
    if user_message == "/stop":
        break

    # Adicionando a mensagem do usuário e da AI ao histórico
    new_messages.append({"role": "human", "content": user_message})
    print("AI: Olá!")
    new_messages.append({"role": "ai", "content": "Olá?"})

    # Salvando o histórico em um arquivo
    with open("./modulo_2/conversation_history.txt", "a") as historico_conversa:
        for message in new_messages:
            historico_conversa.write(f"{message['role']}: {message['content']}\n")
