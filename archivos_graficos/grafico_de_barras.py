import csv 
import matplotlib.pyplot as plt
fuente = ["Trabajo fijo", "Freelance", "Youtube", "Influencer", "Criptomonedas"]

ingresos = [3000, 2000, 450, 375, 100]

#escribir en un nuevo archivo csv 
with open ('archivos_graficos/ingresos.csv', 'w', newline='') as archivo_csv:
    writer = csv.writer(archivo_csv)
    writer.writerow(['Fuente', 'Ingresos'])
    for mes, var in zip(fuente, ingresos):
        writer.writerow([mes, var])
        
colors = ['red' if v > 8.8 else 'blue' for v in ingresos]

 #Plotting
plt.figure(figsize=(10, 5))
plt.bar(fuente, ingresos, color=colors)

# Adding exact numbers on the left side of the bars
for i, v in enumerate(ingresos):
    plt.text(i, v + 0.5, str(v), ha='center')  # Adjust the position as needed

plt.title('Ingresos')
plt.xlabel('Fuente')
plt.ylabel('Ingresos')
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig('archivos_graficos/ingresos.png')


plt.show()