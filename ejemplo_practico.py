import asyncio  # Importa la biblioteca asyncio para programación asíncrona
import aiohttp   # Importa la biblioteca aiohttp para realizar solicitudes HTTP asíncronas
import time      # Importa la biblioteca time para medir el tiempo de ejecución

# ---------------------------- CLASE LIBRO ----------------------------

class Libro:
    """
    Clase que representa un libro.
    """

    def __init__(self, titulo, autor, año):
        self.titulo = titulo
        self.autor = autor
        self.año = año

    def descripcion(self):
        """
        Método que devuelve una descripción del libro.
        """
        return f"{self.titulo} por {self.autor} ({self.año})"


# ---------------------------- DESCARGA ASÍNCRONA DE DATOS ----------------------------

async def descargar_datos(url):
    """
    Función asíncrona para descargar datos desde una URL.
    """
    print(f"Descargando datos de {url}...")
    async with aiohttp.ClientSession() as sesion:
        async with sesion.get(url) as respuesta:
            datos = await respuesta.text()  # Espera a que se complete la descarga
            print(f"Datos descargados de {url} con tamaño {len(datos)} bytes.")
            return datos


async def obtener_informacion_libros(urls):
    """
    Función asíncrona que descarga información de libros desde varias URLs.
    """
    tareas = [descargar_datos(url) for url in urls]  # Crear tareas asíncronas
    resultados = await asyncio.gather(*tareas)  # Ejecutar las tareas de manera concurrente
    return resultados


# ---------------------------- MENÚ INTERACTIVO ----------------------------

async def main():
    """
    Función principal que ejecuta el menú interactivo.
    """
    # Lista de URLs simuladas para descargar información de libros
    urls = [
        'https://api.example.com/libro1',
        'https://api.example.com/libro2',
        'https://api.example.com/libro3',
    ]

    while True:
        print("\n--- SISTEMA DE GESTIÓN DE LIBROS ---")
        print("1. Descargar información de libros")
        print("2. Salir")

        opcion = input("Seleccione una opción: ").strip()

        if opcion == "1":
            # Llamar a la función asíncrona para obtener información de libros
            resultados = await obtener_informacion_libros(urls)
            for i, datos in enumerate(resultados):
                print(f"Información del libro {i + 1}: {datos[:100]}...")  # Imprimir los primeros 100 caracteres
        elif opcion == "2":
            print("Saliendo del programa...")
            break  # Termina el bucle y finaliza el programa
        else:
            print("Opción no válida. Intente de nuevo.")


# Ejecutar el bucle de eventos
if __name__ == "__main__":
    start_time = time.time()  # Guardar el tiempo de inicio
    asyncio.run(main())  # Ejecutar la función principal en el bucle de eventos
    print(f"Tiempo total: {time.time() - start_time:.2f} segundos")  # Imprimir el tiempo total de ejecución
