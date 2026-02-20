import os

os.system("clear")

cash = 0
movements = []


def check_balance():
    print(f"\nTu saldo actual es de ${cash:.2f}")


def deposit_money():
    global cash
    new_quantity = int(input("\nIngresa la cantidad a depositar: "))
    cash += new_quantity
    movements.append(
        ["Deposito", f"Cantidad: ${new_quantity:.2f}", f"Saldo: ${cash:.2f}"]
    )
    print(f"""
Se agregaron ${new_quantity:.2f} a tu cuenta
Tu saldo total es de ${cash:.2f}
    """)


def withdraw_money():
    global cash
    new_quantity = int(input("\nIngresa la cantidad a retirar: "))
    if new_quantity > cash:
        print("Saldo insuficiente")
        return
    cash -= new_quantity
    movements.append(
        ["Retiro", f"Cantidad: ${new_quantity:.2f}", f"Saldo: ${cash:.2f}"]
    )
    print(f"""
Se retiraron ${new_quantity:.2f} de tu cuenta
Tu saldo total es de ${cash:.2f}
    """)


def check_movements():
    number_of_movements = len(movements)

    if number_of_movements > 0:
        print("\n")
        for movement_index in range(number_of_movements):
            movement_message = ""
            for movement_detail in movements[movement_index]:
                movement_message += movement_detail + "\n"
            print(f"""Movimiento {movement_index + 1}\n{movement_message}""")
    else:
        print("\nNo hay movimientos registrados")


def main():
    while True:
        print("""
Opciones

1) Ver saldo
2) Depositar
3) Retirar
4) Ver los movimientos realizados
5) Salir
        """)

        opt = int(input("Ingresa una opción: "))

        if opt == 1:
            check_balance()
        elif opt == 2:
            deposit_money()
        elif opt == 3:
            withdraw_money()
        elif opt == 4:
            check_movements()
        elif opt == 5:
            print("\nSaliendo...")
            break
        else:
            print("\nLa opción ingresada no es valida")


main()
