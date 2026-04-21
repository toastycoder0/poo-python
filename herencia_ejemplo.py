class Persona:
    def __init__(self, name, aPaterno, aMaterno):
        self._nombre = name
        self._apePaterno = aPaterno
        self._apeMaterno = aMaterno

    @property
    def name(self):
        return self._nombre

    @name.setter
    def name(self, newName):
        self._name = newName

    @property
    def firstLastName(self):
        return self._apePaterno

    @firstLastName.setter
    def firstLastName(self, newLastName):
        self._apePaterno = newLastName

    @property
    def secondtLastName(self):
        return self._apeMaterno

    @secondtLastName.setter
    def secondtLastName(self, newLastName):
        self._apeMaterno = newLastName

    def __str__(self):
        return f"""{self._nombre} {self._apePaterno}
        {self._apeMaterno}"""

    def descontar(self):
        return 0


class Alumno(Persona):
    def __init__(self, name, aPaterno, aMaterno, career):
        super().__init__(name, aPaterno, aMaterno)
        # Le estoy hablando al constructor padre
        self._carrera = career

    @property
    def career(self):
        return self._carrera

    @career.setter
    def career(self, newCareer):
        self._carrera = newCareer

    def __str__(self):
        return f"{super().__str__()}, {self._carrera}"

    def descontar(self):
        return 0.5


class Maestro(Persona):
    def __init__(self, name, aPaterno, aMaterno, profession):
        super().__init__(name, aPaterno, aMaterno)
        self._profesion = profession

    @property
    def profession(self):
        return self._profesion

    @profession.setter
    def profession(self, newProfession):
        self._profesion = newProfession

    def __str__(self):
        return f"{super().__str__()}, {self._profesion}"

    def descontar(self):
        return 0.25


persona1 = Persona("Luis", "Alor", "Vazques")
print(f"Persona: {persona1}")
print(f"Descuento: {persona1.descontar() * 100}%")
alumno1 = Alumno("Saul", "Morales", "Jimenes", "Ingenieria en sistemas")
print(f"Alumno: {alumno1}")
print(f"Descuento: {alumno1.descontar() * 100}%")
maestro1 = Maestro("Francisco", "Huerta", "Perez", "Ing. Electronico")
print(f"Maestro: {maestro1}")
print(f"Descuento: {maestro1.descontar() * 100}%")
