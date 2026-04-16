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

    def __str__(self):
        return f"""Producto: {self.__nombre}
Precio: ${self.__precio:.2f}
Stock: {self.__stock}
"""

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

    def vender(self, cantidad):
        self.__stock -= cantidad

    def reabastecer(self, cantidad):
        self.__stock += cantidad


producto_uno = Producto("Macbook Neo", 13999.99, 10)
producto_dos = Producto("PS5", 11999.99)

print(producto_uno)
print(producto_dos)

print("Stock del PS5 actualizado a 20 unidades disponibles\n")

producto_dos.reabastecer(20)

print(producto_dos)

print("Venta de 2 unidades del Macbook Neo\n")

producto_uno.vender(2)

print(producto_uno)
