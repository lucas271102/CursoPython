#creando una funcion que devuelva nukeros primos
#entre 0 y el argumento que le pasemos

#crear una funcion que verifique si un numero es primo 
def es_primo(num):
    #verificamos que el numero pasado no puede dividirse
    #por ningun otro numero entre 2 y es mimso numero -1
    for i in range(2, num - 1):
        #si es divisible por alguno retornamos false y termina el bucle
        if num %i == 0: return False
    #si termina el bucle, significa que no fue divisible entonces es primo 
    return True


#creando funcion que retorne una lista con todos los numeros primos
def primos_hasta(num):
    #creandoi la lista 
    primos = []
    for i in range(3, num +1 ):
        #verificamos si el valor es primo 
        resultado = es_primo(i)
        #en caso de que sea primo, se agrega a la lista 
        if resultado == True: primos.append(i)
    #devolvemos la lista 
    return primos
#creamos el resultado llamando a la funcion y lo mostramos
resultado = primos_hasta(98)
print(resultado)
        
#creando una funciion que devuelva una lista
#con todos los numeros perfectos entre 1 y el argumento que le pasemos
def perfectos_hasta(num):
    perfectos = []
    for i in range(1, num + 1):
        suma_divisores= 0
        for j in range(1, i):
          if i % j == 0 :
           suma_divisores+= j
        if suma_divisores== i :
            perfectos.append(i)
    return perfectos

son_perfectos = perfectos_hasta(898)
print(son_perfectos)