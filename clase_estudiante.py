import os


class Estudiante:
    def __init__(self, nombre, matricula, promedio):
        self.__nombre = nombre
        self.__matricula = matricula
        self.__promedio = promedio

    def consultarNombre(self):
        return self.__nombre

    def consultarMatricula(self):
        return self.__matricula

    def consultarPromedio(self):
        return self.__promedio

    def modificarNombre(self, valor):
        self.__nombre = valor

    def modificarMatricula(self, valor):
        self.__matricula = valor

    def modificarPromedio(self, valor):
        self.__promedio = valor

    def estaAprobado(self):
        return self.__promedio > 70

    def __str__(self):
        return f"""
Nombre: {self.__nombre}
Matricula: {self.__matricula}
Promedio: {self.__promedio}
        """


os.system("clear")

estudiante_uno = Estudiante("Luis", "23450611", 90)
print(estudiante_uno)
print("Esta aprobado" if estudiante_uno.estaAprobado() else "No esta aprobado")

estudiante_dos = Estudiante("Rafael", "88450611", 50)
print(estudiante_dos)
print("Esta aprobado" if estudiante_dos.estaAprobado() else "No esta aprobado")
