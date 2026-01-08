import pandas as pd

class ETL:

    def __init__(self, file_path: str):
        self.file_path = file_path
        self.data = self.load_data()

    def load_data(self) -> pd.DataFrame:
        return pd.read_csv(self.file_path)

    def normalize_sender(self, df: pd.DataFrame) -> pd.DataFrame:
        df["sender"] = df["sender"].str.lower()

        # Fazendo replace
        df["sender"] = df["sender"].str.replace("assistant", "ai")
        df["sender"] = df["sender"].str.replace("bot", "ai")
        df["sender"] = df["sender"].str.replace("cliente", "human")

        # Excluindo o que não for human ou ai
        df = df[df["sender"].isin(["human", "ai"])]
        return df

    def normalize_content(self, df: pd.DataFrame) -> pd.DataFrame:
        # Transformando o content em string
        df["content"] = df["content"].astype(str)

        # Filtrar PIIs (email, telefone, CPF)
        ## E-mail (regex completo)
        df = df[~df["content"].str.contains(r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}", regex=True)]
        
        ## Telefone (regex completo)
        df = df[~df["content"].str.contains(r"(?:\+?55\s?)?\(?\d{2}\)?\s?(?:9\d{4}|\d{4})[-\s]?\d{4}", regex=True)]
        
        ## CPF (regex completo)
        df = df[~df["content"].str.contains(r"\b\d{3}\.?\d{3}\.?\d{3}-?\d{2}\b", regex=True)]

        # Remover linhas com conteúdo muito curto (menos de 15 caracteres)
        df = df[df["content"].str.len() >= 15]
        
        # Remover tags HTML simples
        df = df[~df["content"].str.contains(r"<[^>]*>", regex=True)]
        
        # Remover espaços em branco
        df["content"] = df["content"].str.strip()
        
        # Remover quebras de linha
        df["content"] = df["content"].str.replace(r"\n", " ", regex=True)
        
        return df

    def normalize_created_at(self, df: pd.DataFrame) -> pd.DataFrame:
        # Corrigir/parsear created_at
        ## Aceitar múltiplos formatos
        df["created_at"] = pd.to_datetime(df["created_at"], errors="coerce")
        
        ## Descartar timestamps inválidos
        df = df[df["created_at"].notna()]
        return df

    def remove_duplicates(self, df: pd.DataFrame) -> pd.DataFrame:
        # Remover duplicatas óbvias (mesmo chat_id + sender + content)
        df = df.drop_duplicates(subset=["chat_id", "sender", "content"])
        return df

    def correct_conversation_flow(self, df: pd.DataFrame) -> pd.DataFrame:      
        ## Garantindo que não há buracos (exemplo de buraco: ["user", "assistant", "assistant"])
        ## Se houver buracos, descartar o grupo
        chat_ids = df["chat_id"].unique()
        ids_ok = []
        for chat_id in chat_ids:
            list_messages = df[df["chat_id"] == chat_id]['sender'].to_list()
            if len(list_messages)%2 != 0 or ['human', 'ai']*(int(len(list_messages)/2)) != list_messages:
                continue
            
            ids_ok.append(chat_id)
        df = df[df['chat_id'].isin(ids_ok)]
        return df

    def transform_data(self, df: pd.DataFrame) -> str:
        # Ordenar mensagens por chat_id e created_at
        df = df.sort_values(by=["chat_id", "created_at"])

        # Garantir que o fluxo de conversas esteja correto (sempre human->ai->human->ai)
        df = self.correct_conversation_flow(df)
        
        # Coloca no formato JSONL ({"messages":[{"role":"user","content":"..."},{"role":"assistant","content":"..."}]})
        jsonl_string = self.build_jsonl(df)

        return jsonl_string

    def build_jsonl(self, df: pd.DataFrame) -> str:
        # Coloca no formato JSONL ({"messages":[{"role":"user","content":"..."},{"role":"assistant","content":"..."}]})
        unique_ids = df['chat_id'].unique()
        jsonl_final = ""
        for id in unique_ids:
            messages_list = {"messages": []}
            values_sender_content = df[df['chat_id'] == id][['sender', 'content']].values
            for pair in values_sender_content:
                role = 'user' if pair[0] == 'human' else 'assistant'
                messages_list['messages'].append({'role': role, 'content': pair[1]})
            jsonl_final += str(messages_list) + "\n"
        return jsonl_final

    def export_data(self, jsonl_string: str) -> None:
        # Exportar para JSONL (mudar o nome do arquivo final para 'training_data.jsonl')
        ## Lembrar de mudar apenas o nome do arquivo final, não o caminho (caminho pega dinamicamenete do file_path)
        # Considerar até a última /
        file_path = self.file_path.split("/")[:-1]
        file_path = "/".join(file_path) + "/training_data.jsonl"
        with open(file_path, "w") as arquivo:
            arquivo.write(jsonl_string)

    def pipeline(self) -> pd.DataFrame:
        # Normalizando o sender
        df = self.normalize_sender(self.data)

        # Normalizando o content
        df = self.normalize_content(df)

        # Normalizando o created_at
        df = self.normalize_created_at(df)

        # Removendo duplicatas
        df = self.remove_duplicates(df)

        # Transformando os dados
        jsonl_string = self.transform_data(df)

        # Exportando os dados
        self.export_data(jsonl_string)

        return df