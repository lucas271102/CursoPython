import pandas as pd
#df = dataframe
#usando la funcion read_csv para leer el archivo csv

df = pd.read_csv("archivos//datos.csv", names=["name", "lastname", "age"])
nombres = df["name"]
#utilizando metodo slicing para hayar caracteres de un string 

cadena = "0123456789"

#ordenando el dataframe por edad
df_ordenado = df.sort_values("age")

#ordenando de forma descendente
df_ordenado_al_reves = df.sort_values("age", ascending=False)
print(df_ordenado_al_reves)
#print(df_ordenado)
#print(cadena[0:5])