

#usando open para abrir un archivo con una codificacion universal (utf-8)
archivo_sin_leer = open("archivos//texto.txt")

#leer archivo completo
#archivo = archivo_sin_leer.read()

#leer linea por linea 
#lineas = archivo_sin_leer.readlines()

#leer una sola linea
linea = archivo_sin_leer.readline(89)

#cerrar el archivo 
archivo_sin_leer.close()
print(linea)