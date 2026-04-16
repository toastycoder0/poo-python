"""
Deseña una clase que se llame punto 3d que me permita crear objetos con los valores de x, y, y z
que me permita aplicar sobrecarga al constructor para crear un objetos 1 por defecto
debe contener un metodo que se llame modulo, el modulo es igual a los siguiente
aparte se debe diseñar 3 metodos para calcular los cosenos directores bajo la siguiente formula
angulo_de_x
"""

# pyright: reportRedeclaration=false
from os import system
from math import acos, degrees, sqrt
from multimethod import multimethod


class Punto3D:
    @multimethod
    def __init__(self, x: int, y: int, z: int):
        self.__x = x
        self.__y = y
        self.__z = z

    @multimethod
    def __init__(self):
        self.__x = 1
        self.__y = 1
        self.__z = 1

    def __str__(self):
        return f"p({self.__x}, {self.__y}, {self.__z})"

    @property
    def x(self):
        return self.__x

    @property
    def y(self):
        return self.__y

    @property
    def z(self):
        return self.__z

    @x.setter
    def modificar_x(self, valor):
        self.__x = valor

    @y.setter
    def modificar_y(self, valor):
        self.__y = valor

    @z.setter
    def modificar_z(self, valor):
        self.__z = valor

    def modulo(self):
        return sqrt(self.x**2 + self.y**2 + self.z**2)

    def angulo_de_x(self):
        valor_modulo = self.modulo()
        return degrees(acos(self.x / valor_modulo))

    def angulo_de_y(self):
        valor_modulo = self.modulo()
        return degrees(acos(self.y / valor_modulo))

    def angulo_de_z(self):
        valor_modulo = self.modulo()
        return degrees(acos(self.z / valor_modulo))


system("clear")

punto_uno = Punto3D(2, 3, 4)
punto_vacio = Punto3D()

print("Punto uno:", punto_uno)
print("Punto vacio", punto_vacio)


print("Modulo del punto uno", punto_uno.modulo())
print("Modulo del punto vacio", punto_vacio.modulo())

print("Punto uno (angulo de x)", punto_uno.angulo_de_x())  # 68
print("Punto uno (angulo de y)", punto_uno.angulo_de_y())  # 56
print("Punto uno (angulo de z)", punto_uno.angulo_de_z())  # 42
