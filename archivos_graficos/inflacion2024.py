import csv 
import matplotlib.pyplot as plt
meses = ["Dic23", "Ene24", "Feb24", "Mar24", "Abr24", "May24", "Jun24", "Jul24", "Ago24", "Sept24", "Oct24", "Nov 24", "Dic24", "Ene 25", "Feb25", "Mar 25", "Abr 25", "May25", "Jun25"]

variacion = [25.5, 20.6, 13.2,11 , 8.8, 4.2, 4.6, 4.0, 4.2, 3.5, 2.7, 2.4, 2.8, 2.5, 2.2, 3.7, 2.4, 1.5, 1.6]

#escribir en un nuevo archivo csv 
with open ('archivos_graficos/inflacion.csv', 'w', newline='') as archivo_csv:
    writer = csv.writer(archivo_csv)
    writer.writerow(['Mes', 'Variación mensual'])
    for mes, var in zip(meses, variacion):
        writer.writerow([mes, var])
        
colors = ['red' if v > 8.8 else 'blue' for v in variacion]

 #Plotting
plt.figure(figsize=(10, 5))
plt.bar(meses, variacion, color=colors)

# Adding exact numbers on the left side of the bars
for i, v in enumerate(variacion):
    plt.text(i, v + 0.5, str(v), ha='center')  # Adjust the position as needed

plt.title('Inflación Mensual 2024')
plt.xlabel('Mes')
plt.ylabel('Variación mensual (%)')
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig('archivos_graficos/ipc.png')
plt.show()