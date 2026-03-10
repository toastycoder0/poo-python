"""
Hacer un programa que lea una cadena que contenga letras
en mayusculas y minusculas, que genere una nueva cadena
cambiando la mayusculas por minusculas y las minusculas
por mayusculas
"""

import os

os.system("clear")


def convertir_letras(cadena):
    cadena_modificada = ""
    for letra in cadena:
        letra_asci = ord(letra)
        if letra_asci in range(97, 122):
            cadena_modificada += letra.upper()
        elif letra_asci in range(65, 91):
            cadena_modificada += letra.lower()
        else:
            cadena_modificada += letra
    return cadena_modificada


def menu():
    cadena = input("Ingresa una cadena de texto: ")
    cadena_modificada = convertir_letras(cadena)
    print(f"Cadena modificada: {cadena_modificada}")


menu()
