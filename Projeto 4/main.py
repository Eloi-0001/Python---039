import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("Projeto 4/train.csv")

df = df.drop_duplicates()

df['Age'] = df['Age'].fillna(df['Age'].mean())

conversao = df['Age'].astype('int64')

filtro_sobreviventes = df['Survived'] == 1
sobreviventes = df[filtro_sobreviventes]

f_morto = df['Survived'] == 0
mortos = df[f_morto]


# Boxplot que mostra a idade dos sobreviventes.

'''
plt.boxplot([mortos['Age'], sobreviventes['Age']], labels=['Mortos', 'Sobreviventes'])
plt.title('Idade por sobrevivência')
plt.ylabel('Idade')

plt.show()
'''

# histrograma que mostra a idade dos sobreviventes.

'''
sns.histplot(data=df, x='Age', hue='Survived', kde=True, bins=30, palette={0: 'red', 1: 'green'}, alpha=0.6)

plt.show()
'''

# Boxplot exibe o genero e a idade das pessoas que embarcaram no titanic.

'''
sns.boxplot(data=df, x='Sex', y='Age', hue='Sex')
plt.show()
'''