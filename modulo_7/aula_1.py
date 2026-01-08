# Matplotlib

import matplotlib.pyplot as plt

## Configurando título
plt.title("Número de tokens gerados por modelo")

## Gerando gráfico de barras & Linha
plt.bar(['gpt-5.1', 'gemini-2.5-flash', 'grok-4-reasoning', 'claude-4.5-opus'], [90875, 87495, 92494, 88473])

## Configurando labels (eixos)
plt.xlabel("Modelo")
plt.ylabel("Tokens gerados")

## Intervalo do eixo y
plt.ylim(0, 100_000)

## Salvando o gráfico
plt.savefig("tokens_por_modelo.png")

## Mostrando o gráfico
plt.show()
