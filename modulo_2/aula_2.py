# Dicionários (chave-valor)
human_message = {
    'role': 'ai',
    'content': 'How can I help you?'
}

# Acessando elementos do dicionário
print(human_message['role'])
print(human_message.get('content'))

# Substituindo elementos ao dicionário
human_message['content'] = 'How are you?'
print(human_message)

# Adicionando elementos ao dicionário
human_message['tokens'] = [{"tokens_input": 100, "tokens_output": 200}]
print(human_message)

# Removendo elementos do dicionário
human_message.pop('tokens')
print(human_message)