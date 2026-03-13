import os

os.system("clear")


class Reactangulo:
    def __init__(self, largo, ancho):
        self.__largo = largo
        self.__ancho = ancho

    def modificar_largo(self, nuevo_valor):
        self.__largo = nuevo_valor

    def modificar_ancho(self, nuevo_valor):
        self.__ancho = nuevo_valor

    def consultar_largo(self):
        return self.__largo

    def consultar_ancho(self):
        return self.__ancho

    def calcular_area(self):
        return self.__largo * self.__ancho


rectangulo = Reactangulo(2, 4)

print(f"""
----------
Rectangulo
----------
Largo:  {rectangulo.consultar_largo()}
Ancho:  {rectangulo.consultar_ancho()}
Area:   {rectangulo.calcular_area()}
""")
