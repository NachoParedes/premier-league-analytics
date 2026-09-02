import requests

url = "https://fantasy.premierleague.com/api/bootstrap-static/"
data = requests.get(url).json()

# 1. Inspeccionar las claves de un Equipo
equipo_muestra = data['teams'][0]
print("--- CAMPOS DISPONIBLES EN EQUIPOS ---")
print(list(equipo_muestra.keys()))

# 2. Inspeccionar datos de un Jugador de muestra
jugador_muestra = data['elements'][0]
print("\n--- EJEMPLO DE UN JUGADOR ---")
print(f"Nombre: {jugador_muestra['first_name']} {jugador_muestra['second_name']}")
print(f"Equipo (ID): {jugador_muestra['team']}")
print(f"Posición (ID): {jugador_muestra['element_type']}")
print(f"Puntos Totales: {jugador_muestra['total_points']}")
print(f"Goles: {jugador_muestra['goals_scored']}")
print(f"Asistencias: {jugador_muestra['assists']}")