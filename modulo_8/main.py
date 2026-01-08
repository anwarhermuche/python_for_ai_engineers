"""
# PROJETO DO MÓDULO — THE CLI ASSISTANT

## Objetivo:
Criar um assistente de terminal orientado a objetos que interpreta perguntas em
linguagem natural, decide qual ferramenta utilizar e mantém memória persistente
da conversa entre execuções.

## Ferramentas disponíveis:
- get_current_time()
  - Retorna a data e hora atual usando datetime
- count_words_in_phrase(phrase: str)
  - Retorna a quantidade de palavras em uma frase

--------------------------------------------------
CLASSE PRINCIPAL: CLIAssistant
--------------------------------------------------

__init__(self, history_path: str)
- history_path: caminho do arquivo .txt usado como memória persistente

Responsabilidades:
- Carregar histórico salvo em arquivo
- Exibir histórico ao iniciar
- Controlar o loop principal da conversa
- Decidir qual ferramenta chamar com base na pergunta do usuário
- Registrar todas as interações no histórico

Métodos obrigatórios:
- load_history(self) -> list[str]
  - Lê o arquivo de histórico e retorna as linhas

- save_message(self, sender: str, content: str) -> None
  - Salva uma mensagem no arquivo de histórico

- run(self) -> None
  - Inicia o loop principal do assistente
  - Encerra quando o usuário digitar "/stop"

## Estrutura do projeto:
- main.py            → ponto de entrada e orquestração (esse arquivo)
- cli_assistant.py    → classe responsável por criar o agente
- tools.py           → arquivo para criar as ferramentas

--------------------------------------------------
REGRAS OBRIGATÓRIAS:
--------------------------------------------------
- O histórico deve ser persistido em um arquivo `.txt`
- O arquivo deve ser manipulado usando context manager (`with open(...)`)
- Cada mensagem do usuário e cada resposta do assistente devem ser salvas (inclui as mensagens das Tools)
- A decisão da ferramenta deve ser feita pelo agente criado com create_agent
- O assistente deve reaproveitar o histórico entre execuções

## Estruturas que devem ser utilizadas:
- Classes e métodos
- Funções para representar ferramentas
- Loop `while`
- Manipulação de arquivos para memória persistente
"""

# Importando a classe CLIAssistant
from cli_assistant import CLIAssistant

# Definindo o System Prompt e o Modelo
MODELO = "gpt-5.2"
SYSTEM_PROMPT = """
Você é um assistente pessoal do Anwar Hermuche, chame-o pelo nome.
"""

cli_assistant = CLIAssistant(model=MODELO, system_prompt=SYSTEM_PROMPT, history_path="./modulo_8/conversation_history.txt")
cli_assistant.run()