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
        return f"Producto: {self.__nombre}\nPrecio: {self.__precio}\nUnidades: {self.__stock}\n"

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
        if cantidad > self.stock:
            return NotImplemented
        self.stock -= cantidad

    def reabastecer(self, cantidad):
        self.stock += cantidad


producto_uno = Producto("Consola Sony PlayStation 5 Slim", 8599.00, 25)
producto_dos = Producto("Consola Nintendo Switch 2", 9132.02)

print(producto_uno)
print(producto_dos)

print(f"1 unidad vendida de {producto_uno.nombre}")
producto_uno.vender(1)

print(producto_uno)

print(f"20 unidades agregadas de {producto_dos.nombre}")
producto_dos.reabastecer(20)

print(producto_dos)
