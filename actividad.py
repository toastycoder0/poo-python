"""
Elaborar un programa, que cree 2 funciones para
calcular el minímo comun multiplo y el maximo comun
divisor de 2 números enteros leidos desde el teclado
"""

import os

os.system("clear")


def obtener_mcm(numero, numero_dos):
    mcm = max(numero, numero_dos)

    while True:
        if mcm % numero == 0:
            if mcm % numero_dos == 0:
                return mcm
        mcm += 1


def obtener_mcd(numero, numero_dos):
    while numero != numero_dos:
        if numero > numero_dos:
            numero -= numero_dos
        else:
            numero_dos -= numero
    return numero


def menu():
    numero = int(input("Ingresa un número: "))
    numero_dos = int(input("Ingresa otro número: "))

    mcm = obtener_mcm(numero, numero_dos)
    mcd = obtener_mcd(numero, numero_dos)

    print(f"""
El MCM de {numero} y {numero_dos} es {mcm}
El MCD de {numero} y {numero_dos} es {mcd}
    """)


menu()
