diccionario = {
    "nombre": "lucas",
    "puesto": "lift operator",
    "destino":"thomsponville, mi",
    "edad": 21
}
#nos devuelve un objeto iterable
claves = diccionario.keys()
#obtenemos un dato de una clave con get()
obtener_datos= diccionario.get("edad")

#eliminando todos los elementos del diccionario 
#eliminar_diccionario = diccionario.clear()


#eliminando un elemento del diccionario 
diccionario.pop("nombre")

#obteniendo un elemento dict_items iterable 
diccionario_iterable = diccionario.items()


print(diccionario)