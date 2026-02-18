# Solicitar al usuario el tamaño de una matriz n por m y llenar la matriz con
# datos solicitados desde el teclado y crear otra matriz del mismo tamaño de numeros
# aleatorios generados entre 0 y 99
import os
import random

os.system("clear")

filas_a_crear = int(input("Ingresa el valor de filas: "))
columnas_a_crear = int(input("Ingresa el valor de columnas: "))

matriz = []
matriz_random = []

for numero_de_fila in range(filas_a_crear):
    fila = []
    fila_random = []

    for numero_de_columna in range(columnas_a_crear):
        valor = int(
            input(
                f"Ingresa el valor en la posición [{numero_de_fila}][{numero_de_columna}]: "
            )
        )
        valor_random = random.randint(0, 100)

        fila.append(valor)
        fila_random.append(valor_random)

    matriz.append(fila)
    matriz_random.append(fila_random)

print(f"Matriz ingresada: {matriz}")
print(f"Matriz random: {matriz_random}")
