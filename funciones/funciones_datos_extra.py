
#creando la misma funcion con un parametro opcional y un valor por defecto 
def frase (nombre,apellido, adjetivo="Tonto"):
    return (f"Hola {nombre} {apellido}, sos muy {adjetivo}")

frase_resultante = frase("Lucas", "Speziale", "inteligente")
print(frase_resultante)