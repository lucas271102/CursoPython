import csv 
meses = ["Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio", "Julio", "Agosto", "Septiembre", "Octubre", "Noviembre", "Diciembre"]

ventas = [150, 200, 220, 240, 280, 300, 450, 320, 600, 250, 900, 290]

#escribir en un nuevo archivo csv 
with open ('ventas.csv', 'w', newline='') as archivo_csv:
    writer = csv.writer(archivo_csv)
    writer.writerow(['Mes', 'Ventas'])
    for mes, venta in zip(meses, ventas):
        writer.writerow([mes,venta])