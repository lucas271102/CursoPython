import pandas as pd
#df = dataframe
#usando la funcion read_csv para leer el archivo csv

df = pd.read_csv("archivos//datos.csv")


df2 = pd.read_csv("archivos//datos.csv")
#obteniendo los datos de la columna nombres
nombres = df["nombre"]

#utilizando metodo slicing para hayar caracteres de un string 

#cadena = "0123456789"

#ordenando el dataframe por edad
#df_ordenado = df.sort_values("edad")

#ordenando de forma descendente
#df_ordenado_al_reves = df.sort_values("edad", ascending=False)


#concatenando los dos dataframes
df_concatenado = pd.concat([df, df2])

#accediendo a la primeras 3 filas con head()
primeras_fila = df.head(3)

#accediendo a las ultimas 3 filas con tail()
ultimas_filas = df.tail(3)

#accediendo a la cantidad de filas y columnas con shape
filas_columnas = df.shape
filas_totales = filas_columnas[0]
columnas_totales = filas_columnas[1]

#obteniemdo datos estadisticos del dataframe
df_stats = df.describe()


print(df_stats)
#print(df_concatenado)
#print(df_ordenado)
#print(cadena[0:5])