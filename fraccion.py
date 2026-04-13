# pyright: reportRedeclaration=false
from multimethod import multimethod
import math


class Fraccion:
    @multimethod
    def __init__(self, numerador: int, denominador: int):
        self.__numerador = numerador
        self.__denominador = denominador if denominador != 0 else 1
        self.simplificar()

    @multimethod
    def __init__(self):
        self.__numerador = 1
        self.__denominador = 1

    def __str__(self):
        return f"{self.__numerador}/{self.__denominador}"

    @property
    def numerador(self):
        return self.__numerador

    @property
    def denominador(self):
        return self.__denominador

    @numerador.setter
    def numerador(self, valor):
        self.__numerador = valor
        self.simplificar()

    @denominador.setter
    def denominador(self, valor):
        if valor == 0:
            valor = 1
        self.__denominador = valor
        self.simplificar()

    def simplificar(self):
        mcd = math.gcd(self.__numerador, self.__denominador)
        self.__numerador //= mcd
        self.__denominador //= mcd

        if self.__denominador < 0:
            self.__numerador *= -1
            self.__denominador *= -1

    def a_decimal(self):
        return self.__numerador / self.__denominador

    def __add__(self, other):
        if not isinstance(other, Fraccion):
            return NotImplemented
        num = (
            self.__numerador * other.__denominador
            + other.__numerador * self.__denominador
        )
        den = self.__denominador * other.__denominador
        return Fraccion(num, den)

    def __sub__(self, other):
        if not isinstance(other, Fraccion):
            return NotImplemented
        num = (
            self.__numerador * other.__denominador
            - other.__numerador * self.__denominador
        )
        den = self.__denominador * other.__denominador
        return Fraccion(num, den)

    def __mul__(self, other):
        if not isinstance(other, Fraccion):
            return NotImplemented
        return Fraccion(
            self.__numerador * other.__numerador,
            self.__denominador * other.__denominador,
        )

    def __truediv__(self, other):
        if not isinstance(other, Fraccion):
            return NotImplemented
        return Fraccion(
            self.__numerador * other.__denominador,
            self.__denominador * other.__numerador,
        )

    def __pow__(self, potencia):
        return Fraccion(self.__numerador**potencia, self.__denominador**potencia)

    def __neg__(self):
        return Fraccion(-self.__numerador, self.__denominador)

    def __eq__(self, other):
        if not isinstance(other, Fraccion):
            return NotImplemented
        return (
            self.__numerador == other.__numerador
            and self.__denominador == other.__denominador
        )

    def __lt__(self, other):
        if not isinstance(other, Fraccion):
            return NotImplemented
        return self.a_decimal() < other.a_decimal()

    def __le__(self, other):
        if not isinstance(other, Fraccion):
            return NotImplemented
        return self.a_decimal() <= other.a_decimal()

    def __gt__(self, other):
        if not isinstance(other, Fraccion):
            return NotImplemented
        return self.a_decimal() > other.a_decimal()

    def __ge__(self, other):
        if not isinstance(other, Fraccion):
            return NotImplemented
        return self.a_decimal() >= other.a_decimal()


fraccion_uno = Fraccion(1, 2)
fraccion_dos = Fraccion(3, 4)

print("Fracciones:")
print("f1 =", fraccion_uno)
print("f2 =", fraccion_dos)

print("Suma:", fraccion_uno + fraccion_dos)
print("Resta:", fraccion_uno - fraccion_dos)
print("Multiplicación:", fraccion_uno * fraccion_dos)
print("División:", fraccion_uno / fraccion_dos)
print("Potencia:", fraccion_uno**2)
print("Negación:", -fraccion_uno)

print("¿f1 == f2?", fraccion_uno == fraccion_dos)
print("¿f1 < f2?", fraccion_uno < fraccion_dos)
print("¿f1 <= f2?", fraccion_uno <= fraccion_dos)
print("¿f1 > f2?", fraccion_uno > fraccion_dos)
print("¿f1 >= f2?", fraccion_uno >= fraccion_dos)

print("f1 en decimal:", fraccion_uno.a_decimal())
