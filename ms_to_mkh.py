# Hacer un programa que convierta las unidades de velocidad en m/s a km/h,
# el programa debera pedir al usuario la velocidad expresada en m/s
# y debera imprimir su equivalente en km/h,
# imprimir eil resultado de la conversion redondeado a 2 decimales
import os


os.system("clear")

velocidad_en_ms = float(input("Ingresa la velocidad a convertir (en m/s): "))

velocidad_en_kmh = velocidad_en_ms * (3600 / 1000)

print(
    f"El valor de {velocidad_en_ms:.2f} m/s en km/h es de {velocidad_en_kmh:.2f}",
)
