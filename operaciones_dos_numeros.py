import os

os.system("clear")

numero_uno = int(input("Ingresa el primer número: "))
numero_dos = int(input("Ingresa el segundo número: "))


def sumar():
    print(
        f"La suma de {numero_uno} más {numero_dos} es igual a {numero_uno + numero_dos}"
    )


def restar():
    print(
        f"La resta de {numero_uno} menos {numero_dos} es igual a {numero_uno - numero_dos}"
    )


def multiplicar():
    print(
        f"La multiplicación de {numero_uno} por {numero_dos} es igual a {numero_uno * numero_dos}"
    )


def dividir():
    print(
        f"La divición de {numero_uno} entre {numero_dos} es igual a {(numero_uno / numero_dos):.2f}".rstrip(
            "0"
        ).rstrip(".")
    )


def menu():
    while True:
        print("""
Opciones: 

1) Suma
2) Resta
3) Multiplicación
4) División
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
            print("Opcion no valida")


menu()
