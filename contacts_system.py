class Contact:
    def __init__(self, name, number):
        self.__name = name
        self.__numbe = number

    @property
    def name(self):
        return self.__name

    @name.setter
    def set_name(self, value):
        self.__name = value

    @property
    def number(self):
        return self.__numbe

    @number.setter
    def set_number(self, value):
        self.__numbe = value


class Contacts:
    def __init__(self):
        self.__contacts = []

    def create_contact(self):
        name = input("\nIngresa el nombre del nuevo contacto: ")
        number = input(f"Ingresa el número de teléfono de {name}: ")

        new_contact = Contact(name, number)

        self.__contacts.append(new_contact)

        return f"Contacto {name} agregado"

    def delete_contact(self):
        name = input("\nIngresa el nombre del contacto a eliminar: ")

        for contact in self.__contacts:
            if contact.name == name:
                self.__contacts.remove(contact)

                return f"Contacto {name} eliminado"

        return f"El contacto {name} no existe"

    def __str__(self):
        if len(self.__contacts) == 0:
            return "\nNo hay contacto registrados"

        contacts_str = ""

        for contact in self.__contacts:
            index = self.__contacts.index(contact)
            contacts_str = f"""
Contacto {index + 1}
Nombre: {contact.name}
Teléfono: {contact.number}
            """

        return contacts_str


contacts = Contacts()

while True:
    print("""
Opciones:
1) Agregar un contacto
2) Mostrar los contactos
3) Eliminar un contacto
4) Salir
    """)

    option = input("Ingresa una opción: ")

    if option == "1":
        message = contacts.create_contact()
        print(message)
    elif option == "2":
        print(contacts)
    elif option == "3":
        message = contacts.delete_contact()
        print(message)
    elif option == "4":
        print("Saliendo....")
        break
    else:
        print(f'La opción ingresada "{option}" no es valida')
