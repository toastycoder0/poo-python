# Solicitar al usuario el tamaño de una matriz n por m y llenar la matriz con
# datos solicitados desde el teclado y crear otra matriz del mismo tamaño de numeros
# aleatorios generados entre 0 y 99, agregar multiplicacion de matrices
import os
import random

os.system("clear")

filas_a_crear = int(input("Ingresa el número de filas: "))
columnas_a_crear = int(input("Ingresa el número de columnas: "))

matriz = []
matriz_random = []
matriz_combinada = []
matriz_multiplicada = []

for numero_de_fila in range(filas_a_crear):
    fila_combinada = []
    fila_random = []

    for numero_de_columna in range(columnas_a_crear):
        valor = int(
            input(
                f"Ingresa el valor en la posición [{numero_de_fila}][{numero_de_columna}]: "
            )
        )
        valor_random = random.randint(0, 100)

        fila_combinada.append(valor)
        fila_random.append(valor_random)

    matriz.append(fila_combinada)
    matriz_random.append(fila_random)

for numero_de_fila in range(filas_a_crear):
    fila_combinada = []

    for numero_de_columna in range(columnas_a_crear):
        valor_combinado = (
            matriz[numero_de_fila][numero_de_columna]
            + matriz_random[numero_de_fila][numero_de_columna]
        )
        fila_combinada.append(valor_combinado)

    matriz_combinada.append(fila_combinada)

if columnas_a_crear == filas_a_crear:
    for numero_de_fila in range(filas_a_crear):
        fila_multiplicada = []

        for numero_de_columna in range(columnas_a_crear):
            multiplicacion_acumulada = 0

            for numero_intermedio in range(columnas_a_crear):
                multiplicacion_acumulada += (
                    matriz[numero_de_fila][numero_intermedio]
                    * matriz_random[numero_intermedio][numero_de_columna]
                )

            fila_multiplicada.append(multiplicacion_acumulada)

        matriz_multiplicada.append(fila_multiplicada)

    print(f"Matriz multiplicada: {matriz_multiplicada}")

print(f"Matriz ingresada: {matriz}")
print(f"Matriz random: {matriz_random}")
print(f"Matriz combinada: {matriz_combinada}")

if len(matriz_multiplicada) > 0:
    print(f"Matriz multiplicada: {matriz_multiplicada}")
else:
    print("No se pueden multiplicar el número de columnas y filas no es igual")
