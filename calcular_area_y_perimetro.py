# Hacer un programa que calcule el area y el perimetro de un circulo,
# preguntandole al usuario que ingrese el valor del radio desde el teclado
import os

from math import pow, pi

os.system("clear")

radius = float(input("Insert te radius of the circle: "))

area = round(pi * pow(radius, 2), 2)
perimetter = round(pi * 2 * radius, 2)

print(f"The area is {area:.2f}")
print(f"The perimetter is {perimetter:.2f}")
