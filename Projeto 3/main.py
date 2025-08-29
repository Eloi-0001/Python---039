import pandas as pd
import plotly.express as px
import matplotlib as plt
import func as funcao

dados = pd.read_csv("Projeto 2/dados.csv")

plt.plot(dados)
plt.show()