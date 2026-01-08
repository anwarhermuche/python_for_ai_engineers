from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from tools import get_current_time, count_words_in_phrase
from langchain.agents import create_agent
from langchain_core.messages import SystemMessage,HumanMessage, AIMessage, ToolMessage, AnyMessage

load_dotenv()

class CLIAssistant:

    def __init__(self, model: str, system_prompt: str, history_path: str):
        self.history_path = history_path
        self.model = model if model.startswith("openai:") else f"openai:{model}"
        self.history = self.load_history()
        self.system_prompt = system_prompt
        self.agent = create_agent(self.model, tools = [get_current_time, count_words_in_phrase])

    def load_history(self) -> list[AnyMessage]:
        with open(self.history_path, "r") as f:
            messages = f.read().split("\n")
        
        new_messages = []
        for message in messages:
            if message.startswith("human:"):
                new_messages.append(HumanMessage(content=message.split(": ")[1]))
            elif message.startswith("ai:"):
                new_messages.append(AIMessage(content=message.split(": ")[1]))

        return new_messages

    def save_message(self, sender: str, content: str) -> None:
        with open(self.history_path, "a") as f:
            f.write(f"{sender}: {content}\n")

    def message_agent(self, human_message: AnyMessage) -> str:
        # Obtendo histórico 
        history = [SystemMessage(content=self.system_prompt)] + self.history + [human_message]
        history_dict = {"messages": history}
        response = self.agent.invoke(history_dict)
        
        # Salvando a mensagem do humano e a resposta do agente
        self.save_message("human", human_message.content.replace('\n', ' '))
        self.save_message("ai", response['messages'][-1].content.replace('\n', ' '))
        
        return response['messages'][-1].content

    # Enviando mensagem para o agente

    def run(self) -> None:
        print("Histórico:")
        for message in self.history:
            print(f"{message.type}: {message.content}")
        print("--------------------------------\n")

        while True:
            user_input = input("Você: ")
            if user_input == "/stop":
                break
            human_message = HumanMessage(content=user_input)
            response = self.message_agent(human_message) 
            print(f"AI: {response}")
            