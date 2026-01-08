# Tool calling
from langchain_openai import ChatOpenAI
from langchain_core.tools import tool
from dotenv import load_dotenv

# Carregando as variáveis de ambiente
load_dotenv()

# Criando uma ferramenta
@tool
def temperatura_atual(cidade: str) -> float:
    """
    Útil para obter a temperatura atual de uma cidade.

    Args:
      - cidade: Nome da cidade para obter a temperatura atual

    Returns:
      - Temperatura atual em graus Celsius
    """
    TEMPERATURA_CIDADES = {
        "são paulo": 22.5,
        "belo horizonte": 23.0
    }
    return TEMPERATURA_CIDADES.get(cidade.lower(), "Não tem informação sobre a temperatura atual dessa cidade. Diga para pesquisar no google.")

functions = {
    "temperatura_atual": temperatura_atual
}

# Instanciando o modelo
modelo = ChatOpenAI(model="gpt-4o-mini", temperature=0)
modelo_com_ferramentas = modelo.bind_tools(list(functions.values()))

# Prompt
from langchain_core.messages import SystemMessage, HumanMessage, AIMessage, ToolMessage

## ToolMessage
## name: str
## args: Dict[str, Any]
## id: Optional[str]

messages = [
    SystemMessage(content="Você é um assistente de IA que responde perguntas sobre a temperatura atual de cidades."),
    HumanMessage(content="Qual é a temperatura atual em Abre Campo?")
]

# Resposta
resposta = modelo_com_ferramentas.invoke(messages)
messages.append(resposta)

if resposta.tool_calls:
    for tool_call in resposta.tool_calls:
        tool_name = tool_call['name']
        tool_args = tool_call['args']
        tool_result = functions[tool_name].func(**tool_args)
        messages.append(ToolMessage(content=tool_result, tool_call_id=tool_call['id']))

resposta = modelo_com_ferramentas.invoke(messages)
messages.append(resposta)

# Exibindo a resposta
print(messages)
print("\n-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-\n")
print(f"Conteúdo textual: {resposta.content}")
