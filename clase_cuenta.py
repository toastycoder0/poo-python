from abc import ABC, abstractmethod


class Persona:
    def __init__(self, nombre, apellidos, nif):
        self.__nombre = nombre
        self.__apellidos = apellidos
        self.__nif = nif

    def __str__(self):
        return (
            f"Nombre:{self.__nombre}\nApellidos:{self.__apellidos}\nNIF:{self.__nif}\n"
        )

    @property
    def nombre(self):
        return self.__nombre

    @nombre.setter
    def nombre(self, valor):
        self.__nombre = valor

    @property
    def apellidos(self):
        return self.__apellidos

    @apellidos.setter
    def apellidos(self, valor):
        self.__apellidos = valor

    @property
    def nif(self):
        return self.__nif

    @nif.setter
    def nif(self, valor):
        self.__nif = valor


class Cuenta(ABC):
    def __init__(self, cliente, numero_cuenta):
        self.__cliente = cliente
        self.__numero_cuenta = numero_cuenta
        self.__saldo = 0.00

    def __str__(self):
        return f"Cliente:\n{self.__cliente}Número de Cuenta:{self.__numero_cuenta}\nSaldo:{self.__saldo:.2f}\n"

    @property
    def cliente(self):
        return self.__cliente

    @property
    def numero_cuenta(self):
        return self.__numero_cuenta

    @property
    def saldo(self):
        return self.__saldo

    @cliente.setter
    def cliente(self, valor):
        self.__cliente = valor

    @numero_cuenta.setter
    def numero_cuenta(self, valor):
        self.__numero_cuenta = valor

    @saldo.setter
    def saldo(self, valor):
        self.__saldo = valor

    def ingresar(self, cantidad):
        self.__saldo += cantidad

    @abstractmethod
    def retirar(self, cantidad):
        pass

    @abstractmethod
    def actualizar_saldo(self):
        pass


class CuentaCorriente(Cuenta):
    def __init__(self, cliente, numero_cuenta):
        super().__init__(cliente, numero_cuenta)
        self.__interes_fijo = 1.5

    def __str__(self):
        return f"{super().__str__()}Tipo:Cuenta Corriente\nInterés Fijo:{self.__interes_fijo}%\n"

    def actualizar_saldo(self):
        interes_calculado = self.saldo * (self.__interes_fijo / 100)
        nuevo_saldo = self.saldo + interes_calculado
        self.saldo = nuevo_saldo

    def retirar(self, cantidad):
        if self.saldo < cantidad:
            return NotImplemented
        self.saldo -= cantidad


class CuentaAhorro(Cuenta):
    def __init__(self, cliente, numero_cuenta, interes_variable, saldo_minimo):
        super().__init__(cliente, numero_cuenta)
        self.__interes_variable = interes_variable
        self.__saldo_minimo = saldo_minimo

    def __str__(self):
        return f"{super().__str__()}Tipo:Cuenta Ahorro\nInterés Variable:{self.__interes_variable}%\nSaldo Mínimo:{self.__saldo_minimo:.2f}\n"

    @property
    def interes_variable(self):
        return self.__interes_variable

    @interes_variable.setter
    def interes_variable(self, valor):
        self.__interes_variable = valor

    def actualizar_saldo(self):
        interes_agregado = self.saldo * (self.__interes_variable / 100)
        nuevo_saldo = self.saldo + interes_agregado
        self.saldo = nuevo_saldo

    def retirar(self, cantidad):
        saldo_restante = self.saldo - cantidad
        if saldo_restante < self.__saldo_minimo:
            return NotImplemented
        self.saldo -= cantidad


persona = Persona("Rick", "Sanchez", "C-137-MX")
cuenta_corriente = CuentaCorriente(persona, 10002000)
cuenta_de_ahorro = CuentaAhorro(persona, 30004000, 0.5, 500.0)

cuenta_corriente.ingresar(1000)
cuenta_corriente.actualizar_saldo()

cuenta_de_ahorro.ingresar(2000)
cuenta_de_ahorro.retirar(1600)

print(cuenta_corriente)
print(cuenta_de_ahorro)
