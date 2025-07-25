import numpy as np
import matplotlib.pyplot as plt

# Crear grilla de valores
x = np.linspace(-8, 8, 400)
y = np.linspace(-5, 5, 400)
X, Y = np.meshgrid(x, y)
Z = (X**2)/4 + Y**2

# Niveles de z para las curvas de nivel
niveles = [-1, 0, 1, 9]

# Graficar curvas de nivel
plt.figure(figsize=(8, 6))
contornos = plt.contour(X, Y, Z, levels=niveles, colors='blue')
plt.clabel(contornos, inline=True, fontsize=10)
plt.title('Curvas de nivel de z = x²/4 + y²')
plt.xlabel('x')
plt.ylabel('y')
plt.axhline(0, color='gray', linewidth=0.5)
plt.axvline(0, color='gray', linewidth=0.5)
plt.grid(True)
plt.axis('equal')

# Mostrar gráfico
plt.tight_layout()
plt.show()