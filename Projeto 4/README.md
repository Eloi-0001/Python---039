````markdown
# 📘 Projeto 4 - Análise de Sobrevivência no Titanic

## 🔍 Objetivo

Este projeto tem como objetivo analisar os dados dos passageiros do Titanic para entender possíveis padrões relacionados à **idade**, **sexo** e **taxa de sobrevivência**. Foram utilizados gráficos estatísticos como **boxplots** e **histogramas com densidade (KDE)** para visualizar essas relações.

---

## 📁 Dados

Os dados estão no arquivo `train.csv` e contêm os seguintes campos relevantes:

- `Survived`: 0 = Não sobreviveu, 1 = Sobreviveu
- `Age`: Idade dos passageiros
- `Sex`: Sexo dos passageiros

---

## ⚙️ Pré-processamento

```python
df = pd.read_csv("train.csv")
df = df.drop_duplicates()
df['Age'] = df['Age'].fillna(df['Age'].mean())
```
````

- Remoção de duplicatas.
- Preenchimento de valores nulos em `Age` com a média das idades.

---

## 📊 Visualizações

### 1. Boxplot - Idade por Sexo

```python
sns.boxplot(data=df, x='Sex', y='Age', hue='Sex')
```

![Boxplot por Sexo](./graficos/kde.png)

**Conclusões:**

- Mulheres embarcaram, em média, um pouco mais jovens que os homens.
- A distribuição de idade é similar, com outliers mais comuns entre homens.

---

### 2. Boxplot - Idade por Sobrevivência

```python
plt.boxplot([mortos['Age'], sobreviventes['Age']], labels=['Mortos', 'Sobreviventes'])
```

![Boxplot por Sobrevivência](./graficos/kde1.png)

**Conclusões:**

- Idade média semelhante entre mortos e sobreviventes.
- Crianças e jovens tendem a ter maior chance de sobrevivência.

---

### 3. Histograma com KDE - Idade e Sobrevivência

```python
sns.histplot(data=df, x='Age', hue='Survived', kde=True, bins=30, palette={0: 'red', 1: 'green'})
```

![Histograma de Idade](./graficos/kde2.png)

**Conclusões:**

- A maioria dos passageiros estava entre 20 e 40 anos.
- Leve vantagem de sobrevivência para crianças e adultos jovens.
- A curva verde (sobreviventes) é mais proeminente entre 0–15 e 30–40 anos.

---

## 📈 Conclusões Gerais

- Mulheres possuíam maior taxa de sobrevivência (a ser explorado diretamente em análises futuras).
- Idade não foi um fator determinante, mas passageiros mais jovens apresentaram leve vantagem.
- Outliers de idade (acima de 60 anos) eram raros e geralmente não sobreviveram.

---

## 📚 Bibliotecas Utilizadas

- `pandas`
- `matplotlib`
- `seaborn`

---

## 🛠️ Melhorias Futuras

- Incluir variáveis como `Sex`, `Pclass` e `Fare` na análise.
- Explorar modelos de machine learning para prever sobrevivência.
- Gerar gráficos interativos com Plotly.

---
