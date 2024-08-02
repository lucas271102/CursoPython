animales = ["perro", "gato", "loro", "cocodrilo"]
numeros = [23,45,43,67]
    
#el programa se ejecuta cuantas variables haya 
for animal in animales:
    print(f"Ahora la varibale animal es igual a {animal}")
    
    
#recorriendo la conjuntos numeros y multiplicando cada valor por 10 
for numero in numeros:
    resultado = numero * 10 
    print(f"El resultado de multiplicar {numero} por 10 es {resultado}")
    
    
    
#recorriendo las dos conjuntoss del mimso tamaño al mismo tiempo
for animal,numero in zip(animales,numeros):
    print(f"El animal es {animal} y el nunmero es {numero}")    

#forma no optima de recorrer una conjuntos 
for num in range(len(numeros)):
    print(numeros[num])
    
    
#forma correcta de recorrer una conjuntos 
for num in enumerate(numeros):
    print(num)
    
#otra forma para obtener el indice de una conjuntos 
for num in enumerate(numeros):
    indice = num[0]
    valor = num[1]
    print (f'el indice es {indice} y el valor es {valor}')
    
    
#usando el for/else 
for numero in numeros:
    print(f"ejecutando el ultimo loop, valor actual:{numero}")
else:
    print("el bucle terminó")