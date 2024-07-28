cadena1 = "Hola, soy, Lucas"
cadena2 = "Bienvenido"
cadena3 = "35234523"
#dir = funcion 
#convierte a mayuscula
mayus = cadena1.upper()
#convierte a minuscula 
minus = cadena1.lower()

#primer letra en mayuscula 
primera = cadena1.capitalize()

#buscar una cadena en otra cadena, si no hay coincidencias, devuelve -1
busqueda = cadena1.find("soy")

#el metodo index encuentra la primera aparicion del calor especificado, sino muestra una excepcion 
busqueda_index = cadena1.index("s")

#si es numerico devuelve true 
es_numerico = cadena3.isnumeric()

# si es alfanumerico devolvemos true 
es_alfanumerico = cadena1.isalpha()

#contar la cantidad de veces que aparece un caracter o numero 
contar = cadena1.count("L")

#contamos cuantos carcteres tiene unda cadena, es una FUNCIÓN, no un metodo
contar_caracteres = len(cadena1)

#verifica si una cadena empieza con otra cadena dada , si es asi devuelve TRUE 
empieza_con = cadena1.startswith("H")

#verifica si una cadena termina con otra cadena dada, si es asi devuelve TRUE 
termina_con =  cadena1.endswith("cas")

#reemplaza un pedazo de la cadena dada, por otra. cadena1.replace(valor anterior, valor nuevo), 
# si el valor 1 se encuentra en la cadena original , 
# reemplaza el valor 1 de la misma por el valor 2
cadena_nueva = cadena1.replace("Hola", "Como estas")

#separar cadenas con la cadena que le pasemos 
cadena_separada = cadena1.split(",")

print (cadena_separada[2])