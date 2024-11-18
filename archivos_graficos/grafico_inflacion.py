import pandas as pd 
import matplotlib.pyplot as plt
import seaborn as sns 
from flask import Flask, send_file

dfv = pd.read_csv("archivos_graficos//inflacion.csv")
estadisticas = dfv['Variación mensual'].describe()
print(estadisticas.round(1))

#sns.lineplot(x="Mes", y="Ventas", data=dfv )
sns.barplot(x="Mes", y="Variación mensual", data=dfv )
plt.title('Inflacion dic23 - oct24')
plt.savefig('archivos_graficos/graficoinflacion.png')
plt.show()

