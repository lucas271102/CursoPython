#creandom diccionarios con dict
diccionario = dict(nombre = "lucas", apellido = "speziale")

#las listas no pueden ser claves, las tuplas si 
diccionario= {("lucas", "speziale"):"jajaja"}


#creando diccionarios con fromkeys(), que es un metodo de diccionario,  valor por defecto : none 

diccionario = dict.fromkeys("nombre", "apellido") #el primer valor es iterable 

#creando diccionarios con fromkeys()  cambiando el valor por defecto a "no se"

diccionario = dict.fromkeys(["nombre", "apellido"], "no se")


print(diccionario)