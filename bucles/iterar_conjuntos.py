animales = {"perro", "gato", "loro", "cocodrilo"}
numeros = {23,45,43,67}
    
#recorriendo el conjunto animales 
for animal in animales:
    print(f"Ahora la varibale animal es igual a {animal}")
    
    
#recorriendo  el conjunto numeros y multiplicando cada valor por 10 
for numero in numeros:
    resultado = numero * 10 
    print(f"El resultado de multiplicar {numero} por 10 es {resultado}")
    
    
    
#recorriendo los dos conjuntos del mimso tamaño al mismo tiempo
for animal,numero in zip(animales,numeros):
    print(f"El animal es {animal} y el nunmero es {numero}")    

    
#forma correcta de recorrer un conjunto
for num in enumerate(numeros):
    print(num)
    
#otra forma para obtener el indice de un conjunto
for num in enumerate(numeros):
    indice = num[0]
    valor = num[1]
    print (f'el indice es {indice} y el valor es {valor}')
    
    
#usando el for/else 
for numero in numeros:
    print(f"ejecutando el ultimo loop, valor actual:{numero}")
else:
    print("el bucle terminó")