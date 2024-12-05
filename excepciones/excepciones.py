def sumar_dos():
    a = input("Numero 1:")
    b = input("Numero 2:")
    try:
        resultado = int (a) +int(b)
    except:
        print("No te detengas ")
    return resultado

print(sumar_dos())