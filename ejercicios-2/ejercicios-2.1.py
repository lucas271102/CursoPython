#falto el profesor y los alumnos van a armar la clase
#pedir el nombre y la edad de los compañeros que vinieron hoy a clase 

#funcion para obtener al asistente y al profesro según la edad 
def obtener_compañeros(cantidad_de_compañeros):
    #creando la lista donde se van a acumular los compañeros 
    compañeros = []
    #ejecuta un bucle for para pedir información de cada compaeñero 
    for i in range (cantidad_de_compañeros):
      nombre = input("ingrese el nombre del compañero")
      edad = int(input("ingrese la edad del compañero"))
      compañero= (nombre,edad)
      #se agrega la informacion que se pidio a la lista
      compañeros.append(compañero)  
      #ordenando de menor a mayor según su edad
    compañeros.sort(key= lambda x : x[1])
    #compañeros[x] devuelve una tupla (nombre, edad) y despues accedemos al nombre 
    #para definir al asistente y al profesor 
    asistente = compañeros[0][0]
    profesor = compañeros[-1][0]
    return asistente,profesor

asistente, profesor = obtener_compañeros(6)
print(f"el asistente es {asistente} y el profesor es {profesor}")