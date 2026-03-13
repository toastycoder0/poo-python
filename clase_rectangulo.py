import os

os.system("clear")


class Reactangulo:
    def __init__(self, largo, ancho):
        self.__largo = largo
        self.__ancho = ancho

    def consultarLargo(self):
        return self.__largo

    def consultarAncho(self):
        return self.__ancho

    def calcularArea(self):
        return self.__largo * self.__ancho

    def modificarLargo(self, nuevo_valor):
        self.__largo = nuevo_valor

    def modificarAncho(self, nuevo_valor):
        self.__ancho = nuevo_valor


rectangulo_uno = Reactangulo(2, 4)
rectangulo_dos = Reactangulo(8, 6)

rectangulos = [rectangulo_uno, rectangulo_dos]

for rectangulo in rectangulos:
    indice = rectangulos.index(rectangulo)
    print(f"""
----------
Rectangulo {indice + 1}
----------
Largo:  {rectangulo.consultarLargo()}
Ancho:  {rectangulo.consultarAncho()}
Area:   {rectangulo.calcularArea()}
    """)
