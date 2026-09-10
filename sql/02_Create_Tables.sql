USE premier_league_analytics;


CREATE TABLE IF NOT EXISTS equipo (
    id_equipo INT PRIMARY KEY,
    codigo INT NOT NULL,
    nombre VARCHAR(50) NOT NULL,
    abreviatura VARCHAR(3) NOT NULL
);


CREATE TABLE IF NOT EXISTS posicion (
    id_posicion INT PRIMARY KEY,
    nombre VARCHAR(20) NOT NULL,
    abreviatura VARCHAR(3) NOT NULL
);


CREATE TABLE IF NOT EXISTS jugador (
    id_jugador INT PRIMARY KEY, 
    nombre VARCHAR(50) NOT NULL,
    apellido VARCHAR(50) NOT NULL,
    minutos_jugados INT DEFAULT 0,
    
    -- Rendimiento Ofensivo
    goles INT DEFAULT 0,
    asistencias INT DEFAULT 0,
    goles_esperados DECIMAL(5,2) DEFAULT 0.00,
    asistencias_esperadas DECIMAL(5,2) DEFAULT 0.00,
    
    -- Rendimiento Defensivo
    recuperaciones INT DEFAULT 0,
    entradas INT DEFAULT 0,
    despejes_bloqueos_intercepciones INT DEFAULT 0,

    
    -- Arquero y Disciplina
    atajadas INT DEFAULT 0,
    vallas_invictas INT DEFAULT 0,
    goles_recibidos_esperados DECIMAL(5,2) DEFAULT 0.00,
    tarjetas_rojas INT DEFAULT 0,
    tarjetas_amarillas INT DEFAULT 0,
    
    -- Claves Foráneas
    id_equipo INT NOT NULL,
    id_posicion INT NOT NULL,
    
    CONSTRAINT fk_jugador_equipo FOREIGN KEY (id_equipo) REFERENCES equipo(id_equipo) ON DELETE RESTRICT ON UPDATE CASCADE,
    CONSTRAINT fk_jugador_posicion FOREIGN KEY (id_posicion) REFERENCES posicion(id_posicion) ON DELETE RESTRICT ON UPDATE CASCADE
);