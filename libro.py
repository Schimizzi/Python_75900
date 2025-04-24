
class Libro:
    def __init__(self, id_libro, autor, nombre_libro):
        self.id_libro = id_libro
        self.autor = autor
        self.nombre_libro = nombre_libro
        self.esta_prestado = False

    def __str__(self): # metodo especial
        return f"Tenemos el libro '{self.nombre_libro}' del autor '{self.autor}', {"prestado" if self.esta_prestado else "para prestar"}"
