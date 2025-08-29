import pandas as pd
import plotly.express as px
import matplotlib.pyplot as plt
import func as funcao

dados = pd.read_csv("Projeto 3/dados.csv")

anus = dados['year']

plt.hist(x='anus')
plt.show()
