# Hacer un programa que solicite al usuario 2 numeros enteros y crear las funciones, sumar, restar, mutiplicar y dividir.
# Mediante un menu principal solicitar al usuario 2 numeros, mostrar las opciones.
# Hacer el programa usando funciones
import os

os.system("clear")

numero_uno = float(input("Ingresa el primer número: "))
numero_dos = float(input("Ingresa el segundo número: "))


def sumar():
    suma = numero_uno + numero_dos
    print(f"La suma de {numero_uno} y {numero_dos} es {suma:.2f}")


def restar():
    resta = numero_uno - numero_dos
    print(f"La resta de {numero_uno} y {numero_dos} es {resta:.2f}")


def multiplicar():
    multiplicacion = numero_uno * numero_dos
    print(f"La multiplicacion de {numero_uno} y {numero_dos} es {multiplicacion:.2f}")


def dividir():
    division = numero_uno / numero_dos
    print(f"La división de {numero_uno} y {numero_dos} es {division:.2f}")


def menu():
    while True:
        print("""
Opciones

1) Sumar
2) Restar
3) Multiplicar
4) Dividir
5) Salir
            """)

        opcion = int(input("Ingresa una opción: "))

        if opcion == 1:
            sumar()
        elif opcion == 2:
            restar()
        elif opcion == 3:
            multiplicar()
        elif opcion == 4:
            dividir()
        elif opcion == 5:
            print("Saliendo...")
            break
        else:
            print(f"Opcion '{opcion}' no valida")


menu()
