import os

os.system("clear")

lista_uno = ["Rojo", "Rosa", "Morado", "Azul", "Amarillo", "Magenta", "Turquesa"]
lista_dos = ["Gris", "Naranja", "Azul", "Amarillo", "Verde", "Blanco", "Negro"]


def palabras_en_ambas():
    palabras_en_ambas_listas = []
    for palabra in lista_uno:
        if palabra in lista_dos:
            palabras_en_ambas_listas.append(palabra)
    return palabras_en_ambas_listas


def palabras_solo_en_lista_uno():
    palabras_solo_en_lista_uno = []
    for palabra in lista_uno:
        if not palabra in lista_dos:
            palabras_solo_en_lista_uno.append(palabra)
    return palabras_solo_en_lista_uno


def palabras_solo_en_lista_dos():
    pass


def principal():
    palabras = palabras_en_ambas()
    palabras_en_uno = palabras_solo_en_lista_uno()
    print("Palabras en ambas: ", palabras)
    print("Palabras en lista uno: ", palabras_en_uno)


principal()
