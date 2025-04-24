class Cliente:
    def __init__(self,socio, nombre, dni, telefono):
        self.socio = socio
        self.nombre = nombre
        self.dni = dni
        self.telefono = telefono
        


    def __str__(self):
        return f"socio: {self.socio}, nombre: {self.nombre}, dni: {self.dni}, telefono: {self.telefono}"
    

class Libro:
    def __init__(self, id_libro, autor, nombre_libro):
        self.id_libro = id_libro
        self.autor = autor
        self.nombre_libro = nombre_libro
        self.esta_prestado = False

    def __str__(self): # metodo especial
        return f"Tenemos el libro '{self.nombre_libro}' del autor '{self.autor}', {"prestado" if self.esta_prestado else "para prestar"}"


class Biblioteca:
    def __init__(self):
        self.libros = {} # {1: Libro(1, "Pedro", "Aprendiendo Python"), 2: Libro(2, "Pablo", "Aprende a colorear desde cero")}
        self.clientes = {}

    def agregar_libro(self, libro):
        if libro.id_libro not in self.libros:
            print("no está en la biblioteca")
            self.libros[libro.id_libro] = libro
        else: print("está")

    def agregar_clientes(self, cliente):
        if cliente.socio not in self.clientes:
            self.clientes[cliente.socio] = cliente
            print("agregado")
        else: print("duplicado")


    def imprimir_libros(self):
        for i in self.libros.keys():
            print(i)
        for l in self.libros.values():
            print(l)

    def imprimir_clientes(self):
        for d in self.clientes.values():
            print(d)


if __name__ == '__main__':
    biblioteca = Biblioteca()

    cliente1 = Cliente(1, "claudio" , 29000999, 11336699)
    cliente2 = Cliente(2, "pepe" , 29000888, 11226699)
    libro1 = Libro(3, "Pedro", "Aprendiendo Python")
    libro2 = Libro(4, "Pablo", "Aprende a colorear desde cero")
    print(libro1)

    biblioteca.agregar_libro(libro1)
    biblioteca.agregar_libro(libro2)
    biblioteca.agregar_libro(libro1)
    biblioteca.agregar_clientes(cliente1)
    biblioteca.agregar_clientes(cliente2)
    biblioteca.imprimir_libros()
    biblioteca.imprimir_clientes()

