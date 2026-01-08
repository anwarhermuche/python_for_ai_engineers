# Agentes
from langchain_openai import ChatOpenAI
from langchain.agents import create_agent
from langchain.tools import tool
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


# Criando um agente
agent = create_agent("openai:gpt-4o-mini", tools = [temperatura_atual])

# Prompt
prompt = "Qual é a temperatura atual em São Paulo?"

# Resposta
resposta = agent.invoke({"messages": [{"role": "user", "content": prompt}]})
print(f"Conteúdo textual: {resposta['messages'][-1].content}")