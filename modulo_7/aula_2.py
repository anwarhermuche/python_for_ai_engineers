# Analisando distribuições e outliers
import matplotlib.pyplot as plt
numero_de_tokens = [90875, 87495, 92494, 88473, 91473, 89473, 93473, 87473, 92473, 88473, 82000]

## Histograma
plt.hist(numero_de_tokens)
plt.show()

## Boxplot
plt.boxplot(numero_de_tokens)
plt.show()