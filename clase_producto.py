"""
1.Hacer una clase producto que contenga 3 atributos
- Nombre
- Precio
- Stock (existencia)
2.Permite crear objetos sin stock (por defecto 0)
3.Debe tener 2 metodos
- Vender (cantidad)
- Reabastecer (cantidad)
"""
# pyright: reportRedeclaration=false

from multimethod import multimethod


class Producto:
    @multimethod
    def __init__(self, nombre: str, precio: float, stock: int):
        self.__nombre = nombre
        self.__precio = precio
        self.__stock = stock

    @multimethod
    def __init__(self, nombre: str, precio: float):
        self.__nombre = nombre
        self.__precio = precio
        self.__stock = 0

    @property
    def nombre(self):
        return self.__nombre

    @property
    def precio(self):
        return self.__precio

    @property
    def stock(self):
        return self.__stock

    @nombre.setter
    def nombre(self, valor):
        self.__nombre = valor

    @precio.setter
    def precio(self, valor):
        self.__precio = valor

    @stock.setter
    def stock(self, valor):
        self.__stock = valor
