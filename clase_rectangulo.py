import os

os.system("clear")


class Reactangulo:
    def __init__(self, largo, ancho):
        self.__largo = largo
        self.__ancho = ancho

    def __str__(self):
        return f"""
Largo: {self.__largo}
Ancho: {self.__ancho}
Area: {self.__largo * self.__ancho}
        """

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


def crear_rectangulo():
    print(f"Rectangulo {len(rectangulos) + 1}")
    largo = int(input("Ingresa el valor del largo: "))
    ancho = int(input("Ingresa el valor del ancho: "))
    rectangulo_nuevo = Reactangulo(largo, ancho)
    rectangulos.append(rectangulo_nuevo)


def listar_rectangulos():
    if len(rectangulos) > 0:
        for rectangulo in rectangulos:
            indice = rectangulos.index(rectangulo)
            print(f"""
----------
Rectangulo {indice + 1}
----------
{rectangulo}
            """)
    else:
        print("No hay rectangulos por mostrar")


def mostrar_un_rectangulo():
    numero_de_rectangulos = int(input("Ingresa el numero del rectangulo a consultar: "))


def menu():
    while True:
        print("""
Opciones
1) Crear un triangulo
2) Listar triangulos
3) Obtener la información de un solo triangulo
4) Eliminar triangulo
5) Salir
        """)
        opcion = input("Ingresa una opción")

        if opcion == "1":
            crear_rectangulo()
        elif opcion == "2":
            listar_rectangulos()
        elif opcion == "3":
            pass
        elif opcion == "4":
            pass
        elif opcion == "5":
            print("Saliendo...")
            break
        else:
            print(f"La opción {opcion} no es valida")
