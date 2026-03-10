import math

letras = [
    "a",
    "b",
    "c",
    "d",
    "e",
    "f",
    "g",
    "h",
    "i",
    "j",
    "k",
    "l",
    "m",
    "n",
    "ñ",
    "o",
    "p",
    "q",
    "r",
    "s",
    "t",
    "u",
    "v",
    "w",
    "x",
    "y",
    "z",
    " ",
]


def obtener_coprimo(F_n):
    E = 2
    while True:
        if math.gcd(E, F_n) == 1:
            break
        E += 1
    return E


def generar_clave_privada(F_n, E):
    D = 0
    K = 1
    while True:
        d = ((K * F_n) + 1) / E
        if d.is_integer():
            D = int(d)
            break
        K += 1
    return D


def separar_en_bloques(codigo, digitos_max):
    bloques = []
    for indice in range(0, len(codigo), digitos_max):
        indice_final = indice + digitos_max
        bloques.append(codigo[indice:indice_final])
    return bloques


def encriptar_mensaje():
    mensaje = input("\nIngresa el mensaje: ")
    p = int(input("Ingresa el primer número primo (p): "))
    q = int(input("Ingresa el segundo número primo (q): "))

    n = p * q
    F_n = (p - 1) * (q - 1)

    E = obtener_coprimo(F_n)
    D = generar_clave_privada(F_n, E)

    digitos_max = len(str(n))
    mensaje_encriptado = ""

    for letra in mensaje.lower():
        codigo_de_letra = letras.index(letra) + 1
        letra_encriptada = str(pow(codigo_de_letra, E, n)).zfill(digitos_max)
        mensaje_encriptado += letra_encriptada

    print(f"""
Mensaje original: {mensaje}
Mensaje encriptado: {mensaje_encriptado}
Llave pública (n:{n}, E:{E})
Llave privada D:{D}
    """)


def desencriptar_mensaje():
    codigo = input("\nIngresa el mensaje a desencriptar: ")
    n = int(input("Ingresa la primera parte de la llave publica (n): "))
    D = int(input("Ingresa la llave privada (D): "))

    digitos_max = len(str(n))
    bloques = separar_en_bloques(codigo, digitos_max)

    mensaje_descifrado = ""

    for bloque in bloques:
        c = int(bloque)
        m = pow(c, D, n)
        if 1 <= m <= len(letras):
            mensaje_descifrado += letras[m - 1]
        else:
            mensaje_descifrado += "?"

    print(f"""
Mensaje encriptado: {codigo}
Mensaje original: {mensaje_descifrado}
    """)


def menu():
    while True:
        print("""
Opciones:
1) Encriptar mensaje
2) Desencriptar mensaje
3) Salir
        """)
        opcion = input("Ingresa una opción: ")

        if opcion == "1":
            encriptar_mensaje()
        elif opcion == "2":
            desencriptar_mensaje()
        elif opcion == "3":
            print("Saliendo...")
            break
        else:
            print(f"La opción '{opcion}' no es valida")


menu()
