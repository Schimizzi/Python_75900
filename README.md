# Sistema de Gestión de Librería en Python

Este proyecto implementa un sistema básico para gestionar libros y clientes de una librería utilizando Python. Permite agregar, quitar y listar libros y clientes, además de cargar y guardar datos de clientes en formato JSON.

## Descripción

El sistema se compone de las siguientes clases:

* **`Libro`**: Representa un libro con atributos como ID, autor, nombre y estado (vendido/disponible).
* **`Cliente`**: Representa un cliente con atributos como número de socio, nombre, DNI y teléfono.
* **`Libreria`**: Clase principal que gestiona las colecciones de libros y clientes. Ofrece métodos para agregar y quitar elementos, así como para imprimirlos.

El script `main.py` inicializa el sistema, carga datos iniciales desde archivos JSON (si existen), realiza algunas operaciones de ejemplo (agregar/quitar libros y clientes) y guarda los datos de los clientes actualizados.

## Características

* Gestión de inventario de libros (agregar, quitar, listar).
* Gestión de base de datos de clientes (agregar, quitar, listar).
* Carga de datos iniciales de libros desde `data/data_libros.json`.
* Carga y guardado persistente de datos de clientes en `data/data_clientes.json`.
* Ejemplo de uso y flujo de operaciones en `main.py`.

## Archivos de Datos

* `data/data_clientes.json`: Almacena la información de los clientes en formato JSON. Se carga al inicio y se actualiza al guardar nuevos clientes.
* `data/data_libros.json`: Contiene una lista inicial de libros en formato JSON. Se carga al iniciar el script `main.py`.

## Uso

1.  **Asegúrate de tener Python instalado.**
2.  **Coloca los archivos** `cliente.py`, `libro.py`, `libreria.py` y `main.py` en el mismo directorio.
3.  **Crea un directorio `data`** en la misma ubicación.
4.  **(Opcional)** Coloca los archivos `data_clientes.json` y `data_libros.json` dentro del directorio `data` si deseas cargar datos iniciales. Si no existen, el programa comenzará con listas vacías o manejará el error de archivo no encontrado.
5.  **Ejecuta el script principal:**
    ```bash
    python main.py
    ```
6.  El script realizará las operaciones definidas en `main.py` e imprimirá los resultados en la consola, mostrando el estado final de los libros y clientes en la librería, y guardando la información de los clientes relevantes en `data_clientes.json`.

## Dependencias

* Python 3.x
* Módulos estándar de Python: `json`, `os`. No se requieren bibliotecas externas.
