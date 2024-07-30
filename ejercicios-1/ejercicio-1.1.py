#a) Diferencia en porcentaje en el curso actual y:
#el mas rapido de otros cursos 
#el mas lento de otros cursos 
#el promedio de los cursos 

#b)Porcentaje de material invisible que se reduce en:
#el promedio de los cursos 
#el curso actual 

#c) ver 10 horas de este curso a cuantas de otros cursos equivale? 

#Promedio de duracion 
otros_cursos_max = 7
otros_cursos_min =  2.5
otros_cursos_promedio = 4
dalto_curso = 1.5
#duracion de crudos
crudo_promedio = 5 
crudo_dalto = 3.5

#Diferncias de duracion
diferencia_con_min =100 - dalto_curso / otros_cursos_min * 100 #primero se ejecutan las multiplicaciones y divisiones 
diferencia_con_max =100 - dalto_curso *1000 // otros_cursos_max / 10 
diferencia_con_promedio =100 - dalto_curso / otros_cursos_promedio * 100 

#calculando el porcentaje de tiempo vacio 
tiempo_vacio_promedio = 100 - otros_cursos_promedio * 1000 // crudo_promedio / 10 
tiempo_vacio_dalto = 100 - dalto_curso * 1000 // crudo_dalto / 10 
print("-----------------")


print (f'El curso de dalto dura un {diferencia_con_min}% menos que el mas rapido')

print (f'El curso de dalto dura un {diferencia_con_max}% menos que el mas lento')

print (f'El curso de dalto dura un {diferencia_con_promedio}% menos que el promedio')
print("-----------------")
#mostrando la cantidad de espacios vacios que se remueven 
print(f'Un curso promedio elimina un  {tiempo_vacio_promedio}% de tiempo vacio')
print (f'Este curso eliminó el {tiempo_vacio_dalto}% de porcentaje vacio')

print("-----------------")
#mostrando diferencias si loos cursos duraran 10 horas 
print(f'Ver 10 horas de este curso equivale a ver {otros_cursos_promedio * 100 // dalto_curso / 10} horas de otros cursos ')
print(f'Ver 10 horas de otro curso equivale a ver {dalto_curso * 100 // otros_cursos_promedio / 10} horas de curso de dalto ')
print("-----------------")