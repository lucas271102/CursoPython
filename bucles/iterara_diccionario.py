diccionario = {
    "nombre" : "lucas", 
    "edad" : "21",
    "destino":"Michigan"
    }

#recorriendo el diccionario para obtener las key
for key in diccionario:
    print(key)

#recorriendo el diccionario con items() para obtener las claves y los valores 
for datos in diccionario.items():
    key = datos[0]
    value = datos[1]
    print(f"la clave es {key} y el valor es {value}")