import pandas as pd
import numpy as np
# Series seria algo como o estrutura padrão mais básica do pandas

labels = ['a', 'b', 'c']
m_list = [10, 20, 30]
arr = np.average([1, 30, 2])
d = {'a': 10, 'b': 29, 'c': 40}

# Associar valores
series = pd.Series(data=m_list, index=labels)

#accesar valores
series['a']

series = pd.Series(m_list, labels)
series_arr = pd.Series(arr, labels)

ser1 = pd.Series([1,2,3,4], ["EAU", "Alemanha","Italia", "JAPAO"])
ser2 = pd.Series([4,3,2,1], ["EAU", "Alemanha","Italia", "JAPAO"])


#basicamente as Series é fazer operações baseadas em índice

print(ser1 + ser2)