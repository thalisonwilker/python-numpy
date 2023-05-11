import numpy as np
import pandas as pd

data = {"col1": [1, 2, 3, 4], "col2": [444, 555, 666, 444],
        "col3": ['abc', 'def', 'ghi', 'xyz']}
df = pd.DataFrame(data)
df.head()

# verificar os valors únicos de uma coluna específica
df["col2"].unique()
df["col2"].value_counts()


# definir uma função para aplicar em cada elemento do dataframe

def s(x):
    return x * x


df["col2"].apply(s)  # equivalente ao map
df["col2"].apply(lambda x: x * 2)  # equivalente ao map


#deletar colunas
del df["col3"]

#buscar os valres das colunas
df.columns

#os indezes

df.index

#ordernar os valores
df.sort_values(by="col2")
df.sort_values(by=["col1", "col2"])

#buscar nulos
df.isnull()

#pivotear
