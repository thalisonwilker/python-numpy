import numpy as np
import pandas as pd

# DataFrames: é o objeto principal do Pandas que utiliza um conjunto de Series

# Definie um seed para o random
np.random.seed(101)

# Criação de um dataframe
df = pd.DataFrame(data=np.random.randn(5, 4), index="A E I O U".split(
), columns="X Z Y Z".split(), dtype=None, copy=False)

# acessar uma coluna de dados
df["X"]

# Acessar algumas colunas
df[["X", "Y"]]

# criar colunas novas
df["K"] = df["X"] + df["Y"]

# apagar
df.drop('K', axis=1)  # não modifica o DataFrame original

# modifica diretamente o DataFrame
#ff = df.drop('K', axis=0)
# ou
df.drop('K', axis=1, inplace=True)

#Localização de elementos via index
df.loc['A']

#Localizar uma seleção
#df.loc[ ['X', 'Y'], ['X', 'Y'] ]
