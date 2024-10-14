import pandas as pd 
import matplotlib.pyplot as plt
import seaborn as sns 

dfv = pd.read_csv("archivos_graficos//ventas.csv")
print(dfv)

#sns.lineplot(x="Mes", y="Ventas", data=dfv )
sns.barplot(x="Mes", y="Ventas", data=dfv )
plt.show()
