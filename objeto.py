class Usuario:
    def __init__(self, nombre, correo, clave):
        self.nombre = nombre
        self.correo = correo
        self.__clave = clave

    @property
    def clave(self):
        return self.__clave

    @clave.setter
    def clave(self, value):
        self.__clave = value


usuario_uno = Usuario("Jose", "jose@gmail.com", "123456")
