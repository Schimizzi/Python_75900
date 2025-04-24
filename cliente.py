

class Cliente:
    def __init__(self,socio, nombre, dni, telefono):
        self.socio = socio
        self.nombre = nombre
        self.dni = dni
        self.telefono = telefono

    def __str__(self):
        return f"socio: {self.socio}, nombre: {self.nombre}, dni: {self.dni}, telefono: {self.telefono}"

    