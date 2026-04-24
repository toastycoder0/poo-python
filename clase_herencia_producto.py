"""
Crear una superclase llamada Producto
    Atributos:
        1) clave
        2) nombre
        3) precio
    Metodos
        1) __str__
        2) set y get con decoradores

Crear la clase Perecedero que deriva de Producto
    Atributos:
       1) Fecha de caducidad
    Metodos:
        1) __str__
        2) set y get con decoradores
        3) Anexar un metodo llamado imprimir que muestre la fecha de caducidad

Crear la clase Electronico que deriva de Producto
    Atributos:
        1) Marca
    Metodos:
        1) __str__
        2) set y get con decoradores
        3) Anexar un metodo llamado imprimir que imprimer la marca del producto

Crear 3 objetos p1 de Producto, p2 de Perecedero y p3 de Electronico con los siguiente datos
"""


class Producto:
    def __init__(self, clave, nombre, precio):
        self.__clave = clave
        self.__nombre = nombre
        self.__precio = precio

    def __str__(self):
        return f"Producto: {self.nombre}\nClave: {self.clave}\nPrecio: {self.precio}"

    @property
    def clave(self):
        return self.__clave

    @property
    def nombre(self):
        return self.__nombre

    @property
    def precio(self):
        return self.__precio

    @clave.setter
    def clave(self, valor):
        self.__clave = valor

    @nombre.setter
    def nombre(self, valor):
        self.__nombre = valor

    @precio.setter
    def precio(self, valor):
        self.__precio = valor


class Perecedero(Producto):
    def __init__(self, clave, nombre, precio, fecha_de_caducidad):
        super().__init__(clave, nombre, precio)
        self.__fecha_de_caducidad = fecha_de_caducidad

    def __str__(self):
        return f"{super().__str__()}\nFecha: {self.__fecha_de_caducidad}"

    @property
    def fecha_de_caducidad(self):
        return self.__fecha_de_caducidad

    @fecha_de_caducidad.setter
    def fecha_de_caducidad(self, valor):
        self.__fecha_de_caducidad = valor

    def imprimir(self):
        return self.__fecha_de_caducidad


class Electronico(Producto):
    def __init__(self, clave, nombre, precio, marca):
        super().__init__(clave, nombre, precio)
        self.__marca = marca

    def __str__(self):
        return f"{super().__str__()}\nMarca: {self.__marca}"

    @property
    def marca(self):
        return self.__marca

    @marca.setter
    def marca(self, valor):
        self.__marca = valor

    def imprimir(self):
        return self.__marca


p1 = Producto(1, "Atún", 35)
p2 = Perecedero(2, "Galletas", 28, "2025-12-31")
p3 = Electronico(3, "Laptop", 10999, "Asus")

productos = (p1, p2, p3)

for producto in productos:
    print(f"{producto}\n")
    print(f"Tipo de clase: {type(producto)}")

    if isinstance(producto, Electronico):
        print(f"{producto.nombre} pertenece a la clase Electronico")
