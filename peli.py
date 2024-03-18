import requests

def buscar_pelicula_por_titulo(titulo):
    api_key = " 39fd138f"
    url = f"http://www.omdbapi.com/?apikey={api_key}&t={titulo}"
    respuesta = requests.get(url)
    datos = respuesta.json()
    return datos

def mostrar_detalles_pelicula(datos):
    if datos['Response'] == 'True':
        print("Título:", datos['Title'])
        print("Año:", datos['Year'])
        print("Clasificación:", datos['Rated'])
        print("Género:", datos['Genre'])
        print("Reparto:", datos['Actors'])
        print("Trama:", datos['Plot'])
    else:
        print("Película no encontrada")

# Ejemplo de uso
titulo_pelicula = input("Introduce el título de la película: ")
datos_pelicula = buscar_pelicula_por_titulo(titulo_pelicula)
mostrar_detalles_pelicula(datos_pelicula)