import os

os.system("clear")


def ListaPrimos():
    numero = int(input("Ingresa el número a verificar: "))

    for numero_en_rango in range(2, numero + 1):
        for divisor in range(2, numero_en_rango):
            if numero_en_rango % divisor == 0:
                break
        else:
            print(numero_en_rango)


ListaPrimos()
