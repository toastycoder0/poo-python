# Hacer un programa que solicicte al usuario nombre y 3 calificaciones, almacenas los nombres en una
# lista y las calificaciones en una matriz. Mostrar un menu de opciones que me permita,
# 1) Agregar alumno
# 2) Mostrar alumnos
# 3) Eliminar alumno
# 4) Mostrar promedios
# 5) Salir

import os

os.system("clear")

alumnos = []
calificaciones = []


def agregar_alumno():
    nombre = input("\nIngresa el nombre del alumno: ")

    if nombre in alumnos:
        print("Ya hay una alumno con ese nombre registrado")
        return

    calificaciones_del_alumno = []

    for materia in range(3):
        calificacion = int(input(f"Ingresa la calificación {materia + 1} del alumno: "))
        calificaciones_del_alumno.append(calificacion)

    alumnos.append(nombre)
    calificaciones.append(calificaciones_del_alumno)

    print(f"Alumno {nombre} agregado")


def mostrar_alumnos():
    if len(alumnos) > 0:
        for alumno in alumnos:
            print(f"\nAlumno: {alumno}")
            alumno_indice = alumnos.index(alumno)
            for calificacion_indice in range(len(calificaciones[alumno_indice])):
                print(
                    f"Calificación {calificacion_indice + 1}: {calificaciones[alumno_indice][calificacion_indice]}"
                )
    else:
        print("No hay alumnos registrados")


def eliminar_alumno():
    nombre = input("\nIngresa el nombre del alumno a eliminar: ")
    if nombre in alumnos:
        alumno_indice = alumnos.index(nombre)
        alumnos.remove(nombre)
        calificaciones.remove(calificaciones[alumno_indice])
        print(f"Alumno {nombre} eliminado")
    else:
        print(f"El alumno {nombre} no existe")


def mostrar_promedios():
    print("\n")
    if len(alumnos) > 0:
        for alumno in alumnos:
            alumno_indice = alumnos.index(alumno)
            promedio = 0
            for calificacion in calificaciones[alumno_indice]:
                promedio += calificacion
            promedio /= len(calificaciones[alumno_indice])
            print(f"\nAlumno {alumno} con promedio de {promedio}")
    else:
        print("No hay alumnos registrados")


def main():
    while True:
        print("""
Opciones

1) Agregar alumno
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
            print("Saliendo....")
            break
        else:
            print(f"La opción ingresada {opcion} no esta disponible")


main()
