import json
from cliente import Cliente
from libro import Libro
import os

class Biblioteca:
    def __init__(self):
        self.libros = {}
        self.clientes = {}

    def agregar_libro(self, libro):
        if libro.id_libro not in self.libros:
            print("no está en la biblioteca")
            self.libros[libro.id_libro] = libro
        else:
            print("está")

    def agregar_clientes(self, cliente):
        if cliente.socio not in self.clientes:
            self.clientes[cliente.socio] = cliente
            print("agregado")
        else:
            print("duplicado")

    def imprimir_libros(self):
        for i in self.libros.keys():
            print(i)
        for l in self.libros.values():
            print(l)

    def imprimir_clientes(self):
        for d in self.clientes.values():
            print(d)


if __name__ == '__main__':

    # Construir la ruta del archivo JSON de libros
    libros_path = os.path.join('entrega2', 'data_libros.json')

    # Leer datos de libros desde el archivo JSON y guardarlos en una variable
    with open(libros_path, 'r') as fl:
        libros_data = json.load(fl)

    # Construir la ruta del archivo JSON de libros
    cliente_path = os.path.join('entrega2', 'data_clientes.json')

    # Leer datos de libros desde el archivo JSON y guardarlos en una variable
    with open(cliente_path, 'r') as fc:
        cliente_path = json.load(fc)


    # Imprimir los datos de libros para verificar
    print(libros_data)
    print(cliente_path)

    biblioteca = Biblioteca()

    cliente1 = Cliente(1, "claudio", 29000999, 11336699)
    cliente2 = Cliente(2, "pepe", 29000888, 11226699)
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
