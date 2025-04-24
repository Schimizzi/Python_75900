

class Cliente:
    def __init__(self,socio, nombre, dni, telefono):
        self.socio = socio
        self.nombre = nombre
        self.dni = dni
        self.telefono = telefono
        self.clientes = {}

    def datos_clientes(self, cliente):
        if cliente not in self.clientes.values():
            self.clientes[self.socio] = cliente
            print("agregado")
        else: print("duplicado")

    def __str__(self):
        return f"socio: {self.socio}, nombre: {self.nombre}, dni: {self.dni}, telefono: {self.telefono}"
    
    def imprimir_datos(self):
        for d in self.clientes:
            print(d)


cliente1 = Cliente(1, "claudio" , 29000999, 11336699)
cliente2 = Cliente(2, "pepe" , 29000888, 11226699)
        
cliente1.imprimir_datos()