import numpy as np
import pandas as pd

d = {"A": [2, 3, np.nan], "B": [5, np.nan, np.nan], "C": [1, 2, 3]}
df = pd.DataFrame(d)

# exclui valores
df.dropna()

# exclui valores nas linhas, as quais as linhas possuem uma determinada quantidade de valores faltantes
df.dropna(thresh=2)

# subsitui os valores por alguma coisa
df.fillna(value="FALROU")
# preenche os valores com a média dos valores de A
df.fillna(value=df["A"].mean())

df.fillna(method="ffill") # foward fill: preenche os valores com os valores anteriores

