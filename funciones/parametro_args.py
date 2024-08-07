
#forma no optima de sumar valores
#def suma (lista):
 #   numeros_sumados= 0
  #     numeros_sumados = numeros_sumados + numero
   #     return numeros_sumados
    
#esultado = suma([32,45,6,7,8,76])
#print(resultado)

#utilizando el parametro args
def suma (nombre, *numeros):
    return f"{nombre}, tu dia de nacimiento fue {sum(numeros)}"
resultado = suma("Lucas", 13,14)
print(resultado)