from langchain.tools import tool
from datetime import datetime
import requests

@tool
def get_current_time() -> str:
    """
    Útil para obter a data e hora atual.

    Returns:
      - Data e hora atual no formato "YYYY-MM-DD HH:MM:SS"
    """
    return datetime.now().strftime("%Y-%m-%d %H:%M:%S")

@tool
def count_words_in_phrase(phrase: str) -> int:
    """
    Útil para contar o número de palavras em uma frase.

    Args:
      - phrase: Frase para contar o número de palavras

    Returns:
      - Número de palavras na frase
    """
    return len(phrase.split())

@tool
def get_pokemon_info(pokemon_name: str) -> str:
    """
    Útil para obter informações básicas de um Pokémon.

    Args:
      - pokemon_name: Nome do Pokémon para obter informações

    Returns:
      - Informações básicas do Pokémon
    """
    url = f"https://pokeapi.co/api/v2/pokemon/{pokemon_name}"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        return f"Erro ao obter informações do Pokémon {pokemon_name}"