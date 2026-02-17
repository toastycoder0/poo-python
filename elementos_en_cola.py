# Hacer un programa que muestre un menu de opciones con las siguientes opciones:
# Opcion 1 agregar elemento
# Opcion 2 eliminar elemento (como cola)
# Opcion 3 mostrar elementos
# Opcion 4 salir
import os

os.system("clear")

lista = []


while True:
    print("""
Opciones (colas): 
1) Agregar elemento
2) Eliminar elemento
3) Mostrar elementos
4) Salir
    """)
    opcion = int(input("Selecciona una opción: "))

    if opcion == 1:
        nuevo_elemento = int(input("Ingresa el nuevo elemento: "))
        lista.append(nuevo_elemento)
    elif opcion == 2:
        if len(lista) > 0:
            elemento_eliminado = lista.pop(0)
        else:
            print("La cola está vacía")
    elif opcion == 3:
        print("Elementos en la cola:")
        for elemento in lista:
            print(elemento)
    elif opcion == 4:
        break
    else:
        print("Opción no disponible")
