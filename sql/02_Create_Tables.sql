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
goles_esperados DECIMAL(5, 2) DEFAULT 0.00,
asistencias_esperadas DECIMAL(5, 2) DEFAULT 0.00,

-- Rendimiento Defensivo
recuperaciones INT DEFAULT 0,
entradas INT DEFAULT 0,
despejes_bloqueos_intercepciones INT DEFAULT 0,

-- Arquero y Disciplina
atajadas INT DEFAULT 0,
vallas_invictas INT DEFAULT 0,
goles_recibidos_esperados DECIMAL(5, 2) DEFAULT 0.00,
tarjetas_rojas INT DEFAULT 0,
tarjetas_amarillas INT DEFAULT 0,

-- Claves Foráneas

id_equipo INT NOT NULL,
id_posicion INT NOT NULL,
CONSTRAINT fk_jugador_equipo FOREIGN KEY (id_equipo) REFERENCES equipo (id_equipo) ON DELETE RESTRICT ON UPDATE CASCADE,
CONSTRAINT fk_jugador_posicion FOREIGN KEY (id_posicion) REFERENCES posicion (id_posicion) ON DELETE RESTRICT ON UPDATE CASCADE,


CONSTRAINT chk_metricas_positivas CHECK (
    minutos_jugados >= 0
    AND goles >= 0
    AND asistencias >= 0
    AND tarjetas_amarillas >= 0
    AND tarjetas_rojas >= 0)


);

CREATE TABLE IF NOT EXISTS jugador_auditoria (
    id_auditoria INT AUTO_INCREMENT PRIMARY KEY,
    id_jugador INT NOT NULL,
    id_equipo INT,
    id_posicion INT,
    minutos_jugados INT,
    goles INT,
    asistencias INT,
    goles_esperados DECIMAL(5, 2),
    asistencias_esperadas DECIMAL(5, 2),
    recuperaciones INT,
    entradas INT,
    despejes_bloqueos_intercepciones INT,
    vallas_invictas INT,
    goles_recibidos_esperados DECIMAL(5, 2),
    atajadas INT,
    tarjetas_rojas INT,
    tarjetas_amarillas INT,
    tipo_operacion VARCHAR(10) NOT NULL, -- 'UPDATE' o 'DELETE'
    fecha_registro DATETIME DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (id_jugador) REFERENCES jugador (id_jugador) ON DELETE CASCADE
);