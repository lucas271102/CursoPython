#creando un conjunto con set 

conjunto = set(["dato 1"])

#metiendo un conjunto dentro de otro conjunto. se utiliza frozenset
conjunto1 =frozenset( {"dato1", "dato2"})
conjunto2 = {conjunto1, "dato 3"}
print(conjunto2) 

#teoria de conjuntos 

conjunto1 = {2,4,6}
conjunto2= {1,3,7}
#verificando si es un subconjunto  issubset es lo mismo que <=
resultado = conjunto2.issubset(conjunto1)
resultado = conjunto2 <= conjunto1

#verificando si es un superconjunto
resultado = conjunto2.issuperset(conjunto1)
resultado = conjunto2 < conjunto1

#verificando si hay algun numero en comun. solo da true cuando NINGUN ELEMENTO O NUMERO COINCIDE EN LOS CONJUNTOS 
resultado = conjunto1.isdisjoint(conjunto2)

print(resultado)