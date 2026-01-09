# 🐍 Python Foundations for AI Engineering

<div align="center">

![Python](https://img.shields.io/badge/Python-3.13+-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Poetry](https://img.shields.io/badge/Poetry-Package%20Manager-60A5FA?style=for-the-badge&logo=poetry&logoColor=white)
![LangChain](https://img.shields.io/badge/LangChain-Agents-1C3C3C?style=for-the-badge&logo=langchain&logoColor=white)
![NumPy](https://img.shields.io/badge/NumPy-Vetores-013243?style=for-the-badge&logo=numpy&logoColor=white)
![Pandas](https://img.shields.io/badge/Pandas-ETL-150458?style=for-the-badge&logo=pandas&logoColor=white)

**De Zero a Pipelines de Dados Profissionais**

*Curso completo para formar a base técnica sólida necessária para construir sistemas de IA, focando em boas práticas, manipulação de dados textuais/vetoriais e engenharia de software.*

</div>

---

## 📋 Índice

- [Objetivo](#-objetivo)
- [Pré-requisitos](#-pré-requisitos)
- [Instalação](#-instalação)
- [Estrutura do Projeto](#-estrutura-do-projeto)
- [Módulos do Curso](#-módulos-do-curso)
  - [Módulo 1: Fundamentos & Versionamento](#módulo-1-fundamentos--versionamento)
  - [Módulo 2: Estruturas de Dados & Persistência](#módulo-2-estruturas-de-dados--persistência)
  - [Módulo 3: Profissionalização](#módulo-3-profissionalização-funções-módulos--poetry)
  - [Módulo 4: POO e Integrações](#módulo-4-poo-e-integrações)
  - [Módulo 5: NumPy - Matemática dos Vetores](#módulo-5-numpy---a-matemática-dos-vetores)
  - [Módulo 6: Pandas - Engenharia de Dados](#módulo-6-pandas---engenharia-de-dados)
  - [Módulo 7: Matplotlib - Observabilidade](#módulo-7-matplotlib---observabilidade)
  - [Módulo 8: LangChain & Agentes](#módulo-8-introdução-ao-langchain--agentes)
- [Tecnologias Utilizadas](#-tecnologias-utilizadas)
- [Autor](#-autor)

---

## 🎯 Objetivo

Este curso forma a **base técnica sólida** necessária para construir sistemas de Inteligência Artificial, com foco em:

- ✅ Boas práticas de engenharia de software
- ✅ Manipulação de dados textuais e vetoriais
- ✅ Gestão profissional de dependências com Poetry
- ✅ Preparação de datasets para Fine-Tuning
- ✅ Busca semântica com vetores
- ✅ Construção de agentes com LangChain

---

## 📚 Pré-requisitos

- Python 3.13+
- Cursor IDE (ou VS Code)
- Git & GitHub
- Conta na OpenAI (para o Módulo 8)

---

## 🚀 Instalação

```bash
# Clone o repositório
git clone https://github.com/seu-usuario/python_for_ai_engineers.git
cd python_for_ai_engineers

# Instale as dependências com Poetry
poetry install

# Ative o ambiente virtual
poetry shell
```

### Configuração de Variáveis de Ambiente

Crie um arquivo `.env` na raiz do projeto:

```env
OPENAI_API_KEY=sk-sua-chave-aqui
LLAMA_API_KEY=sk-sua-chave-aqui
```

> ⚠️ **Importante:** O arquivo `.env` nunca deve ser versionado no Git!

---

## 📁 Estrutura do Projeto

```
python_for_ai_engineers/
├── modulo_1/                    # Fundamentos & Versionamento
│   ├── aula_1.py               # Primeiro código (print, comentários)
│   ├── aula_2.py               # Variáveis e tipos de dados
│   ├── aula_3.py               # Manipulação de strings e f-strings
│   ├── aula_4.py               # Operadores aritméticos e lógicos
│   └── main.py                 # 🏆 Projeto: Prompt Packer
│
├── modulo_2/                    # Estruturas de Dados & Persistência
│   ├── aula_1.py               # Listas e Tuplas
│   ├── aula_2.py               # Dicionários (Hash Maps)
│   ├── aula_3.py               # Estruturas condicionais (if/else)
│   ├── aula_4.py               # Estruturas de repetição (for/while)
│   ├── aula_5.py               # Manipulação de arquivos & Context Managers
│   ├── conversation_history.txt
│   └── main.py                 # 🏆 Projeto: Persistent Chat History
│
├── modulo_3/                    # Profissionalização
│   ├── aula_1.py               # Funções, escopo e type hinting
│   ├── aula_2.py               # Erros e exceções (try/except)
│   ├── aula_3.py               # Poetry - Gestão de dependências
│   ├── aula_4.py               # Modularização e imports
│   ├── calculadora.py          # Módulo de cálculo de custos
│   ├── log.txt                 # Log de execuções
│   └── main.py                 # 🏆 Projeto: Token Cost Calculator
│
├── modulo_4/                    # POO e Integrações
│   ├── aula_1.py               # Introdução à POO (classes, objetos)
│   ├── aula_2.py               # Herança e polimorfismo
│   ├── aula_3.py               # Variáveis de ambiente (.env)
│   ├── models/
│   │   ├── base.py             # Classe base ModeloBase
│   │   ├── openai.py           # Subclasse OpenAIModel
│   │   └── llama.py            # Subclasse LlamaModel
│   └── main.py                 # 🏆 Projeto: Model Provider SDK
│
├── modulo_5/                    # NumPy - Vetores
│   ├── aula_1.py               # Introdução ao NumPy (arrays, performance)
│   ├── aula_2.py               # Operações vetoriais e similaridade
│   ├── vector_store.py         # Classe VectorStore
│   └── main.py                 # 🏆 Projeto: Simple Vector Store
│
├── modulo_6/                    # Pandas - ETL
│   ├── aula_1.py               # DataFrames e carregamento de dados
│   ├── aula_2.py               # Limpeza de dados (Data Cleaning)
│   ├── aula_3.py               # Manipulação de texto e exportação
│   ├── etl.py                  # Classe ETL (pipeline completo)
│   ├── support_logs_dirty.csv  # Dataset sujo de entrada
│   ├── training_data.jsonl     # Dataset limpo de saída
│   └── main.py                 # 🏆 Projeto: Fine-Tuning Dataset Prepper
│
├── modulo_7/                    # Matplotlib - Visualização
│   ├── aula_1.py               # Gráficos de barras e linhas
│   ├── aula_2.py               # Histogramas e boxplots
│   ├── models/
│   │   ├── dataset_reader.py   # Classe DatasetReader
│   │   ├── token_stats.py      # Classe TokenStats
│   │   └── dashboard_plotter.py # Classe DashboardPlotter
│   ├── dashboard.png           # Dashboard gerado
│   └── main.py                 # 🏆 Projeto: Token Usage Dashboard
│
├── modulo_8/                    # LangChain & Agentes
│   ├── aula_2.py               # Models & Messages (ChatOpenAI)
│   ├── aula_3.py               # Structured Outputs (Pydantic)
│   ├── aula_4.py               # Tool Calling (@tool)
│   ├── aula_5.py               # Agentes (create_agent)
│   ├── tools.py                # Ferramentas customizadas
│   ├── cli_assistant.py        # Classe CLIAssistant
│   ├── conversation_history.txt
│   └── main.py                 # 🏆 Projeto: The CLI Assistant
│
├── src/                         # Estrutura Poetry
│   └── python_for_ai_engineers/
│       └── __init__.py
├── tests/
│   └── __init__.py
├── pyproject.toml              # Configuração Poetry
├── poetry.lock                 # Lock de dependências
└── README.md
```

---

## 📖 Módulos do Curso

### Módulo 1: Fundamentos & Versionamento

> **Foco:** Aprender a sintaxe básica, lógica de programação e versionamento com Git.

#### Aulas

| Aula | Tema | Conteúdo |
|------|------|----------|
| 1.1 | O Ambiente e o Primeiro Código | Instalação Python 3.13+, Cursor, Poetry, `print()`, comentários |
| 1.2 | Variáveis e Tipos de Dados | `str`, `int`, `float`, `bool`, casting, `type()` |
| 1.3 | Manipulação de Texto (Strings) | `input()`, f-strings, `.strip()`, `.lower()`, `.replace()`, `\n`, `\t` |
| 1.4 | Operadores Aritméticos e Lógicos | `+`, `-`, `*`, `/`, `%`, `==`, `!=`, `>`, `<` |
| 1.5 | Git e GitHub | `git init`, `git add`, `git commit`, `git push`, `.gitignore` |

#### 🏆 Projeto: Prompt Packer

Script que recebe via terminal:
- Role, tom de voz, tarefa e número máximo de palavras
- Monta um prompt final usando f-strings
- Estima quantidade de palavras (1 palavra ≈ 6.11 caracteres)
- Retorna se está dentro do intervalo aceitável (±10 palavras)

```python
# Exemplo de uso
prompt_final = f"""
# Role
{role}

# Tom de voz
{tom_de_voz}

# Tarefa
{tarefa}

Pense passo a passo antes de responder.
"""
palavras_estimadas = len(prompt_final) // 6.11
dentro_do_intervalo = numero_maximo - 10 <= palavras_estimadas <= numero_maximo + 10
```

---

### Módulo 2: Estruturas de Dados & Persistência

> **Foco:** Dominar estruturas de dados e persistir informações em arquivos.

#### Aulas

| Aula | Tema | Conteúdo |
|------|------|----------|
| 2.1 | Listas e Tuplas | Índices, slicing, `.append()`, `.insert()`, `.extend()` |
| 2.2 | Dicionários | Chave-valor `{"role": "user"}`, `.get()`, `.pop()` |
| 2.3 | Estruturas Condicionais | `if`, `elif`, `else` |
| 2.4 | Estruturas de Repetição | `for`, `while`, `range()`, list comprehension |
| 2.5 | Manipulação de Arquivos | `open()`, modos `w`, `r`, `a`, context managers `with` |

#### 🏆 Projeto: Persistent Chat History

Chat via terminal com memória persistente:
- Lê histórico salvo em arquivo `.txt` ao iniciar
- Loop contínuo de conversa até digitar `/stop`
- Cada mensagem salva usando `with open(...)`

```python
# Salvando histórico
with open("./modulo_2/conversation_history.txt", "a") as historico:
    for message in new_messages:
        historico.write(f"{message['role']}: {message['content']}\n")
```

---

### Módulo 3: Profissionalização (Funções, Módulos & Poetry)

> **Foco:** O salto de "Scripter" para "Engenheiro". Organização de projeto e tipagem forte.

#### Aulas

| Aula | Tema | Conteúdo |
|------|------|----------|
| 3.1 | Funções e Escopo | Princípio DRY, `def`, parâmetros, `return`, type hinting |
| 3.2 | Erros e Exceções | `try/except`, `raise`, tipos de exceções |
| 3.3 | Poetry | `poetry init`, `poetry add`, `poetry run`, `pyproject.toml` |
| 3.4 | Modularização | Dividir código em módulos, imports |

#### 🏆 Projeto: Token Cost Calculator

Mini-biblioteca para estimar custo mensal de modelos de linguagem:

```python
CUSTO_MODELOS_DOLAR = {
    "gpt-5.1": {"input": 1.25, "output": 10},
    "claude-4.5-opus": {"input": 5, "output": 25}
}

def calcular_custo_total(modelo: str,
                         tokens_system_prompt: int,
                         media_tokens_input: int,
                         media_tokens_output: int,
                         media_mensagens_por_dia: int) -> float:
    # Considera janela de contexto crescente
    # Registra cada cálculo em log.txt
    ...
```

---

### Módulo 4: POO e Integrações

> **Foco:** Criar objetos robustos e usar bibliotecas de terceiros.

#### Aulas

| Aula | Tema | Conteúdo |
|------|------|----------|
| 4.1 | Introdução à POO | Classes vs Objetos, `__init__`, `self` |
| 4.2 | Herança e Polimorfismo | Classe base genérica, subclasses, `super()` |
| 4.3 | Variáveis de Ambiente | `python-dotenv`, `.env`, segurança de API Keys |

#### 🏆 Projeto: Model Provider SDK

Mini-SDK que simula provedores de modelos usando POO:

```python
class ModeloBase:
    def invoke(self, prompt: str, api_key: str) -> str:
        raise NotImplementedError("Subclasses devem implementar este método")

class OpenAIModel(ModeloBase):
    def invoke(self, prompt: str, api_key: str = OPENAI_API_KEY) -> str:
        if not api_key.startswith("sk-"):
            raise ValueError("API Key inválida")
        time.sleep(3)  # Simula latência
        return {"model": self.nome, "output": "Resposta da OpenAI", "temperatura": self.temperatura}
```

---

### Módulo 5: NumPy - A Matemática dos Vetores

> **Foco:** Entender Embeddings e Busca Semântica na prática.

#### Aulas

| Aula | Tema | Conteúdo |
|------|------|----------|
| 5.1 | Introdução ao NumPy | Arrays vs Listas, performance, conceito de vetor |
| 5.2 | Operações Vetoriais | Produto escalar, distância de cosseno, similaridade |

#### Comparação de Performance

```python
# NumPy é até 100x mais rápido que Python puro!
Python puro: 0.8234s
NumPy:       0.0082s
Speedup:     100.4x
```

#### 🏆 Projeto: Simple Vector Store

Armazenamento de vetores em memória com busca por similaridade:

```python
class VectorStore:
    def query(self, query: np.array, k: int) -> list:
        distances = []
        for document, vector in zip(self.documents, self.vectors):
            # Distância de cosseno
            distance = 1 - (np.dot(query, vector) / 
                          (np.linalg.norm(query) * np.linalg.norm(vector)))
            distances.append((distance, document))
        
        distances.sort(key=lambda x: x[0])
        return distances[:k]
```

---

### Módulo 6: Pandas - Engenharia de Dados

> **Foco:** Limpar e preparar dados textuais para RAG ou Fine-Tuning.

#### Aulas

| Aula | Tema | Conteúdo |
|------|------|----------|
| 6.1 | DataFrames e Carregamento | `read_csv`, `read_json`, `head()`, `info()`, `describe()` |
| 6.2 | Limpeza de Dados | `dropna`, `drop_duplicates`, filtragem booleana |
| 6.3 | Manipulação de Texto | String methods em massa, exportação JSONL |

#### 🏆 Projeto: Fine-Tuning Dataset Prepper

Pipeline ETL completo para preparar dados de treinamento:

```python
class ETL:
    def pipeline(self) -> pd.DataFrame:
        df = self.normalize_sender(self.data)      # human/ai
        df = self.normalize_content(df)            # Remove PIIs
        df = self.normalize_created_at(df)         # Parse datas
        df = self.remove_duplicates(df)            # Deduplicação
        jsonl = self.transform_data(df)            # Formato JSONL
        self.export_data(jsonl)                    # training_data.jsonl
        return df
```

**Saída no formato para Fine-Tuning:**
```json
{"messages":[{"role":"user","content":"..."},{"role":"assistant","content":"..."}]}
```

---

### Módulo 7: Matplotlib - Observabilidade

> **Foco:** Visualizar o que está acontecendo com seus dados/modelos.

#### Aulas

| Aula | Tema | Conteúdo |
|------|------|----------|
| 7.1 | Gráficos Básicos | Barras, linhas, títulos, labels |
| 7.2 | Visualizando Dados de IA | Histogramas, distribuição de tokens, outliers |

#### 🏆 Projeto: Token Usage Dashboard

Dashboard orientado a objetos que analisa dados de treinamento:

```python
# Estrutura de classes
DatasetReader   → Carrega e extrai textos do JSONL
TokenStats      → Estima tokens e classifica tópicos
DashboardPlotter → Gera histograma + gráfico de barras

# Classificação por regras
TOPIC_RULES = {
  "Cancelamento": ["cancel", "cancelar", "assinatura"],
  "Cobrança/Pagamento": ["cobran", "cartão", "pagamento"],
  "App/Erro": ["trava", "erro", "bug"],
  ...
}
```

---

### Módulo 8: Introdução ao LangChain & Agentes

> **Foco:** Transformar código estático em sistemas cognitivos. Python como linguagem de orquestração de IA.

#### Aulas

| Aula | Tema | Conteúdo |
|------|------|----------|
| 8.1 | Ecossistema LangChain | Por que usar? Conceito de "Cadeias" |
| 8.2 | Models & Messages | `ChatOpenAI`, `SystemMessage`, `HumanMessage`, `AIMessage` |
| 8.3 | Structured Outputs | `.with_structured_output()`, Pydantic |
| 8.4 | Tool Calling | Decorador `@tool`, `bind_tools()` |
| 8.5 | Agentes | Loop ReAct, `create_agent()` |

#### Exemplo: Extração de Dados com Structured Output

```python
class Resposta(BaseModel):
    nome: str = Field(description="O nome da pessoa")
    data: datetime = Field(description="A data do e-mail")
    intencao: Literal["comercial", "suporte", "outros"]

modelo_estruturado = modelo.with_structured_output(Resposta)
resposta = modelo_estruturado.invoke(email)
# Retorna objeto Python tipado e validado!
```

#### 🏆 Projeto: The CLI Assistant

Assistente de terminal com memória persistente e ferramentas:

```python
class CLIAssistant:
    def __init__(self, model: str, system_prompt: str, history_path: str):
        self.agent = create_agent(self.model, tools=[
            get_current_time,      # Retorna data/hora atual
            count_words_in_phrase  # Conta palavras em frase
        ])
    
    def run(self) -> None:
        while True:
            user_input = input("Você: ")
            if user_input == "/stop":
                break
            response = self.message_agent(HumanMessage(content=user_input))
            print(f"AI: {response}")
```

**Ferramentas Disponíveis:**

```python
@tool
def get_current_time() -> str:
    """Retorna a data e hora atual."""
    return datetime.now().strftime("%Y-%m-%d %H:%M:%S")

@tool
def count_words_in_phrase(phrase: str) -> int:
    """Conta o número de palavras em uma frase."""
    return len(phrase.split())
```

---

## 🛠 Tecnologias Utilizadas

| Tecnologia | Versão | Uso |
|------------|--------|-----|
| **Python** | 3.13+ | Linguagem principal |
| **Poetry** | 2.0+ | Gestão de dependências |
| **NumPy** | 2.4.0+ | Operações vetoriais e matemáticas |
| **Pandas** | 2.3.3+ | Manipulação e limpeza de dados |
| **Matplotlib** | 3.10.8+ | Visualização de dados |
| **LangChain** | 1.2.3+ | Framework de agentes |
| **LangChain-OpenAI** | 1.1.7+ | Integração com OpenAI |
| **python-dotenv** | 1.2.1+ | Variáveis de ambiente |

---

## 📦 Dependências

```toml
[project]
name = "python-for-ai-engineers"
version = "0.1.0"
requires-python = ">=3.13,<4.0.0"
dependencies = [
    "numpy (>=2.4.0,<3.0.0)",
    "python-dotenv (>=1.2.1,<2.0.0)",
    "pandas (>=2.3.3,<3.0.0)",
    "matplotlib (>=3.10.8,<4.0.0)",
    "langchain-openai (>=1.1.7,<2.0.0)",
    "langchain (>=1.2.3,<2.0.0)"
]
```

---

## 🏃‍♂️ Como Executar os Projetos

```bash
# Módulo 1 - Prompt Packer
poetry run python modulo_1/main.py

# Módulo 2 - Chat Persistente
poetry run python modulo_2/main.py

# Módulo 3 - Calculadora de Custos
poetry run python modulo_3/main.py

# Módulo 4 - SDK de Modelos
poetry run python modulo_4/main.py

# Módulo 5 - Vector Store
poetry run python modulo_5/main.py

# Módulo 6 - ETL Dataset
poetry run python modulo_6/main.py

# Módulo 7 - Dashboard
poetry run python modulo_7/main.py

# Módulo 8 - CLI Assistant (requer OPENAI_API_KEY)
poetry run python modulo_8/main.py
```

---

## 👨‍💻 Autor

**Anwar Hermuche**

- Email: anwarhermuche2@gmail.com

---

<div align="center">

**⭐ Se este curso te ajudou, deixe uma estrela no repositório!**

</div>

