"""
Crea un sistema de gestión de biblioteca en Python utilizando Programación Orientada a Objetos.
Define una clase Libro con atributos como título, autor, año de publicación, disponibilidad,
y una clase Biblioteca que permita agregar, eliminar, prestar y devolver libros,
así como listar los libros disponibles y mostrar el historial de préstamos de cada libro.
El sistema debe gestionar la disponibilidad de los libros y registrar las fechas de préstamo.
"""

import os


class Libro:
    def __init__(self, titulo, autor, anio_publicacion):
        self.__titulo = titulo
        self.__autor = autor
        self.__anio_publicacion = anio_publicacion
        self.__esta_disponible = True

    def __str__(self):
        disponibilidad = "Ocupado"

        if self.__esta_disponible:
            disponibilidad = "Disponible"

        return f"""
Titulo: {self.__titulo}
Autor: {self.__autor}
Año de publicación: {self.__anio_publicacion}
Disponibilidad: {disponibilidad}
        """

    def consultar_titulo(self):
        return self.__titulo

    def consultar_autor(self):
        return self.__autor

    def consultar_anio_publicacion(self):
        return self.__anio_publicacion

    def consultar_esta_disponible(self):
        return self.__esta_disponible

    def prestar_libro(self):
        self.__esta_disponible = False

    def devolver_libro(self):
        self.__esta_disponible = True


class Biblioteca:
    def __init__(self):
        self.__libros = []

    def __str__(self):
        biblioteca_texto = ""

        for libro in self.__libros:
            biblioteca_texto += str(libro) + "\n"

        return biblioteca_texto

    def consultar_libros(self):
        return self.__libros

    def agregar_libro(self, titulo, autor, anio_publicacion):
        libro_nuevo = Libro(titulo, autor, anio_publicacion)
        self.__libros.append(libro_nuevo)

    def eliminar_libro(self, titulo):
        for libro in self.__libros:
            if libro.consultar_titulo() == titulo:
                self.__libros.remove(libro)


while True:
    print("""
Opciones
1) Agregar un libro
2) Eliminar un libro 
3) Prestar un libro
4) Devolver un libro
5) Salir
    """)

    opcion = input("Ingresa una opción: ")

    if opcion == "1":
        pass
    elif opcion == "2":
        pass
    elif opcion == "3":
        pass
    elif opcion == "4":
        pass
    elif opcion == "5":
        pass
    else:
        print("")
