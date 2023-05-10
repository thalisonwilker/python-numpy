import numpy as np

arr = np.arange(0, 30, 3)

# recuperar um index
arr[0]

# recuperar multiplos elementos
arr[2:4]

# recueprar a partir do zero até
arr[:5]

# recuperar a partir do zero
arr[2:]

# atribuição em múltiplos indices
arr[2:] = 10

# array bidimencional

arr = np.arange(50).reshape((5, 10))

arr.shape

#slice
arr[:3][:]


# onde que a condição se satisfaz
bol = arr > 50

# recuperar os valores
print(arr[bol])

#extração
arr[2:3, 5]
