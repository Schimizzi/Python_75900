import json
import os

from clases import Cliente
from clases import Libro
from clases import Libreria

if __name__ == '__main__':
    libreria = Libreria()
    
    # Cargo los clientes desde JSON en la bd de la libreria
    ruta_clientes = os.path.join('data', 'data_clientes.json')  # [!] MODIFICAR el path si es necesario
    try:
        with open(ruta_clientes, 'r') as archivo:
            datos_clientes = json.load(archivo)
            for info_cliente in datos_clientes:
                cliente = Cliente(
                    info_cliente['socio'],
                    info_cliente['nombre'],
                    info_cliente['dni'],
                    info_cliente['telefono']
                )
                libreria.agregar_cliente(cliente)
    except FileNotFoundError:
        print("data_clientes.json no encontrado. Comenzando con lista de clientes vacía.")
    
    # Cargo los libros desde JSON en la bd de la libreria
    ruta_libros = os.path.join('data', 'data_libros.json') # [!] MODIFICAR el path si es necesario!
    try:
        with open(ruta_libros, 'r') as archivo:
            datos_libros = json.load(archivo)
            for info_libro in datos_libros:
                libro = Libro(
                    info_libro['id_libro'],
                    info_libro['autor'],
                    info_libro['nombre_libro']
                )
                libreria.agregar_libro(libro)
    except FileNotFoundError:
        print("data_libros.json no encontrado")
    
    # crear clientes de forma manual 
    cliente1 = Cliente(1, "Claudio", 29000999, 11336699)
    cliente2 = Cliente(2, "Pepe", 29000888, 11226699)
    cliente7 = Cliente(7, "JuanJo", 29999000, 11333444)
    
    # crear libros de forma manual 
    libro1 = Libro(1, "Pedro", "Aprendiendo Python")
    libro2 = Libro(2, "Pablo", "Aprende a colorear desde cero")
    
    # agregar clientes
    libreria.agregar_cliente(cliente1)
    libreria.agregar_cliente(cliente2)
    libreria.agregar_cliente(cliente7)
    
    # agregar libros
    libreria.agregar_libro(libro1)
    libreria.agregar_libro(libro2)
    
    # quitar cliente activo
    libreria.quitar_cliente(cliente7)
    
    # quitar libro
    libreria.quitar_libro(libro1)
    
    # guardar clientes en JSON
    libreria.guardar_cliente_en_json(cliente2)
    libreria.guardar_cliente_en_json(cliente7)
    
    # Imprimir el historico de la libreria
    print("\n----- Historial de Libros en la libreria -----")
    libreria.imprimir_libros()
    print("\n----- Historial de clientes de la libreria -----")
    libreria.imprimir_clientes()

