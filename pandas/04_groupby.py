import numpy as np
import pandas as pd

data = {
    "Empresa": ["GOOG", "GOOG", "MSFT", "MSFT", "FB", "FB"],
    "Nome": ["Sam", "Charlie", "Amy", "Vanessa", "Carl", "Saraf"],
    "Vendas": [200, 120, 340, 124, 243, 350]
}

df = pd.DataFrame(data)

#Criação do grupo
group = df.groupby("Empresa")
group_names = df.groupby("Nome")

group_names.sum()
group.describe()