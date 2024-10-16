import pandas as pd 
import matplotlib.pyplot as plt
import seaborn as sns 
from flask import Flask, send_file

dfv = pd.read_csv("archivos_graficos//ventas.csv")
print(dfv)

#sns.lineplot(x="Mes", y="Ventas", data=dfv )
sns.barplot(x="Mes", y="Ventas", data=dfv )
plt.title('Informe de ventas del año 2023')
plt.savefig('archivos_graficos/grafico.png')
plt.show()
