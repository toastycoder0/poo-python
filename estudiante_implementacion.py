import os

from clase_estudiante import Estudiante

os.system("clear")

estudiante_uno = Estudiante("Luis", "23450611", 90)
print(estudiante_uno)
print("Esta aprobado" if estudiante_uno.estaAprobado() else "No esta aprobado")

estudiante_dos = Estudiante("Rafael", "88450611", 50)
print(estudiante_dos)
print("Esta aprobado" if estudiante_dos.estaAprobado() else "No esta aprobado")
