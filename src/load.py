import os
import logging
from dotenv import load_dotenv
from sqlalchemy import create_engine, MetaData, Table
from sqlalchemy.dialects.mysql import insert

load_dotenv()

USER = os.getenv("DB_USER")
PASSWORD = os.getenv("DB_PASSWORD")
HOST = os.getenv("DB_HOST", "localhost")
PORT = os.getenv("DB_PORT", "3306")
DB_NAME = os.getenv("DB_NAME")

DATABASE_URL = f"mysql+pymysql://{USER}:{PASSWORD}@{HOST}:{PORT}/{DB_NAME}"
engine = create_engine(DATABASE_URL)


def _upsert_dataframe(df, table_name, pk_column):
    """
    Inserta registros nuevos o actualiza los existentes en MySQL 
    si la clave primaria ya existe (ON DUPLICATE KEY UPDATE).
    """
    if df.empty:
        return

    
    metadata = MetaData()
    table = Table(table_name, metadata, autoload_with=engine)

    records = df.to_dict(orient="records")
    stmt = insert(table).values(records)

    # Definir qué columnas actualizar cuando hay coincidencia de Primary Key (todas menos la PK)
    update_cols = {
        col.name: getattr(stmt.inserted, col.name)
        for col in table.columns
        if col.name != pk_column
    }

    
    on_duplicate_stmt = stmt.on_duplicate_key_update(**update_cols)

    
    with engine.begin() as conn:
        conn.execute(on_duplicate_stmt)


def cargar_posiciones(df_posiciones):
    if not df_posiciones.empty:
        _upsert_dataframe(df_posiciones, "posicion", pk_column="id_posicion")
        logging.info("Tabla 'posicion' procesada con UPSERT.")


def cargar_equipos(df_equipos):
    if not df_equipos.empty:
        _upsert_dataframe(df_equipos, "equipo", pk_column="id_equipo")
        logging.info("Tabla 'equipo' procesada con UPSERT.")


def cargar_jugadores(df_jugadores):
    if not df_jugadores.empty:
        _upsert_dataframe(df_jugadores, "jugador", pk_column="id_jugador")
        logging.info("Tabla 'jugador' procesada con UPSERT.")


if __name__ == "__main__":
    print("Módulo load.py con soporte UPSERT listo.")