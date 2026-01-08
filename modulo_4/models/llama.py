from models.base import ModeloBase
import time
from dotenv import load_dotenv
import os

load_dotenv()
LLAMA_API_KEY = os.getenv("LLAMA_API_KEY")

class LlamaModel(ModeloBase):
    def __init__(self, nome: str, temperatura: float):
        super().__init__(nome, temperatura)

    def invoke(self, prompt: str, api_key: str = LLAMA_API_KEY) -> str:
        if not api_key.startswith("sk-"):
            raise ValueError("API Key inválida")
        
        time.sleep(3)
        return {"model": f"{self.nome}", "output": "Resposta da Llama", "temperatura": self.temperatura}