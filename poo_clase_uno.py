import os


class Punto:
    def __init__(self, x, y):
        self.__ejex = x
        self.__ejey = y

    def __str__(self):
        return f"P({self.__ejex}, {self.__ejey})"

    def obtener_x(self):
        return self.__ejex

    def obtener_y(self):
        return self.__ejey


os.system("clear")

punto_uno = Punto(5, 8)
punto_dos = Punto(-3, 0)

print(punto_uno, punto_dos)
print(f"""
Valor de "x" en el punto uno: {punto_uno.obtener_x()}
Valor de "x" en el punto dos: {punto_dos.obtener_x()}
""")
