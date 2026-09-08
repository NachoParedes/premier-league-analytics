import requests

url = "https://fantasy.premierleague.com/api/bootstrap-static/"


def obtener_datos():

    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"}

    try:
        respuesta = requests.get(url, headers=headers, timeout=10)
        respuesta.raise_for_status()

        datos = respuesta.json()
        print("Datos extraidos.")

#       print("Entidades disponibles:", list(datos.keys()))
#       entidades = ["teams", "element_types", "elements"]

#       for entidad in entidades:
#           if entidad in datos and len(datos[entidad]) > 0:
#               print(f"\n--- Atributos de '{entidad}' ---")
#               print(list(datos[entidad][0].keys()))

        return datos

    except requests.exceptions.RequestException as error:
        print(f"Error al conectar con la API: {error}")
        return None


if __name__ == "__main__":
    obtener_datos()
