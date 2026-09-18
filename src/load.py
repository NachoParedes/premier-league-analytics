import os
import logging
from dotenv import load_dotenv
from sqlalchemy import create_engine

# Carga de variables de entorno y conexión
load_dotenv()

USER = os.getenv("DB_USER")
PASSWORD = os.getenv("DB_PASSWORD")
HOST = os.getenv("DB_HOST", "localhost")
PORT = os.getenv("DB_PORT", "3306")
DB_NAME = os.getenv("DB_NAME")

DATABASE_URL = f"mysql+pymysql://{USER}:{PASSWORD}@{HOST}:{PORT}/{DB_NAME}"
engine = create_engine(DATABASE_URL)


def cargar_posiciones(df_posiciones):
    if not df_posiciones.empty:
        df_posiciones.to_sql(name="posicion", con=engine, if_exists="append", index=False)
        logging.info("Tabla 'posicion' actualizada en MySQL.")


def cargar_equipos(df_equipos):
    if not df_equipos.empty:
        df_equipos.to_sql(name="equipo", con=engine, if_exists="append", index=False)
        logging.info("Tabla 'equipo' actualizada en MySQL.")


def cargar_jugadores(df_jugadores):
    if not df_jugadores.empty:
        df_jugadores.to_sql(name="jugador", con=engine, if_exists="append", index=False)
        logging.info("Tabla 'jugador' actualizada en MySQL.")


if __name__ == "__main__":
    # Prueba aislada opcional
    print("Módulo load.py listo para ser llamado desde main.py")