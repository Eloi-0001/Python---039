import pandas as pd

dados = pd.read_csv("Projeto 2/dados.csv")


print(dados[dados['transmission'] == "Automatic"])
