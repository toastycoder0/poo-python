"""
Definir una superclase llamada vehiculo con lo siguiente
Atributos:
- Matricula
- Modelo
- Potencia (en CV)
Metodos get y set con decoradores

Definir una subclase llamada Taxi
Atributos:
- Numero de licencia
- Hereda los del padre
Metodos get y set con decoradores

Definir una subclase llamada Autobus
Atributos:
- Numero de plazas
- Hereda los del padre
Metodos get y set con decoradores

Crear 3 objetos
- Un objeto vehiculo
- Un objeto Taxi
- Un objeto Autobus
"""

import os

os.system("clear")


class Vehiculo:
    def __init__(self, matricula, modelo, potencia):
        self.__matricula = matricula
        self.__modelo = modelo
        self.__potencia = potencia

    def __str__(self):
        return f"Matricula:{self.__matricula}\nModelo:{self.__modelo}\nPotencia:{self.__potencia}\n"

    @property
    def matricula(self):
        return self.__matricula

    @property
    def modelo(self):
        return self.__modelo

    @property
    def potencia(self):
        return self.__potencia

    @matricula.setter
    def matricula(self, valor):
        self.__matricula = valor

    @modelo.setter
    def modelo(self, valor):
        self.__modelo = valor

    @potencia.setter
    def potencia(self, valor):
        self.__potencia = valor


class Taxi(Vehiculo):
    def __init__(self, matricula, modelo, potencia, licencia):
        super().__init__(matricula, modelo, potencia)
        self.__licencia = licencia

    def __str__(self):
        return f"{super().__str__()}Licencia:{self.__licencia}\n"

    @property
    def licencia(self):
        return self.__licencia

    @licencia.setter
    def licencia(self, valor):
        self.__licencia = valor


class Autobus(Vehiculo):
    def __init__(self, matricula, modelo, potencia, numero_de_plazas):
        super().__init__(matricula, modelo, potencia)
        self.__numero_de_plazas = numero_de_plazas

    def __str__(self):
        return f"{super().__str__()}Número de plazas:{self.__numero_de_plazas}\n"

    @property
    def numero_de_plazas(self):
        return self.__numero_de_plazas

    @numero_de_plazas.setter
    def licencia(self, valor):
        self.__numero_de_plazas = valor


vehiculo = Vehiculo("12HJR", "Toyota Corolla", 125)
taxi = Taxi("22LKM", "Nissan Versa", 450, "LIC-48392017-MX")
autobus = Autobus("34RTS", "Mercedes-Benz O500", 122, 47)

print(vehiculo)
print(autobus)
print(taxi)
