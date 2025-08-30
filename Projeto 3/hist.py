import pandas as pd
import matplotlib.pyplot as plt

dados = pd.read_csv("Projeto 3/dados.csv")


plt.hist(dados['price'], color='skyblue')
plt.title('Preços dos carros.')
plt.xlabel('Preços')
plt.ylabel('carros totais')
plt.show()
