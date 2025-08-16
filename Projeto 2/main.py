import pandas as pd

dados = pd.read_csv("Projeto 2/dados.csv")




filtro_atomatico = dados['transmission'] == "Automatic"
filtro_manual = dados['transmission'] == "Manual"
