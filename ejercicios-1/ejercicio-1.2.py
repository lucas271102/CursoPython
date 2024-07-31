#ejercicio 2 
#a) pedirle al usuario que diga cualquier texto real y: 
      #- calcular cuanto tardaria en  decir esa frase 
      #- cuantas palabras dijo ?
#b) si se tarda mas de 1 minuto decirle "mucho texto"

# dalto habla un 30% mas rapido, cuanto taradaria en decirlo ?

#le pedimos al usuario que diga una o varias frases 
frase = input ("Decime una frase y te digo cuanto tardarías si tuvieras que decirla:")

#creamos una lista con todas las palabras de la frase 
palabras_separadas = frase.split(" ")

#usamos len para saber la cantidad de elementos que hay en la lista 
cantidad_de_palabras= len(palabras_separadas)

#en caso de que tarde mas de un minutoen decirlo, le decimos que es mucho texto 
if cantidad_de_palabras > 120 :
    print("Mucho texto")

#calculamos cuanto tardaría en decri las palabras y lo imprimimos 
print (f'Dijiste {cantidad_de_palabras} palabras, y tardarias {cantidad_de_palabras/2} segundos en decirlas')
print(f'Dalto lo diria en {cantidad_de_palabras * 100 // 2 * 1.3 / 100} segundos ')