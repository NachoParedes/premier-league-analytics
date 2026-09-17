import pandas as pd


def transformar_equipos(datos_raw):
    if not datos_raw or "teams" not in datos_raw:
        return pd.DataFrame()

    df = pd.DataFrame(datos_raw["teams"])

    columnas_mapeo = {
        "id": "id_equipo",
        "code": "codigo",
        "name": "nombre",
        "short_name": "abreviatura",
    }

    df_equipos = df[list(columnas_mapeo.keys())].rename(columns=columnas_mapeo)
    return df_equipos.astype({"id_equipo": int, "codigo": int})


def transformar_jugadores(datos_raw):
    if not datos_raw or "elements" not in datos_raw:
        return pd.DataFrame()

    df = pd.DataFrame(datos_raw["elements"])

    columnas_mapeo = {
        "id": "id_jugador",
        "first_name": "nombre",
        "second_name": "apellido",
        "minutes": "minutos_jugados",
        "goals_scored": "goles",
        "assists": "asistencias",
        "expected_goals": "goles_esperados",
        "expected_assists": "asistencias_esperadas",
        "recoveries": "recuperaciones",
        "tackles": "entradas",
        "clearances_blocks_interceptions": "despejes_bloqueos_intercepciones",
        "saves": "atajadas",
        "clean_sheets": "vallas_invictas",
        "expected_goals_conceded": "goles_recibidos_esperados",
        "red_cards": "tarjetas_rojas",
        "yellow_cards": "tarjetas_amarillas",
        # Claves foráneas
        "team": "id_equipo",
        "element_type": "id_posicion",
    }

    df = df[list(columnas_mapeo.keys())].rename(columns=columnas_mapeo)

    df["nombre"] = df["nombre"].astype(str).str.strip()
    df["apellido"] = df["apellido"].astype(str).str.strip()

    df = df[
        (df["minutos_jugados"] >= 0) &
        (df["goles"] >= 0) &
        (df["asistencias"] >= 0) &
        (df["tarjetas_amarillas"] >= 0) &
        (df["tarjetas_rojas"] >= 0)
    ]

    return df.astype({"id_jugador": int})


def transformar_posiciones(datos_raw):
    if not datos_raw or "element_types" not in datos_raw:
        return pd.DataFrame()

    df = pd.DataFrame(datos_raw["element_types"])

    columnas_mapeo = {
        "id": "id_posicion",
        "singular_name": "nombre",
        "singular_name_short": "abreviatura",
    }

    return df[list(columnas_mapeo.keys())].rename(columns=columnas_mapeo)


if __name__ == "__main__":
    from extract import obtener_datos

    raw_data = obtener_datos()
    if raw_data:
        df_equipo = transformar_equipos(raw_data)
        df_jugador = transformar_jugadores(raw_data)
        df_posiciones = transformar_posiciones(raw_data)

        print("=== EQUIPOS ===")
        print(df_equipo.head())
        print("\n--------------------------------------------------------\n")
        print("=== JUGADORES ===")
        print(df_jugador.head())
        print("\n--------------------------------------------------------\n")
        print("=== POSICIONES ===")
        print(df_posiciones.head())
