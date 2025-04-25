import os
import json

def data_libros():
    # cambiar el path para leer el archivo json
    libros_path = os.path.join('entrega2', 'data_libros.json')

    with open(libros_path, 'r') as fl:
        libros_data = json.load(fl)

    for i in libros_data:
        print(i)
    
""" 
# cambiar el path para leer el archivo json
cliente_path = os.path.join('entrega2', 'data_clientes.json')

with open(cliente_path, 'r') as fc:
    cliente_data = json.load(fc)

 """


data_libros()