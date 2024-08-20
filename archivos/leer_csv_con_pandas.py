import pandas as pd
#df = dataframe
#usando la funcion read_csv para leer el archivo csv

df = pd.read_csv("archivos//datos.csv")
print(df["nombre"]) 