import pandas as pd
df = pd.read_csv('archivos/datos.csv')

# Obtiene un resumen estadístico de la columna 'edad'
estadisticas = df['edad'].describe()

print(estadisticas.round(1))