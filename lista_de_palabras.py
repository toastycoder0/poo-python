"""
Escribe un programa que permita crear una lista de palabras y que, a continuación de tres opciones:
1) Contar: Me pide una cadena, y me dice cuántas veces aparece en la lista
2) Modificar: Me pide una cadena, y la otra cadena a modificar, y modifica
todas las apariciones de la primera por la segunda en la lista
3) Eliminar: Me pide una cadena, y la elimina de la lista
4) Mostrar: Muestra la lista de cadenas
5) Terminar
"""

import os

os.system("clear")

palabras = [
    "Hola Mundo",
    "Python",
    "Compilador",
    "Variable",
    "Objeto",
    "Clase",
    "Clase",
    "Método",
    "Tipo de dato",
    "Funciones",
    "Matriz",
]


def eliminar():
    pass


def mostrar():
    pass


def contar(palabra_a_buscar):
    veces_en_la_lista = 0
    for palabra in palabras:
        if palabra_a_buscar == palabra:
            veces_en_la_lista += 1
    return veces_en_la_lista


def modificar(palabra_a_buscar, palabra_a_modificar):
    for palabra_indice in range(len(palabras)):
        if palabras[palabra_indice] == palabra_a_buscar:
            palabras[palabra_indice] = palabra_a_modificar


def menu():
    while True:
        print("""
Opciones

1) Contar: Me pide una cadena, y me dice cuántas veces aparece en la lista
2) Modificar: Me pide una cadena, y la otra cadena a modificar, y modifica
todas las apariciones de la primera por la segunda en la lista
3) Eliminar: Me pide una cadena, y la elimina de la lista
4) Mostrar: Muestra la lista de cadenas
5) Terminar
        """)
        opcion = int(input("Ingresa una opción: "))

        if opcion == 1:
            palabra_a_buscar = input("Ingresa una palabra: ")
            print(f"La palabra aparece {contar(palabra_a_buscar)} veces")
        elif opcion == 2:
            palabra_a_buscar = input("Ingresa una palabra: ")
            palabra_a_modificar = input(
                f"Introduce la palabra por la que deseas modificar la palabra {palabra_a_buscar}: "
            )
            modificar(palabra_a_buscar, palabra_a_modificar)
            print(palabras)
        elif opcion == 3:
            pass
        elif opcion == 4:
            pass
        elif opcion == 5:
            print("Saliendo...")
            break
        else:
            print(f"La opción '{opcion}' no es valida")


menu()
