numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9]

# Creando una función lambda que multiplica por 2
multiplicar_por_dos = lambda x: x * 2
print(multiplicar_por_dos(5))

# Creando una función que diga si el número es par o no
#def es_par(num):
 #   if num % 2 == 1:
  #      return True
   # else:
    #    return False

# Usando filter con una función común
#numeros_pares = list(filter(es_par, numeros))

#creando lo mismo pero con lambda
numeros_pares = filter(lambda numero : numero%2 == 0, numeros)
print(list(numeros_pares))