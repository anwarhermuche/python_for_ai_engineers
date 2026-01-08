import matplotlib.pyplot as plt

class DashboardPlotter:

    def __init__(self, output_path: str = "./modulo_7/dashboard.png"):
        self.output_path = output_path

    def plot_histogram(self, lengths: list[int], title: str) -> None:
        plt.hist(lengths, bins=10)
        plt.title(title)
        plt.savefig(self.output_path)

    def plot_bar(self, topic_counts: dict[str, int], title: str) -> None:
        plt.bar(topic_counts.keys(), topic_counts.values())
        plt.title(title)
        plt.savefig(self.output_path)

    def save_dashboard(self, lengths: list[int], topic_counts: dict[str, int]) -> None:
        # Criando a figura
        
        # Criando o primeiro subplot
        plt.figure(figsize=(10, 5))
        plt.subplot(1, 2, 1)

        # Plotando o histograma
        self.plot_histogram(lengths, "Distribuição de tamanho das perguntas")

        # Criando o segundo subplot
        plt.subplot(1, 2, 2)

        # Rotacionando as labels do eixo x
        plt.xticks(rotation=45)

        # Plotando o gráfico de barras
        self.plot_bar(topic_counts, "Frequência de tópicos")
        
        # Salvando a figura
        # Ajustando o layout das subplots
        plt.tight_layout()
        plt.savefig(self.output_path)