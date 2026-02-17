import os

os.system("clear")

money = 100

while True:
    option = int(
        input("""
ATM Opciones

1) Consultar saldo
2) Depositar dinero
3) Retirar dinero
4) Salir

Ingresa una opción: 
""")
    )

    match option:
        case 1:
            print(f"Tu saldo es de ${money:.2f}")
        case 2:
            new_quantity = int(input("Ingresa la cantidad a depositar: "))
            money += new_quantity
        case 3:
            new_quantity = int(input("Ingresa la cantidad a retirar: "))
            if new_quantity > money:
                print("Fondos insuficientes")
            else:
                money -= new_quantity
                print(f"Tu saldo restante es de ${money:.2f}")
        case 4:
            print("Saliendo....")
            break
        case _:
            print(f"La opción ingresada {option} no es correcta")
