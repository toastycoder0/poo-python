import os

os.system("clear")

numero_de_calificaciones = 2
alumnos = []
calificaciones = []


def agregar_alumno():
    nuevo_alumno = input("\nIngresa el nombre del nuevo alumno: ")
    if nuevo_alumno in alumnos:
        print(f"El alumno {nuevo_alumno} ya esta registrado")
        return
    calificaciones_del_alumno = []
    for calificacion_indice in range(numero_de_calificaciones):
        calificacion = int(
            input(f"Ingresa el valor de la calificación {calificacion_indice + 1}: ")
        )
        calificaciones_del_alumno.append(calificacion)
    alumnos.append(nuevo_alumno)
    calificaciones.append(calificaciones_del_alumno)
    print(f"Alumno {nuevo_alumno} agregado")


def mostrar_alumnos():
    if len(alumnos) > 0:
        for alumno_indice in range(len(alumnos)):
            print(f"""
\nAlumno {alumno_indice + 1}
Nombre: {alumnos[alumno_indice]}
            """)
            for calificacion_indice in range(len(calificaciones[alumno_indice])):
                calificacion_valor = calificaciones[alumno_indice][calificacion_indice]
                print(
                    f"Materia {calificacion_indice + 1} con calificación de {calificacion_valor:.2f}"
                )
    else:
        print("\nNo hay alumnos registrados")


def eliminar_alumno():
    alumno_a_eliminar = input("\nIngresa el nombre del alumno a eliminar: ")
    if alumno_a_eliminar in alumnos:
        alumno_indice = alumnos.index(alumno_a_eliminar)
        alumnos.remove(alumno_a_eliminar)
        calificaciones.remove(calificaciones[alumno_indice])
        print(f"Alumno {alumno_a_eliminar} eliminado")
    else:
        print(f"El alumno {alumno_a_eliminar} no esta registrado")


def mostrar_promedios():
    if len(alumnos) > 0:
        for alumno_indice in range(len(alumnos)):
            promedio = 0

            for calificacion in calificaciones[alumno_indice]:
                promedio += calificacion

            promedio /= len(calificaciones[alumno_indice])

            print(f"""
\nAlumno {alumno_indice + 1}
Nombre: {alumnos[alumno_indice]}
Promedio: {promedio:.2f}
            """)
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
            print("Opción no valida")


menu()
