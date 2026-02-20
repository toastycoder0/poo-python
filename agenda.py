# Hacer una agenda en python que almacene informacion de contactos como nombre teléfono y correo.
# Mostrar un menu que visualice las siguientes opciones
# 1) Agregar contactos
# 2) Eliminar contacto
# 3) Mostrar contactos
# 4) Salir
import os

os.system("clear")

agenda = []


def agregar_contacto():
    nombre = input("\nIngresa el nombre del contacto: ")

    for contacto in agenda:
        if contacto["nombre"] == nombre:
            print("Ya existe un contacto con ese nombre.")
            return

    telefono = input("Ingresa el teléfono del contacto: ")
    correo = input("Ingresa el correo del contacto: ")

    agenda.append({"nombre": nombre, "telefono": telefono, "correo": correo})

    print("Se agrego el contacto de forma correcta")


def eliminar_contacto():
    nombre = str(input("\nIngresa el nombre del contacto a eliminar: "))

    for contacto in agenda:
        if contacto["nombre"] == nombre:
            agenda.remove(contacto)
            print(f"Se elimino a {nombre} de la agenda")
            return

    print("El contacto no existe")


def mostrar_contactos():
    print("\nLista de contactos")
    if len(agenda) > 0:
        for contacto in agenda:
            print(f"\nTeléfono: {contacto['telefono']}")
            print(f"Nombre: {contacto['nombre']}")
            print(f"Correo: {contacto['correo']}\n")
    else:
        print("No hay contactos en la agenda")


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
            print("Opción invalida")


menu()
