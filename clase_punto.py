# pyright: reportRedeclaration=false
from os import system
from math import atan2, degrees, sqrt
from multimethod import multimethod


class Punto2D:
    @multimethod
    def __init__(self, x: int, y: int):
        self.__x = x
        self.__y = y

    @multimethod
    def __init__(self, x: float, y: float):
        self.__x = x
        self.__y = y

    @multimethod
    def __init__(self):
        self.__x = 0
        self.__y = 0

    def __str__(self):
        return f"p({self.__x}, {self.__y})"

    @property
    def x(self):
        return self.__x

    @property
    def y(self):
        return self.__y

    @x.setter
    def modificar_x(self, valor):
        self.__x = valor

    @y.setter
    def modificar_y(self, valor):
        self.__y = valor

    def suma(self, punto):
        x = self.x + punto.x
        y = self.y + punto.y
        return Punto2D(x, y)

    def resta(self, punto):
        x = self.x - punto.x
        y = self.y - punto.y
        return Punto2D(x, y)

    def modulo(self):
        return sqrt(self.x**2 + self.y**2)

    def angulo(self):
        return degrees(atan2(self.y, self.x))

    def cuadrante(self):
        if self.__x > 0 and self.__y > 0:
            return 1
        elif self.__x < 0 and self.__y > 0:
            return 2
        elif self.__x < 0 and self.__y < 0:
            return 3
        elif self.__x > 0 and self.__y < 0:
            return 4
        elif self.__x == 0 and self.__y == 0:
            return 0
        return None

    def __add__(self, v2):
        return Punto2D(self.x + v2.x, self.y + v2.y)

    def __sub__(self, v2):
        return Punto2D(self.x - v2.x, self.y - v2.y)

    def __mul__(self, escalar):
        return Punto2D(self.x * escalar, self.y * escalar)

    #
    # def __truediv__(self, n):
    #     return Punto2D(self.x / n, self.y / n)

    def __neg__(self):
        return Punto2D(self.x * (-1), self.y * (-1))


system("clear")

punto_uno = Punto2D(2, 3)
punto_dos = Punto2D(-3, 5)
punto_tres = Punto2D(-3, -5)

punto_cuatro = Punto2D(3, -5)
punto_cinco = Punto2D()
punto_seis = Punto2D(3.3, 4.4)

punto_suma = punto_uno + punto_dos
punto_resta = punto_uno - punto_dos
punto_multiplicacion = punto_uno * 2
punto_negativo = -punto_uno

print(punto_uno, "cuadrante", punto_uno.cuadrante())
print(punto_dos, "cuadrante", punto_dos.cuadrante())
print(punto_tres, "cuadrante", punto_tres.cuadrante())
print(punto_cuatro, "cuadrante", punto_cuatro.cuadrante())
print(punto_cinco, "cuadrante", punto_cinco.cuadrante())
print(punto_seis, "cuadrante", punto_seis.cuadrante())
print("Punto suma", punto_suma, "cuadrante", punto_suma.cuadrante())
print("Punto resta", punto_resta, "cuadrante", punto_resta.cuadrante())
print(
    "Punto por escalar",
    punto_multiplicacion,
    "cuadrante",
    punto_multiplicacion.cuadrante(),
)
print("Punto negativo", punto_negativo, "cuadrante", punto_negativo.cuadrante())
