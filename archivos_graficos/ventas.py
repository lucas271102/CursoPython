import csv 
meses = ["Ene", "Feb", "Mar", "Abr", "May", "Jun", "Jul", "Ago", "Sept", "Oct", "Nov", "Dic"]

ventas = [150, 200, 220, 240, 280, 300, 450, 320, 600, 250, 900, 290]

#escribir en un nuevo archivo csv 
with open ('archivos_graficos/ventas.csv', 'w', newline='') as archivo_csv:
    writer = csv.writer(archivo_csv)
    writer.writerow(['Mes', 'Ventas'])
    for mes, venta in zip(meses, ventas):
        writer.writerow([mes,venta])