#2 listas, una con nombres otra con apellidos 
nombres = ["Lucas", "Matias", "Camila", "Pedro"]
apellidos = [ "Dalto", "Zing", "Dalto", "Robertix"]

#Registrar esta informacion en un TXT de forma optima 

with open ("/Users/lucasspeziale/Desktop/Curso de Python/archivos/nombres_y_apellidos.txt", "w") as arch:
    arch.writelines("Los datos son:\n\n")
    [arch.writelines(f"Nombre: {n}\nApellido:{a}\n---------\n")for n,a in zip (nombres, apellidos)]


