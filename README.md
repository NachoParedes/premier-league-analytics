# ⚽ Premier League Analytics - Data Pipeline & BI Dashboard

## 📖 Descripción

Este proyecto consiste en el desarrollo de una solución *end-to-end* de análisis de datos para la **Premier League**, abarcando desde la extracción y transformación de estadísticas de jugadores hasta su modelado en una base de datos relacional y su posterior visualización en un dashboard interactivo de Power BI.

El objetivo principal es automatizar el procesamiento de datos deportivos crudos para transformarlos en métricas de rendimiento comparables y claras, facilitando el análisis visual sobre métricas de goles, asistencias, efectividad y rendimiento por posición.

---

# 🎯 Objetivo

Construir un pipeline de datos (ETL) eficiente en **Python** que extraiga, limpie y cargue información cuantitativa de jugadores de la Premier League en **MySQL**, permitiendo la ingesta estructurada de datos y la generación de tableros analíticos en **Power BI** para evaluar el desempeño individual y colectivo de los equipos.

---

# 📊 Caso de uso y Preguntas analíticas

El análisis de datos aplicados al fútbol requiere convertir métricas dispersas en indicadores clave de rendimiento (KPIs). Este proyecto busca responder interrogantes analíticos como:

* ¿Quiénes son los jugadores con mayor participación directa en goles (Goles + Asistencias) por cada 90 minutos jugados?
* ¿Qué equipos generan mayor volumen ofensivo en comparación con su efectividad real?
* ¿Cómo se distribuyen las métricas de rendimiento según las distintas posiciones en el campo (delanteros, mediocampistas, defensas)?
* ¿Existe correlación entre la disciplina (tarjetas) y la efectividad defensiva/ofensiva de un jugador?

---

# 🔄 Arquitectura del Pipeline (ETL)

El proyecto sigue un flujo de datos modular divido en tres etapas principales:

```text
[ Extracción (Python) ] ──> [ Limpieza & Transformación (Pandas) ] ──> [ Carga (MySQL) ] ──> [ Visualización (Power BI) ]