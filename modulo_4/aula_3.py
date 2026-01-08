from dotenv import load_dotenv
import os

# Carregando as variáveis de ambiente
load_dotenv()

# Acessando a variável de ambiente
API_KEY = os.getenv("API_KEY")
print(API_KEY)
