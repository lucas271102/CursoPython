#creando un a lista con list 
lista = list ([232, 253,387, 19, 3452])
#ahora nos va a devolver la cantidad de elementos y no de caracteres 
cantidad_elementos  = len(lista)

#agregando un elemtno a la lista APPEND
lista.append(90)

#agregando un elemento a la lista con el meetodo INSERT A UN INDICE ESPECIFICO

lista.insert(2, 45)

#agregando varios elementos a la lista 
lista.extend([43, 23])

#eliminando un elemento de la lista por su indice 
lista.pop(-2)

#removiendo un elemento de la lista por su valor 
lista.remove(232)

#elimina todos los elemntos de una lista 
#lista.clear()

#funcion que ordena los elemtnos de manera ascendente 
#si usamos reverse = true, los ordena al reves.
lista.sort()

#verificando si un elemento se enecuentra en la lista. elementos completos 
elemento_encontrado = lista.index(3452)
print (elemento_encontrado)