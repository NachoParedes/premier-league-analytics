USE premier_league_analytics;

-- =====================================================
-- Trigger 1: Auditoría de Jugadores (BEFORE UPDATE)
-- =====================================================
DELIMITER $$

CREATE TRIGGER trg_auditoria
BEFORE UPDATE ON jugador
FOR EACH ROW
BEGIN
    
    INSERT INTO jugador_auditoria (
        id_jugador,
        id_equipo,
        id_posicion,
        minutos_jugados,
        goles,
        asistencias,
        goles_esperados,
        asistencias_esperadas,
        recuperaciones,
        entradas,
        despejes_bloqueos_intercepciones,
        vallas_invictas,
        goles_recibidos_esperados,
        atajadas,
        tarjetas_rojas,
        tarjetas_amarillas,
        tipo_operacion,
        fecha_registro
    )
    VALUES (
        OLD.id_jugador,
        OLD.id_equipo,
        OLD.id_posicion,
        OLD.minutos_jugados,
        OLD.goles,
        OLD.asistencias,
        OLD.goles_esperados,
        OLD.asistencias_esperadas,
        OLD.recuperaciones,
        OLD.entradas,
        OLD.despejes_bloqueos_intercepciones,
        OLD.vallas_invictas,
        OLD.goles_recibidos_esperados,
        OLD.atajadas,
        OLD.tarjetas_rojas,
        OLD.tarjetas_amarillas,
        'UPDATE', 
        NOW()
    );
END$$

DELIMITER ;


-- =====================================================
-- Trigger 2: Auditoría de Bajas de Jugadores (BEFORE DELETE)
-- =====================================================
DELIMITER $$
CREATE TRIGGER trg_jugador_before_delete
BEFORE DELETE ON jugador
FOR EACH ROW
BEGIN
    INSERT INTO jugador_auditoria (
        id_jugador, 
        id_equipo, 
        id_posicion, 
        minutos_jugados, 
        goles,
        asistencias, 
        goles_esperados, 
        asistencias_esperadas, 
        recuperaciones,
        entradas, 
        despejes_bloqueos_intercepciones, 
        vallas_invictas,
        goles_recibidos_esperados, 
        atajadas, 
        tarjetas_rojas, 
        tarjetas_amarillas,
        tipo_operacion, 
        fecha_registro
    )
    VALUES (
        OLD.id_jugador, 
        OLD.id_equipo, 
        OLD.id_posicion, 
        OLD.minutos_jugados, 
        OLD.goles,
        OLD.asistencias, 
        OLD.goles_esperados, 
        OLD.asistencias_esperadas, 
        OLD.recuperaciones,
        OLD.entradas, 
        OLD.despejes_bloqueos_intercepciones, 
        OLD.vallas_invictas,
        OLD.goles_recibidos_esperados, 
        OLD.atajadas, 
        OLD.tarjetas_rojas, 
        OLD.tarjetas_amarillas,
        'DELETE', 
        NOW()
    );
END$$

DELIMITER ;


-- =====================================================
-- Trigger 3: Auditoría de Nuevos Jugadores (AFTER INSERT)
-- =====================================================
DELIMITER $$

CREATE TRIGGER trg_jugador_after_insert
AFTER INSERT ON jugador
FOR EACH ROW
BEGIN
    INSERT INTO jugador_auditoria (
        id_jugador, 
        id_equipo, 
        id_posicion, 
        minutos_jugados, 
        goles,
        asistencias, 
        goles_esperados, 
        sistencias_esperadas, 
        recuperaciones,
        entradas, 
        despejes_bloqueos_intercepciones, 
        vallas_invictas,
        goles_recibidos_esperados, 
        atajadas, tarjetas_rojas, 
        tarjetas_amarillas,
        tipo_operacion, 
        fecha_registro
    )
    VALUES (
        NEW.id_jugador, 
        NEW.id_equipo, 
        NEW.id_posicion, 
        NEW.minutos_jugados, 
        NEW.goles,
        NEW.asistencias, 
        NEW.goles_esperados, 
        NEW.asistencias_esperadas, 
        NEW.recuperaciones,
        NEW.entradas, 
        NEW.despejes_bloqueos_intercepciones, 
        NEW.vallas_invictas,
        NEW.goles_recibidos_esperados, 
        NEW.atajadas, 
        NEW.tarjetas_rojas, 
        NEW.tarjetas_amarillas,
        'INSERT', 
        NOW()
    );
END$$

DELIMITER ;


-- =====================================================
-- Trigger 4: Control de Abreviaturas de Equipos
-- =====================================================
DELIMITER $$

CREATE TRIGGER trg_equipo_before_insert
BEFORE INSERT ON equipo
FOR EACH ROW
BEGIN
    SET NEW.abreviatura = UPPER(TRIM(NEW.abreviatura));
END$$

DELIMITER ;