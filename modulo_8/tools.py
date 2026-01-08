from langchain.tools import tool
from datetime import datetime

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