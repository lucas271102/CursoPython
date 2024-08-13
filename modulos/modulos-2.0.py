#si el modulo estuviera en una carpeta de la misma ruta
#import funciones_buenas.saludar as saludar
import sys
sys.path.append('/Users/lucasspeziale/Desktop/Curso de Python//funciones_buenas')
import saludar as modulo_saludo
print(modulo_saludo.saludar("Lucas"))