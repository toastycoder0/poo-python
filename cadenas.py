"""
Leer una contraseña de usuario y determinar si es una contraseña segura,
considerando los siguientes requerimientos
1) Tener mas de 8 caracteres
2) Tener al menos 1 letra mayuscula
3) Contener al menos una minuscula
4) Contener un numero
5) Contener un guion bajo
"""

import os

os.system("clear")

clave_a_probar = ""


def tiene_longitud_valida():
    return len(clave_a_probar) > 7


def esta_en_rango(inicial, final):
    for letra in clave_a_probar:
        if ord(letra) in range(inicial, final):
            return True
    return False


def tiene_signo(signo):
    return signo in clave_a_probar


def validar_clave():
    global clave_a_probar

    while True:
        clave_a_probar = input("Introduce la contraseña a evaluar: ")

        if not tiene_longitud_valida():
            print("La contraseña debe tener más de 8 caracteres\n")
            continue

        if not esta_en_rango(97, 122):
            print("La contraseña debe contener al menos una minuscula\n")
            continue

        if not esta_en_rango(65, 91):
            print("La contraseña debe contener al menos una mayuscula\n")
            continue

        if not esta_en_rango(49, 57):
            print("La contraseña debe contener al menos un número\n")
            continue

        if not tiene_signo("_"):
            print("La contraseña debe contener al signo de '_'\n")
            continue

        print("La contraseña cumple con los parametros de seguridad")
        break


validar_clave()
