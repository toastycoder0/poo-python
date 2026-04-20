"""
Implementar una clase que se llame complejo, la clase complejo va a representar a un numero complejo considerando las siguientes especificaciones:
1) Contiene 2 atributos (real, imaginaria)
2) Debe contener 2 constructores
    a) Crear con valores
    b) Crear en vacio (1 y 1)
3) Anexar el motodo str que imprime a+bi
4) Crear un metodo que se llame modulo
5) Crear un metodo que se llame argumento que va a calcular el angulo de alineacion
6) Crear un metodo que se llame polar
7) Crear un constructor que me permita crear un objeto usando la clase fraccion
8) Crear un metodo que se llame sumar con (parte real) + (parte real) y (parte imaginaria) + (parte imaginaria) sobrecarga
9) Crear un metodo que se llame restar (sobrecarga)
"""

from multimethod import multimethod
from math import sqrt, atan2, degrees
from fraccion import Fraccion


# pyright: reportRedeclaration=false
class Complejo:
    @multimethod
    def __init__(self, real: int, imaginario: int):
        self.__real = real
        self.__imaginario = imaginario

    @multimethod
    def __init__(self, real: float, imaginario: float):
        self.__real = real
        self.__imaginario = imaginario

    @multimethod
    def __init__(self, real: Fraccion, imaginario: Fraccion):
        self.__real = real
        self.__imaginario = imaginario

    @multimethod
    def __init__(self):
        self.__real = 1
        self.__imaginario = 1

    @property
    def real(self):
        return self.__real

    @property
    def imaginario(self):
        return self.__imaginario

    @real.setter
    def real(self, valor):
        self.__real = valor

    @imaginario.setter
    def imaginario(self, valor):
        self.__imaginario = valor

    def __str__(self):
        return f"z={self.real}+{self.imaginario}i"

    def __add__(self, v2):
        return Complejo(self.real + v2.real, self.imaginario + v2.imaginario)

    def __sub__(self, v2):
        return Complejo(self.real - v2.real, self.imaginario - v2.imaginario)

    def modulo(self):
        if not isinstance(self.imaginario, Fraccion) and not isinstance(
            self.real, Fraccion
        ):
            return sqrt(self.imaginario + self.real)
        elif isinstance(self.imaginario, Fraccion) and isinstance(self.real, Fraccion):
            return sqrt(self.imaginario.a_decimal() + self.real.a_decimal())
        else:
            return NotImplemented

    def argumento(self):
        angulo = 0
        if not isinstance(self.imaginario, Fraccion) and not isinstance(
            self.real, Fraccion
        ):
            angulo = degrees(atan2(self.imaginario, self.real))
        elif isinstance(self.imaginario, Fraccion) and isinstance(self.real, Fraccion):
            angulo = degrees(atan2(self.imaginario.a_decimal(), self.real.a_decimal()))
        if angulo < 0:
            angulo += 360

        return angulo

    def polar(self):
        return f"{self.modulo():.2f}∠{self.argumento():.2f}"


numero_uno = Complejo(3, 4)
numero_dos = Complejo(-3, -4)
numero_tres = Complejo(Fraccion(1, 2), Fraccion(1, 2))

print("z1", numero_uno)
print("z1 modulo ", numero_uno.modulo())
print("z1 argumento", numero_uno.argumento())
print("z1 en polar", numero_uno.polar())
print("z2", numero_uno)
print("z3", numero_tres)
print("z3 modulo", numero_tres.modulo())
print("z3 argumento", numero_tres.argumento())
print("z3 en polar", numero_tres.polar())

print("Suma z1 + z2", numero_uno + numero_dos)
print("Suma z1 - z2", numero_uno - numero_dos)
print("Argumento z2", numero_dos.argumento())
