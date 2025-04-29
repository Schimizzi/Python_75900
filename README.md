# Sistema de Gestión de Librería en Python

Este proyecto implementa un sistema básico para gestionar libros y clientes de una librería utilizando Python. Permite agregar, quitar y listar libros y clientes, además de cargar y guardar datos de clientes en formato JSON.

## Descripción

El sistema se compone de las siguientes clases[cite: 1]:

* **`Libro`**: Representa un libro con atributos como ID, autor, nombre y estado (vendido/disponible)[cite: 2].
* **`Cliente`**: Representa un cliente con atributos como número de socio, nombre, DNI y teléfono.
* **`Libreria`**: Clase principal que gestiona las colecciones de libros y clientes. Ofrece métodos para agregar y quitar elementos, así como para imprimirlos y guardar clientes en JSON.

El script `main.py` sirve como punto de entrada de ejemplo, mostrando cómo inicializar el sistema, cargar datos iniciales desde archivos JSON (si existen), realizar operaciones de ejemplo (agregar/quitar libros y clientes) y guardar los datos de los clientes actualizados.

## Características

* Gestión de inventario de libros (agregar, quitar, listar).
* Gestión de base de datos de clientes (agregar, quitar, listar).
* Carga de datos iniciales de libros desde `data/data_libros.json`.
* Carga y guardado persistente de datos de clientes en `data/data_clientes.json`.
* Empaquetado con `setup.py` para instalación.
* Ejemplo de uso y flujo de operaciones en `main.py`.

## Archivos de Datos

* `data/data_clientes.json`: Almacena la información de los clientes en formato JSON. Se carga al inicio y se actualiza al guardar nuevos clientes.
* `data/data_libros.json`: Contiene una lista inicial de libros en formato JSON. Se carga al iniciar el script `main.py`.

## Requisitos

* Python >= 3.7
* pip (generalmente incluido con Python)

## Instalación

Puedes instalar este proyecto como un paquete Python. Navega hasta el directorio raíz del proyecto (donde se encuentra `setup.py`) y ejecuta el siguiente comando en tu terminal:

```bash
pip install .
