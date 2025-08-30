import pandas as pd
import matplotlib.pyplot as plt

dados = pd.read_csv("Projeto 3/dados.csv")

preco = dados['price'].sort_values()

plt.boxplot(preco)
plt.ylabel('Valor dos carros')
plt.title('Preços dos carros')

plt.show()
