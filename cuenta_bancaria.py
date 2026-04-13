# pyright: reportRedeclaration=false
from multimethod import multimethod


class CuentaBancaria:
    @multimethod
    def __init__(
        self, nombre_de_titular: str, numero_de_cuenta: str, saldo: float | int
    ):
        self.__numero_de_cuenta = numero_de_cuenta
        self.__nombre_de_titular = nombre_de_titular
        self.__saldo = float(saldo)

    @multimethod
    def __init__(self, nombre_de_titular: str, numero_de_cuenta: str):
        self.__numero_de_cuenta = numero_de_cuenta
        self.__nombre_de_titular = nombre_de_titular
        self.__saldo = 0.0

    def __str__(self):
        return f"""
Titular: {self.__nombre_de_titular}
Número de cuenta: {self.__numero_de_cuenta}
Saldo: ${self.__saldo:.2f}
"""

    @property
    def numero_de_cuenta(self):
        return self.__numero_de_cuenta

    @property
    def nombre_de_titular(self):
        return self.__nombre_de_titular

    @property
    def saldo(self):
        return self.__saldo

    @numero_de_cuenta.setter
    def numero_de_cuenta(self, valor):
        self.__numero_de_cuenta = valor

    @nombre_de_titular.setter
    def nombre_de_titular(self, valor):
        self.__nombre_de_titular = valor

    @saldo.setter
    def saldo(self, valor):
        if valor < 0:
            raise ValueError("El saldo no puede ser negativo")
        self.__saldo = float(valor)

    def depositar(self, cantidad):
        if cantidad <= 0:
            raise ValueError("La cantidad debe ser positiva")
        self.__saldo += cantidad

    def retirar(self, cantidad):
        if cantidad > self.__saldo:
            raise ValueError("Saldo insuficiente")
        self.__saldo -= cantidad

    def transferir(self, cantidad, cuenta_destino):
        if not isinstance(cuenta_destino, CuentaBancaria):
            raise TypeError("La cuenta destino debe ser una CuentaBancaria")
        if cantidad > self.__saldo:
            raise ValueError("Saldo insuficiente")
        self.__saldo -= cantidad
        cuenta_destino.saldo += cantidad

    def __eq__(self, other):
        if not isinstance(other, CuentaBancaria):
            return NotImplemented
        return self.__saldo == other.__saldo

    def __lt__(self, other):
        if not isinstance(other, CuentaBancaria):
            return NotImplemented
        return self.__saldo < other.__saldo

    def __gt__(self, other):
        if not isinstance(other, CuentaBancaria):
            return NotImplemented
        return self.__saldo > other.__saldo


cuenta_uno = CuentaBancaria("Raul", "2A33", 100)
cuenta_dos = CuentaBancaria("Luis", "5A66")

print("Estado inicial:")
print(cuenta_uno)
print(cuenta_dos)

cuenta_uno.depositar(50)
print("Después de depositar 50 a cuenta_uno:")
print(cuenta_uno)

cuenta_uno.retirar(30)
print("Después de retirar 30 a cuenta_uno:")
print(cuenta_uno)

cuenta_uno.transferir(50, cuenta_dos)
print("Después de transferir 50 de cuenta_uno a cuenta_dos:")
print("Cuenta uno:")
print(cuenta_uno)
print("Cuenta dos:")
print(cuenta_dos)

print("¿Tienen el mismo saldo?", cuenta_uno == cuenta_dos)
print("¿Cuenta uno tiene menos saldo?", cuenta_uno < cuenta_dos)
print("¿Cuenta uno tiene más saldo?", cuenta_uno > cuenta_dos)
