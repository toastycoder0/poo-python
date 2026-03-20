# pyright: reportRedeclaration=false
import os
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


os.system("clear")

punto_uno = Punto2D(2, 3)
punto_dos = Punto2D(-3, 5)
punto_tres = Punto2D(-3, -5)
punto_cuatro = Punto2D(3, -5)
punto_cinco = Punto2D()
punto_seis = Punto2D(3.3, 4.4)

print(punto_uno, "cuadrante", punto_uno.cuadrante())
print(punto_dos, "cuadrante", punto_dos.cuadrante())
print(punto_tres, "cuadrante", punto_tres.cuadrante())
print(punto_cuatro, "cuadrante", punto_cuatro.cuadrante())
print(punto_cinco, "cuadrante", punto_cinco.cuadrante())
print(punto_seis, "cuadrante", punto_seis.cuadrante())
