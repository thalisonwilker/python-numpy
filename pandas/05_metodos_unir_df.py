import numpy as np
import pandas as pd

# Concatenação basicamente cola DataFrames. é importante ter em mente que as dimensões devem corresponder ao longo do eixo será concatenado. a função é pd.concat

# ex: pd.concat([df1, df2, df3])
# é possivel definir onde a união será feita: por padrão o eixo0
# ex: pd.concat([df1, df2, df3], axis=1)

# as uniões sempre sempre feitas em colunas com o mesmo nome

#Outros Dataframes
# A função mesclar permite mesclar os quadros de dados juntos utilizando uma lógica semelhante à mesclagem de tabelas SQL juntas.
#Unir dataframes que compartilham algum dado em comum

# pd.merge(df_left, df_right, how="inner", on="key") 
## especificando os parametros de do df
## how: é o método de união de tabelas SQL
## on: especificar pela coluna chave, ou várias chaves, ex: on=["key1", "key2"]

#Join: juntar DataFrames que potencialmente podem ter algumas diferenças entre alguns do teus indices

# df_left.join(df_right)
# o argumento how="outer"

