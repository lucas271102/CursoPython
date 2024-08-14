with open('archivos//texto.txt', 'a', encoding="UTF-8") as archivo:
    #usando un bucle para agregar varias lineas
    for i in range(5):
        archivo.write(f"Esta es la linea {i+1}\n")