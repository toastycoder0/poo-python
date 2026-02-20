# Hacer una agenda en python que almacene informacion de contactos como nombre teléfono y correo.
# Mostrar un menu que visualice las siguientes opciones
# 1) Agregar contactos
# 2) Eliminar contacto
# 3) Mostrar contactos
# 4) Salir
import os

os.system("clear")

nombres = []
telefonos = []
correos = []


def agregar_contacto():
    nombre = input("\nIngresa el nombre del contacto: ")

    if nombre in nombres:
        print("Ya existe un contacto con ese nombre.")
        return

    telefono = input("Ingresa el teléfono del contacto: ")
    correo = input("Ingresa el correo del contacto: ")

    nombres.append(nombre)
    telefonos.append(telefono)
    correos.append(correo)

    print("Se agregó el contacto de forma correcta.")


def eliminar_contacto():
    nombre = input("\nIngresa el nombre del contacto a eliminar: ")

    if nombre not in nombres:
        print("El contacto no existe.")
        return

    index = nombres.index(nombre)

    nombres.pop(index)
    telefonos.pop(index)
    correos.pop(index)

    print(f"Se eliminó el contacto de {nombre}.")


def mostrar_contactos():
    print("\nLista de contactos:")
    if len(nombres) > 0:
        for i in range(len(nombres)):
            print(f"\nNombre: {nombres[i]}")
            print(f"Teléfono: {telefonos[i]}")
            print(f"Correo: {correos[i]}\n")
    else:
        print("No hay contactos en la agenda.")


def menu():
    while True:
        print("""
------ Agenda ------ 

1) Agregar contactos
2) Eliminar contacto
3) Mostrar contactos
4) Salir
        """)
        opcion = int(input("Ingresa una opción: "))

        if opcion == 1:
            agregar_contacto()
        elif opcion == 2:
            eliminar_contacto()
        elif opcion == 3:
            mostrar_contactos()
        elif opcion == 4:
            print("\nSaliendo...")
            break
        else:
            print("Opción inválida.")


menu()
