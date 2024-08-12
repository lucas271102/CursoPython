#importando un modulo y asignandole el nombre m_saludar
#import modulo_saludar as m_saludar

#desde ese modulo, importamos una funcion 
from modulo_saludar import saludar

#creasmos las variables con los resultados
saludo = saludar("Lucas")
#para ver las propiedades y metodos 
#print(dir(m_saludar))

#mostramos los resultados 

print(saludo)