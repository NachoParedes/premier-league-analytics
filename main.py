import logging
import sys

# Configuración de logs
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
    handlers=[logging.StreamHandler(sys.stdout)]
)

from src.extract import obtener_datos
from src.transform import (
    transformar_equipos,
    transformar_posiciones,
    transformar_jugadores,
)
from src.load import cargar_equipos, cargar_posiciones, cargar_jugadores


def ejecutar_pipeline():
    logging.info("==================================================")
    logging.info("  INICIANDO PIPELINE ETL: PREMIER LEAGUE ANALYTICS ")
    logging.info("==================================================")

    # 1. EXTRACCIÓN
    logging.info("[1/3] Extrayendo datos desde la API...")
    datos_raw = obtener_datos()

    if not datos_raw:
        logging.error("Fallo crítico: No se obtuvieron datos de la API. Abortando.")
        return

    # 2. TRANSFORMACIÓN
    logging.info("[2/3] Transformando datasets...")
    try:
        df_equipos = transformar_equipos(datos_raw)
        df_posiciones = transformar_posiciones(datos_raw)
        df_jugadores = transformar_jugadores(datos_raw)

        logging.info(f" -> Equipos: {len(df_equipos)}")
        logging.info(f" -> Posiciones: {len(df_posiciones)}")
        logging.info(f" -> Jugadores: {len(df_jugadores)}")

    except Exception as e:
        logging.error(f"Error en transformación: {e}")
        return

    # 3. CARGA
    logging.info("[3/3] Cargando datos en MySQL...")
    try:
        cargar_posiciones(df_posiciones)
        cargar_equipos(df_equipos)
        cargar_jugadores(df_jugadores)

        logging.info("==================================================")
        logging.info("    PIPELINE ETL EJECUTADO CON ÉXITO             ")
        logging.info("==================================================")

    except Exception as e:
        logging.error(f"Error en carga: {e}")


if __name__ == "__main__":
    ejecutar_pipeline()