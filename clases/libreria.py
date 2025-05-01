import json
import os


class Libreria:
    def __init__(self):
        self.libros = {}
        self.clientes = {}

    def agregar_libro(self, libro):
        if libro.id_libro not in self.libros:
            self.libros[libro.id_libro] = libro
        else:
            print("El libro ya está en la libreria")

    def quitar_libro(self, libro):
        if libro.id_libro in self.libros:
            del self.libros[libro.id_libro]
        else:
            print("El libro no ya está en la libreria")


    def agregar_cliente(self, cliente):
        if cliente.socio not in self.clientes:
            self.clientes[cliente.socio] = cliente
            print(f"Se agregó el {cliente}")
        else:
            print("El cliente ya está registrado")

    def quitar_cliente(self, cliente):
        if cliente.socio in self.clientes:
            del self.clientes[cliente.socio]
            print(f"Se eliminó el cliente {cliente}")
        else:
            print("No es un cliente activo")

    def imprimir_libros(self):
        for libro in self.libros.values():
            print(libro)

    def imprimir_clientes(self):
        for cliente in self.clientes.values():
            print(cliente)

    def guardar_cliente_en_json(self, cliente):
        ruta_archivo = os.path.join('..', 'data_clientes.json')  # [!] MODIFICAR el path si es necesario
        try:
            with open(ruta_archivo, 'r') as archivo:
                datos_clientes = json.load(archivo)
        except FileNotFoundError:
            datos_clientes = []

        cliente_existe = False
        for c in datos_clientes:
            if cliente.socio == c['socio']:
                print(f"El cliente {c['nombre']} ya existe")
                cliente_existe = True
                break

        if not cliente_existe:
            datos_clientes.append({
                'socio': cliente.socio,
                'nombre': cliente.nombre,
                'dni': cliente.dni,
                'telefono': cliente.telefono
            })
            with open(ruta_archivo, 'w') as archivo:
                json.dump(datos_clientes, archivo, indent=4)
            print("Cliente guardado en data_clientes.json")
