import requests
import logging

URL_API = "https://fantasy.premierleague.com/api/bootstrap-static/"

def obtener_datos():
    """Realiza la petición HTTP a la API de la Premier League y retorna el JSON."""
    try:
        response = requests.get(URL_API, timeout=10)
        response.raise_for_status()
        logging.info("Extracción exitosa desde la API.")
        return response.json()
    except requests.exceptions.RequestException as e:
        logging.error(f"Error al conectar con la API: {e}")
        return None

if __name__ == "__main__":
    datos = obtener_datos()
    if datos:
        print(f"Claves recibidas en el JSON: {list(datos.keys())}")
