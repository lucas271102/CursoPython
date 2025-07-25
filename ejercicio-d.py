import numpy as np
import matplotlib.pyplot as plt

# Crear valores de x
x = np.linspace(-10, 10, 400)

# Definir una función que calcula y en función de z
def recta_para_z(z):
    return (-2 * x + 6 * z) / 3

# Crear figura
plt.figure(figsize=(8, 6))

# Graficar las rectas para cada valor de z
for z_val, color in zip([-1, 0, 1, 2], ['blue', 'green', 'orange', 'red']):
    y = recta_para_z(z_val)
    plt.plot(x, y, label=f'z = {z_val}', color=color)

# Decoración del gráfico
plt.title('Curvas de nivel de 2x + 3y - 6z = 0')
plt.xlabel('x')
plt.ylabel('y')
plt.grid(True)
plt.axhline(0, color='gray', linewidth=0.5)
plt.axvline(0, color='gray', linewidth=0.5)
plt.legend()
plt.xlim(-10, 10)
plt.ylim(-10, 10)
plt.gca().set_aspect('equal')
plt.tight_layout()
plt.show()