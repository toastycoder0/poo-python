import os
import math


os.system("clear")


def calcular_area_del_triangulo():
    lado = float(input("Ingresa la longitud del lado del triángulo equilátero: "))
    area = (math.sqrt(3) / 4) * lado**2
    print(f"El área del triángulo equilátero es: {area:.2f}\n")


def calcular_area_del_rombo():
    diagonal_mayor = float(input("Ingresa la diagonal mayor del rombo: "))
    diagonal_menor = float(input("Ingresa la diagonal menor del rombo: "))
    area = (diagonal_mayor * diagonal_menor) / 2
    print(f"El área del rombo es: {area:.2f}\n")


def calcular_volumen_del_cubo():
    lado = float(input("Ingresa la longitud del lado del cubo: "))
    volumen = lado**3
    print(f"El volumen del cubo es: {volumen:.2f}\n")


def menu():
    print("""
Opciones

1) Area de un triangulo equilatero
2) Area de un rombo
3) Volumen de un cubo
4) Salir
    """)
    while True:
        opcion = int(input("Ingresa una opción: "))

        if opcion == 1:
            calcular_area_del_triangulo()
        elif opcion == 2:
            calcular_area_del_rombo()
        elif opcion == 3:
            calcular_volumen_del_cubo()
        elif opcion == 4:
            print("Saliendo...")
            break
        else:
            print(f"La opción '{opcion}' no existe")


menu()
