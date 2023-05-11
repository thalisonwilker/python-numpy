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
# ff = df.drop('K', axis=0)
# ou
df.drop('K', axis=1, inplace=True)

# Localização de elementos via index
df.loc['A']

# Localizar uma seleção
# df.loc[ ['X', 'Y'], ['X', 'Y'] ]


# Seleção condicional de series

# so campos maiores que 0
df > 0

bol = df > 0

# DataFrame do mesmo tamanho com NaN nos lugares dos valores testados
df[bol]

# retorna os valores da coluna X que são maiores que 0
df[df["X"] > 0]

# o resultado da condicional é um DataFrame, também é possível realizar um slice no resultado
# Recuperar os valores da coluna Y cujo os valores da coluna X são maiores que 0
df[df["X"] > 0]["Y"]

# passo a passo
bol = df["X"] > 0
df2 = df[bol]
df2["Y"]

# filtros condicionais baseados em múltiplas condições

# df[ (df["X"] > 0) and (df["Y"] > 1) ] comparação direta com 'and' dá erro

df[(df["X"] > 0) & (df["Y"] > 1)]  # utiliza o operador de simbolo


# reseta o indece para as configurações padrão
df.reset_index()
# para persistir no DataFrame original
df.reset_index(inplace=True)


col = "PA BA RJ MT AL".split()  # precia ter o mesma quantidade de item do indice

df["Estados"] = col

# Utizar os estados como Index no df
df.set_index("Estados")

# Indice Multiníveis
outside = ['G1', 'G1', 'G1', 'G2', 'G2', 'G2']
inside = [1, 2, 3, 1, 2, 3]
hier_index = list(zip(outside, inside))  # hierarquia de index
# criar um objeto de índice multinível
hier_index = pd.MultiIndex.from_tuples(hier_index)

#Criação de um DataFrame multinívels
df = pd.DataFrame(np.random.randn(6, 2), index=hier_index, columns=['A', 'B'])

#Acessar os dados

df.loc["G1"].loc[1]

df.index.names = ["Grupo", "Numeros"] # nomeando os indexes

#processtion
df.xs('G1')

#Acessar os números do grupo interno
print(df.xs(1, level="Numeros"))