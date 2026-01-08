import json

class DatasetReader:

    def __init__(self, jsonl_path: str):
        self.jsonl_path = jsonl_path

    def load_conversations(self) -> list[dict]:
        dados = []

        with open(self.jsonl_path, 'r', encoding='utf-8') as f:
            for linha in f:
                # Ignora linhas em branco, se houver
                if linha.strip():
                    dados.append(json.loads(linha))
        
        return dados

    def extract_user_texts(self) -> list[str]:
        conversations = self.load_conversations()
        user_texts = []
        for conversation in conversations:
            for message in conversation["messages"]:
                if message["role"] == "user":
                    user_texts.append(message["content"])
        return user_texts