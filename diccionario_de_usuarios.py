"""
Hacer un programa que solicite al usuario clave y nombre y los almacena en un diccionario
en un menu con las siguientes opciones
1) Agregar un usuario
2) Mostrar un usuario
3) Eliminar un usuario
4) Salir
"""

import os

os.system("clear")

personas = {}


def agregar_usuario():
    nombre = input("Ingresa el nombre del nuevo usuario: ")
    clave = input("Ingresa la clave: ")
    personas[clave] = nombre
    print(f"Usuario {nombre} agregado\n")


def mostrar_usuarios():
    if len(personas) > 0:
        for clave, nombre in personas.items():
            print(f"Nombre: {nombre}")
            print(f"Clave: {clave}\n")
    else:
        print("No hay usuarios\n")


def eliminar_usuario():
    clave = input("Ingresa la clave: ")

    if personas[clave]:
        print(f"Usuario {personas[clave]} eliminado\n")
        personas.pop(clave)
    else:
        print(f"No hay ningun usuario con clave {clave}\n")


def menu():
    print("""
Opciones

1) Agregar un usuario
2) Mostrar un usuarios
3) Eliminar un usuario
4) Salir
""")
    while True:
        opcion = int(input("Ingresa una opción: "))

        if opcion == 1:
            agregar_usuario()
        elif opcion == 2:
            mostrar_usuarios()
        elif opcion == 3:
            eliminar_usuario()
        elif opcion == 4:
            print("Saliendo...")
            break
        else:
            print(f"La opción '{opcion}' no existe")


menu()
