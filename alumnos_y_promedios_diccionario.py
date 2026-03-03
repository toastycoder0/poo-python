import os

os.system("clear")

numero_de_calificaciones = 2
alumnos = {}


def agregar_alumno():
    nombre = input("\nIngresa el nombre del nuevo alumno: ")

    if nombre in alumnos:
        print(f"El alumno {nombre} ya está registrado")
        return

    calificaciones = []

    for i in range(numero_de_calificaciones):
        calificacion = int(input(f"Ingresa el valor de la calificación {i + 1}: "))
        calificaciones.append(calificacion)

    alumnos[nombre] = calificaciones
    print(f"Alumno {nombre} agregado")


def mostrar_alumnos():
    if alumnos:
        for nombre, lista_calificaciones in alumnos.items():
            print(f"\nNombre: {nombre}")

            materia = 1
            for calificacion in lista_calificaciones:
                print(f"Materia {materia} con calificación de {calificacion:.2f}")
                materia += 1
    else:
        print("\nNo hay alumnos registrados")


def eliminar_alumno():
    nombre = input("\nIngresa el nombre del alumno a eliminar: ")

    if nombre in alumnos:
        del alumnos[nombre]
        print(f"Alumno {nombre} eliminado")
    else:
        print(f"El alumno {nombre} no está registrado")


def mostrar_promedios():
    if alumnos:
        for nombre, lista_calificaciones in alumnos.items():
            promedio = sum(lista_calificaciones) / len(lista_calificaciones)

            print(f"\nNombre: {nombre}")
            print(f"Promedio: {promedio:.2f}")
    else:
        print("\nNo hay alumnos registrados")


def menu():
    while True:
        print("""
Opciones

1) Agregar un alumno
2) Mostrar alumnos
3) Eliminar alumno
4) Mostrar promedios
5) Salir
        """)

        opcion = int(input("Ingresa una opción: "))

        if opcion == 1:
            agregar_alumno()
        elif opcion == 2:
            mostrar_alumnos()
        elif opcion == 3:
            eliminar_alumno()
        elif opcion == 4:
            mostrar_promedios()
        elif opcion == 5:
            print("Saliendo...")
            break
        else:
            print("Opción no válida")


menu()
