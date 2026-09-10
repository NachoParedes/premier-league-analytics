import os
from dotenv import load_dotenv
from sqlalchemy import create_engine
from extract import obtener_datos
from transform import (
    transformar_equipos,
    transformar_jugadores,
    transformar_posiciones
)

load_dotenv()

USER = os.getenv("DB_USER")
PASSWORD = os.getenv("DB_PASSWORD")
HOST = os.getenv("DB_HOST", "localhost")
PORT = os.getenv("DB_PORT", "3306")
DB_NAME = os.getenv("DB_NAME")

DATABASE_URL = f"mysql+pymysql://{USER}:{PASSWORD}@{HOST}:{PORT}/{DB_NAME}"
engine = create_engine(DATABASE_URL)

raw_data = obtener_datos()

df_posiciones = transformar_posiciones(raw_data)
df_equipo = transformar_equipos(raw_data)
df_jugador = transformar_jugadores(raw_data)


df_posiciones.to_sql(name="posicion", con=engine, if_exists="append", index=False)
df_equipo.to_sql(name="equipo", con=engine, if_exists="append", index=False)
df_jugador.to_sql(name="jugador", con=engine, if_exists="append", index=False)

print("¡Carga completada con éxito!")




