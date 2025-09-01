import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("Projeto 4/train.csv")

df = df.drop_duplicates()

df['Age'] = df['Age'].fillna(df['Age'].mean())

conversao = df['Age'].astype('int64')

print(conversao)

df.info()




