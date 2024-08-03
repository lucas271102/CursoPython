numeros = [7,5,3,9,32]
#encontrando el numero mayor de una lista
numero_mas_alto = max(numeros)
print(numero_mas_alto)

#encontrando el numero menor de una lista
numero_mas_bajo = min(numeros)
print(numero_mas_bajo)


#redondeando a 6 decimales 

numero = round(12.4567,2)
print(numero)


#retorna False -> 0, vacio, false, none / True -> distinto a 0, True, cadena, datos no vacios
resultado_bool= bool(422)
print(resultado_bool)


#retorna true si todos los valores son verdaderos adentro de un iterable
resultado_all = all([432,"true",[322, 989]])
print(resultado_all)

#suma todso los valores de un iterable
suma_total = sum(numeros)
print(suma_total)