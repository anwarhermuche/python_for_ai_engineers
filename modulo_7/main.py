# ============================================================================
# TEORIA DESTE MÓDULO:
# Acesse o Google Colab com todo o conteúdo teórico em:
# https://colab.research.google.com/drive/1nywVNv_rAPsUbCiYtiGmBGguqlkYyfLL?usp=sharing
# ============================================================================

"""
# PROJETO DO MÓDULO — TOKEN USAGE DASHBOARD

## Objetivo:
Ler um arquivo `training_data.jsonl` do módulo anterior (conversas limpas) e gerar um PNG com dois gráficos:
1) Histograma com a distribuição de tamanho das perguntas (mensagens do usuário)
2) Gráfico de barras com a frequência de tópicos (classificados por regras)

## Estrutura esperada:
- main.py
- dashboard.py (classes do projeto)

------------------------------------
CLASSE 1: DatasetReader
------------------------------------
Responsabilidade: carregar e extrair dados brutos do JSONL.

__init__(self, jsonl_path: str)
- jsonl_path: caminho do arquivo training_data.jsonl

Métodos:
- load_conversations(self) -> list[dict]
  - lê o JSONL e retorna uma lista de conversas (dicts)

- extract_user_texts(self, conversations: list[dict]) -> list[str]
  - retorna apenas os textos de mensagens onde role == "user"

------------------------------------
CLASSE 2: TokenStats
------------------------------------
Responsabilidade: calcular métricas de tamanho e classificar tópicos.

__init__(self, avg_chars_per_word: float = 6.11, min_chars: int = 15)
- avg_chars_per_word: heurística para estimar palavras/tokens
- min_chars: filtrar perguntas muito curtas

Métodos:
- estimate_tokens(self, text: str) -> int
  - retorna tokens/palavras estimadas usando len(text)/avg_chars_per_word

- build_lengths(self, texts: list[str]) -> list[int]
  - gera lista com os comprimentos (em tokens estimados) das perguntas válidas

- classify_topic(self, text: str, topic_rules: dict[str, list[str]]) -> str
  - classifica uma pergunta em um tópico com base em keywords

- count_topics(self, texts: list[str], topic_rules: dict[str, list[str]]) -> dict[str, int]
  - conta a frequência de tópicos no conjunto de perguntas

------------------------------------
CLASSE 3: DashboardPlotter
------------------------------------
Responsabilidade: gerar e salvar os gráficos com matplotlib.

__init__(self, output_path: str = "dashboard.png")
- output_path: caminho do PNG final

Métodos:
- plot_histogram(self, lengths: list[int], title: str) -> None
  - cria histograma da distribuição

- plot_bar(self, topic_counts: dict[str, int], title: str) -> None
  - cria gráfico de barras (frequência por tópico)

- save_dashboard(self, lengths: list[int], topic_counts: dict[str, int]) -> str
  - gera os dois gráficos na mesma imagem e salva no output_path
  - retorna o caminho do arquivo gerado

------------------------------------
Regras obrigatórias:
- Usar matplotlib para gerar a imagem PNG
- Não usar IA
- main.py não pode ter lógica de cálculo nem de plotagem (só orquestração das classes)
- A classificação por tópico deve ser baseada em regras (keywords)
"""

TOPIC_RULES = {
  "Cancelamento": ["cancel", "cancelar", "assinatura", "plano"],
  "Cobrança/Pagamento": ["cobran", "cartão", "pagamento", "boleto", "estorno"],
  "App/Erro": ["trava", "erro", "tela branca", "bug", "cache"],
  "Verificação/SMS": ["sms", "código", "verificação", "2fa"],
  "Faturamento/Invoice": ["invoice", "nota fiscal", "billing", "fatura"],
  "Humano/Suporte": ["humano", "atendente", "suporte"],
  "Outros": []
}

# Importando as bibliotecas
from models.dataset_reader import DatasetReader
from models.token_stats import TokenStats
from models.dashboard_plotter import DashboardPlotter

# Lendo o arquivo JSONL
dataset_reader = DatasetReader("./modulo_6/training_data.jsonl")
user_texts = dataset_reader.extract_user_texts()

# Calculando as métricas
token_stats = TokenStats()
lengths = token_stats.build_lengths(user_texts)
topic_counts = token_stats.count_topics(user_texts, TOPIC_RULES)

# Plotando o dashboard
dashboard_plotter = DashboardPlotter()
dashboard_plotter.save_dashboard(lengths, topic_counts)