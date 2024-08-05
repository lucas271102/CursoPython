#usamos def para decirle al programa que creamos nuestra propia funcion 
#creando una funcion simple
def saludar():
    print("Hola, soy un programa")
    
saludar()


#creando una funcion con parametros. los parametros son variables que se crean para usarse dentro de una funcion y luego no usarse mas 
def viajar(vuelo, destino):
    destino = destino.lower()
    if destino == "argentina":
        aerolinea = "Aerolineas Argentinas"
    elif destino == "estados unidos":
        aerolinea = "American Airlines"
    print(f"Su vuelo {vuelo} es por la aerolinea {aerolinea}, verdad?")
        
viajar("AR 563", "argentina")
viajar("AA 900", "estados unidos")
        
#creando una funcion que nos retorne valores 
def crear_contraseña_random(num):
    chars = "abcdefghij" #crear caracteres aleatorios
    num_entero = str(num) #convierte a string el primer numero 
    num = int(num_entero[0])
    c1 = num - 2 #9s
    c2 = num 
    c3 = num - 5
    contraseña = f"{chars[c1]}{chars[c2]}{chars[c3]}{num* 2}"
    return contraseña

password = crear_contraseña_random(3)
frase = f"Tu contraseña es {password}"
print(frase)
    