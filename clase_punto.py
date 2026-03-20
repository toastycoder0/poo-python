import os
from typing import Self


class Punto2D:
    def __init__(self, x, y):
        self.__x = x
        self.__y = y

    def __str__(self):
        return f"p({self.__x}, {self.__y})"

    def obtener_x(self):
        return self.__x

    def obtener_y(self):
        return self.__y

    def modificar_x(self, valor):
        self.__x = valor

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

punto_uno = Punto2D(3, 5)
punto_dos = Punto2D(-3, 5)
punto_tres = Punto2D(-3, -5)
punto_cuatro = Punto2D(3, -5)

print(punto_uno, "cuadrante", punto_uno.cuadrante())
print(punto_dos, "cuadrante", punto_dos.cuadrante())
print(punto_tres, "cuadrante", punto_tres.cuadrante())
print(punto_cuatro, "cuadrante", punto_cuatro.cuadrante())
