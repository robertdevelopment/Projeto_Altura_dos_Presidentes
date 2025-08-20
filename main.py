import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
sns.set()

dados = pd.read_csv('president_heights.csv')
print(dados)

altura = (dados["height(cm)"])
print(altura)

print("Médias das Alturas =", altura.mean())
print("Desvio padrão da Altura =", altura.std())
print("Altura mínima =", altura.min())
print("Altura máxima =", altura.max())
print("Mediana", np.median(altura))

plt.hist(altura)
plt.title('Distribuição das Alturas dos Presidentes')
plt.xlabel('Altura (cm)')
plt.ylabel('Número')
plt.show()


