# Hacer un programa que resuelva la soluciones de una ecuacion cuadratica
# usando la formaula general
import os
from math import pow, sqrt

os.system("clear")

a = int(input("Ingresa el valor de a: "))
b = int(input("Ingresa el valor de b: "))
c = int(input("Ingresa el valor de c: "))

disc = pow(b, 2) - (4 * a * c)
if disc > 0:
    x1 = (-1 * b + sqrt(disc)) / (2 * a)
    x2 = (-1 * b - sqrt(disc)) / (2 * a)
    print("Raíces reales diferentes")
    print(f"{a:.0f}x² + {b:.0f}x + {c:.0f} = 0")
    print(f"x1 es igual a {x1:.2f}")
    print(f"x2 es igual a {x2:.2f}")
elif disc == 0:
    x1 = (-1 * b) / (2 * a)
    x2 = (-1 * b) / (2 * a)
    print("Raíces reales repetidas")
    print(f"{a:.0f}x² + {b:.0f}x + {c:.0f} = 0")
    print(f"x1 es igual a {x1:.2f}")
    print(f"x2 es igual a {x2:.2f}")
else:
    print("Raíces complejas")
