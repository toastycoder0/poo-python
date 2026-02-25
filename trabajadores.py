class Trabajador:
    def __init__(self, nombre, puesto, salario_por_hora, horas_trabajadas, bono):
        self.name = nombre
        self.puesto = puesto
        self.salario_por_hora = salario_por_hora
        self.horas_trabajadas = horas_trabajadas
        self.bono = bono

    def obtener_salario_por_horas_trabajadas(self):
        salario_por_horas_trabajadas = self.salario_por_hora * self.horas_trabajadas
        print(
            f"El sueldo de {self.name} por {self.horas_trabajadas}h es de: ${salario_por_horas_trabajadas:.2f}"
        )

    def obtener_salario_con_bono(self):
        salario_con_bono = (self.salario_por_hora * self.horas_trabajadas) + self.bono
        print(f"El sueldo de {self.name} + bono es de: ${salario_con_bono:.2f}")


for trabajador in range(2):
    nombre = input(f"Ingresa el nombre del trabajador {trabajador + 1}: ")
    puesto = input(f"Ingresa el nombre del puesto del trabajador {trabajador + 1}: ")
    salario_por_hora = int(
        input(f"Ingresa el salario por hora del trabajador {trabajador + 1}: ")
    )
    bono = int(
        input(
            f"Ingresa la cantidad del bono que recibe el trabajador {trabajador + 1}: "
        )
    )
    horas_trabajadas = int(
        input(f"Ingresa la cantidad de horas trabajadas por {nombre}: ")
    )

    nuevo_trabajador = Trabajador(
        nombre, puesto, salario_por_hora, horas_trabajadas, bono
    )
    nuevo_trabajador.obtener_salario_por_horas_trabajadas()
    nuevo_trabajador.obtener_salario_con_bono()
