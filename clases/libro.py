
class Libro:
    def __init__(self, id_libro, autor, nombre_libro, esta_vendido = False):
        self.id_libro = id_libro
        self.autor = autor
        self.nombre_libro = nombre_libro
        self.esta_vendido = esta_vendido

    def __str__(self): # metodo especial
        return f"Tenemos el libro '{self.nombre_libro}' del autor '{self.autor}', {"vendido" if self.esta_vendido else "para vender"}"
