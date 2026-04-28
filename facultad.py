"""
1. Se pretende realizar una aplicación para esta facultad que gestione la información sobre las personas
vinculadas con la misma, que se pueden clasificar en tres tipos: estudiantes, profesores y personal de servicio.
A continuación, se detalla qué tipo de información debe gestionar esta aplicación:
* Por cada persona, se debe conocer, al menos, su nombre y apellidos, su número de identificación y su estado civil.
* Con respecto a los empleados, sean del tipo que sean, hay que saber su año de incorporación a la facultad y qué
  número de despacho tienen asignado.
* En cuanto a los estudiantes, se requiere almacenar el curso en el que están matriculados.
* Por lo que se refiere a los profesores, es necesario gestionar a qué departamento pertenecen
  (lenguajes, matemáticas, arquitectura, ...).
* Sobre el personal de servicio, hay que conocer a qué sección están asignados (biblioteca, decanato, secretaría, ...).

El ejercicio consiste, en primer lugar, en definir la jerarquía de clases de esta aplicación. A continuación, debe programar
las clases definidas en las que, además de los constructores, hay que desarrollar los métodos correspondientes a
las siguientes acciones:

* Cambio del estado civil de una persona.
* Reasignación de despacho a un empleado.
* Matriculación de un estudiante en un nuevo curso.
* Cambio de departamento de un profesor.
* Traslado de sección de un empleado del personal de servicio.
* Imprimir toda la información de cada tipo de individuo.
"""


class Persona:
    def __init__(self, nombre, apellido, numero_identificacion, estado_civil):
        self.__nombre = nombre
        self.__apellido = apellido
        self.__numero_identificacion = numero_identificacion
        self.__estado_civil = estado_civil

    @property
    def nombre(self):
        return self.__nombre

    @nombre.setter
    def nombre(self, valor):
        self.__nombre = valor

    @property
    def apellido(self):
        return self.__apellido

    @apellido.setter
    def apellido(self, valor):
        self.__apellido = valor

    @property
    def numero_identificacion(self):
        return self.__numero_identificacion

    @numero_identificacion.setter
    def numero_identificacion(self, valor):
        self.__numero_identificacion = valor

    @property
    def estado_civil(self):
        return self.__estado_civil

    @estado_civil.setter
    def estado_civil(self, valor):
        self.__estado_civil = valor

    def cambiar_estado_civil(self, nuevo_estado):
        self.__estado_civil = nuevo_estado

    def __str__(self):
        return f"""Nombre: {self.__nombre} {self.__apellido}
ID: {self.__numero_identificacion}
Estado civil: {self.__estado_civil}"""


class Empleado(Persona):
    def __init__(
        self,
        nombre,
        apellido,
        numero_identificacion,
        estado_civil,
        incorporacion,
        numero_despacho,
    ):
        super().__init__(nombre, apellido, numero_identificacion, estado_civil)
        self.__incorporacion = incorporacion
        self.__numero_despacho = numero_despacho

    @property
    def incorporacion(self):
        return self.__incorporacion

    @incorporacion.setter
    def incorporacion(self, valor):
        self.__incorporacion = valor

    @property
    def numero_despacho(self):
        return self.__numero_despacho

    @numero_despacho.setter
    def numero_despacho(self, valor):
        self.__numero_despacho = valor

    def reasignar_despacho(self, nuevo_despacho):
        self.__numero_despacho = nuevo_despacho

    def __str__(self):
        return f"{super().__str__()}\nAño de incorporación: {self.__incorporacion}\nNúmero de despacho: {self.__numero_despacho}"


class Estudiante(Persona):
    def __init__(self, nombre, apellido, numero_identificacion, estado_civil, curso):
        super().__init__(nombre, apellido, numero_identificacion, estado_civil)
        self.__curso = curso

    @property
    def curso(self):
        return self.__curso

    @curso.setter
    def curso(self, valor):
        self.__curso = valor

    def matricular_curso_nuevo(self, curso_nuevo):
        self.__curso = curso_nuevo

    def __str__(self):
        return f"{super().__str__()}\nCurso: {self.__curso}"


class Profesor(Persona):
    def __init__(
        self,
        nombre,
        apellido,
        numero_identificacion,
        estado_civil,
        departamento,
    ):
        super().__init__(nombre, apellido, numero_identificacion, estado_civil)
        self.__departamento = departamento

    @property
    def departamento(self):
        return self.__departamento

    @departamento.setter
    def departamento(self, valor):
        self.__departamento = valor

    def cambio_departamento(self, nuevo_departamento):
        self.__departamento = nuevo_departamento

    def __str__(self):
        return f"{super().__str__()}\nDepartamento: {self.__departamento}"


class PersonalServicio(Persona):
    def __init__(
        self,
        nombre,
        apellido,
        numero_identificacion,
        estado_civil,
        seccion,
    ):
        super().__init__(nombre, apellido, numero_identificacion, estado_civil)
        self.__seccion = seccion

    @property
    def seccion(self):
        return self.__seccion

    @seccion.setter
    def seccion(self, valor):
        self.__seccion = valor

    def traslado_seccion(self, nueva_seccion):
        self.__seccion = nueva_seccion

    def __str__(self):
        return f"{super().__str__()}\nSección: {self.__seccion}"


empleado = Empleado("Juan", "Pérez", "12345678", "Soltero", 2020, "101A")
estudiante = Estudiante("Ana", "Gómez", "87654321", "Soltera", "Ingeniería Informática")
profesor = Profesor("Carlos", "Martínez", "11223344", "Casado", "Matemáticas")
personal_de_servicio = PersonalServicio(
    "María", "López", "99887766", "Viuda", "Mantenimiento"
)

print(empleado, "\n")
print(estudiante, "\n")
print(profesor, "\n")
print(personal_de_servicio, "\n")
