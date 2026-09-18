import logging
import sys


logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
    handlers=[
        logging.StreamHandler(sys.stdout)
    ]
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

    # ----------------------------------------------------
    # 1. EXTRACCIÓN (Extract)
    # ----------------------------------------------------
    logging.info("Extrayendo datos desde la API...")
    datos_raw = obtener_datos()

    if not datos_raw:
        logging.error("Fallo crítico: No se obtuvieron datos de la API. Abortando pipeline.")
        return

    # ----------------------------------------------------
    # 2. TRANSFORMACIÓN (Transform)
    # ----------------------------------------------------
    logging.info("Transformando y validando datasets...")
    try:
        df_equipos = transformar_equipos(datos_raw)
        df_posiciones = transformar_posiciones(datos_raw)
        df_jugadores = transformar_jugadores(datos_raw)

        logging.info(f" -> Equipos procesados: {len(df_equipos)}")
        logging.info(f" -> Posiciones procesadas: {len(df_posiciones)}")
        logging.info(f" -> Jugadores procesados (limpios): {len(df_jugadores)}")

    except Exception as e:
        logging.error(f"Error durante la transformación de datos: {e}")
        return

    # ----------------------------------------------------
    # 3. CARGA (Load)
    # ----------------------------------------------------
    logging.info("Cargando datos en MySQL...")
    try:
       
        cargar_posiciones(df_posiciones)
        cargar_equipos(df_equipos)
        cargar_jugadores(df_jugadores)

        logging.info("==================================================")
        logging.info("    PIPELINE ETL EJECUTADO CON ÉXITO             ")
        logging.info("==================================================")

    except Exception as e:
        logging.error(f"Error durante la carga a la base de datos: {e}")


if __name__ == "__main__":
    ejecutar_pipeline()