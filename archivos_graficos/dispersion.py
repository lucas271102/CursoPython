import csv 

meses = ["Dic23", "Ene24", "Feb24", "Mar24", "Abr24", "May24", "Jun24", "Jul24", "Ago24", "Sept24", "Oct24"]

variacion = [25.5, 20.6, 13.2,11 , 8.8, 4.2, 4.6, 4.0, 4.2, 3.5, 2.7]

#escribir en un nuevo archivo csv 
with open ('archivos_graficos/dispersion.csv', 'w', newline='') as archivo_csv:
    writer = csv.writer(archivo_csv)
    writer.writerow(['Mes', 'Variación mensual'])
    for mes, var in zip(meses, variacion):
        writer.writerow([mes, var])