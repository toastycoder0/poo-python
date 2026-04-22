"""
En Python, una clase abstracta es un "molde" o plantilla que no puedes usar
directamente para crear objetos.
Su función principal es definir una estructura base (métodos y propiedades)
que sus clases "hijas" están obligadas a implementar.
"""

from abc import ABC, abstractmethod
from math import pi, sqrt


class Forma(ABC):
    @abstractmethod
    def area(self) -> float:
        pass

    @abstractmethod
    def perimetro(self) -> float:
        pass


class Rectangulo(Forma):
    def __init__(self, ancho, alto):
        self.__ancho = ancho
        self.__alto = alto

    def area(self):
        return self.__alto * self.__ancho

    def perimetro(self):
        return 2 * (self.__alto + self.__ancho)


class Triangulo(Forma):
    def __init__(self, base, altura):
        self.__base = base
        self.__altura = altura

    def area(self):
        return (self.__base * self.__altura) / 2

    def perimetro(self):
        base_entre_dos = self.__base / 2
        hipotenusa = sqrt(base_entre_dos**2 + self.__altura**2)
        return self.__base + hipotenusa + hipotenusa


class Circulo(Forma):
    def __init__(self, radio):
        self.__radio = radio

    def area(self):
        return pi * (self.__radio**2)

    def perimetro(self):
        return 2 * pi * self.__radio


rectangulo = Rectangulo(3, 4)
circulo = Circulo(5)
triangulo = Triangulo(6, 4)

print(f"""
----Rectangulo----
Área {rectangulo.area()}
Perimétro {rectangulo.perimetro()}""")

print(f"""
----Circulo----
Área {circulo.area()}
Perimétro {circulo.perimetro()}""")

print(f"""
---Triangulo---
Área {triangulo.area()}
Perimétro {triangulo.perimetro()}""")
