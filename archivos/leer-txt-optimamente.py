
#abriendo el archivo con with open 
with open("archivos//texto.txt") as archivo:
    
    #leemos el archivo
    contenido = archivo.read()
    
    #mostramos el archivo 
    print(contenido)