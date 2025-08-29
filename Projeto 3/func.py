import pandas as pd
dados = pd.read_csv("Projeto 3/dados.csv")


def exibir(lista: list):
    for lista_organizada in lista:
        print(dados[lista_organizada].value_counts())
