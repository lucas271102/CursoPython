import pandas as pd
#cambiar el tiopo de dato de una columna
df = pd.read_csv("archivos//datos.csv")

#convertir a string los datos de una columna 
df['edad'] = df['edad'].astype(str)


#mostrar el tipo de dato del primer elemento de la columna edad 
#print(type(df['edad'][0]))


#reemplazando datos 
df['apellido'].replace("lopez", "speziale", inplace=True)
print(df['apellido'])
