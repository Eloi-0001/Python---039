import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import numpy.random as rannp
from scipy.stats import norm

dados = pd.read_csv("Projeto 3/dados.csv")

media = dados['price'].mean()
moda = dados['price'].std()

espaçamento = np.linspace(
        media - 4 * moda,
        media + 4 * moda,
        1000,
    )
densidade = norm.pdf(espaçamento, media, moda)

plt.plot(espaçamento, densidade)
plt.show()