# pyright: reportRedeclaration=false
"""
Hacer un programa que cree una clase llamada CuentaBancaria:
1) La cuenta va a tener 3 atributos numero_de_cuenta, nombre_de_titular, saldo
2) La cuenta debe tener 2 constructores, el primero con todos los valores, el segundo sin saldo
3) Agregar el decorador property
4) Crear los siguientes metodos:
    a) Depositar
    b) Retirar
    c) Transferir
5) Aplicar sobrecarga de operadores a la clase:
    a) Usar una operdores logicos de comparación
"""

from multimethod import multimethod


class CuentaBancaria:
    @multimethod
    def __init__(
        self, nombre_de_titular: str, numero_de_cuenta: str, saldo: float | int
    ):
        self.__numero_de_cuenta = numero_de_cuenta
        self.__nombre_de_titular = nombre_de_titular
        self.__saldo = saldo

    @multimethod
    def __init__(self, nombre_de_titular: str, numero_de_cuenta: str):
        self.__numero_de_cuenta = numero_de_cuenta
        self.__nombre_de_titular = nombre_de_titular
        self.__saldo = 0

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
        self.__saldo = valor

    def depositar(self, cantidad):
        self.__saldo += cantidad

    def retirar(self, cantidad):
        if cantidad > self.__saldo:
            raise ValueError("La cantidad a retirar no puede ser mayor al saldo")
        self.__saldo -= cantidad

    def transferir(self, cantidad, cuenta_destino):
        if cantidad > self.__saldo:
            raise ValueError("La cantidad a retirar no puede ser mayor al saldo")
        self.__saldo -= cantidad
        cuenta_destino.saldo += cantidad


cuenta_uno = CuentaBancaria("Raul", "2A33", 100)
cuenta_dos = CuentaBancaria("Luis", "5A66")

print(cuenta_uno)
print(cuenta_dos)
