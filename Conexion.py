from sqlalchemy import create_engine, text
import pandas as pd

def obtener_conexion():
    # Configuración de la cadena de conexión
    username = 'isaias'
    password = 'admin0410'
    server = 'LAPTOP-D3E5OBT7\SQLEXPRESS'
    database = 'SistemaBPM'

    # Crear la cadena de conexión usando SQLAlchemy
    connection_string = f"mssql+pyodbc://{username}:{password}@{server}/{database}?driver=ODBC+Driver+17+for+SQL+Server"
    
    # Crear el engine de SQLAlchemy para conectarse a la base de datos
    engine = create_engine(connection_string)
    return engine

def obtener_datos_por_fecha(fecha):
    # Consulta para obtener los datos filtrados por fecha específica
    query = f"""
    SELECT a.nombre, 
           COUNT(ci.cumple) AS total_incumplimientos,
           CASE 
               WHEN COUNT(ci.cumple) > 4 THEN 'rojo'
               WHEN COUNT(ci.cumple) = 3 THEN 'amarillo'
               ELSE 'verde'
           END AS semaforo
    FROM Area a
    JOIN Cumplimiento_Item ci ON a.id_area = ci.id_area
    WHERE ci.cumple = 0 AND ci.fecha_evaluacion = '{fecha}'
    GROUP BY a.nombre;
    """
    # Conectar y cargar los datos en el DataFrame
    engine = obtener_conexion()
    df = pd.read_sql(query, engine)
    engine.dispose()  # Cerrar la conexión a la base de datos
    return df

def insertar_analisis_area(nombre_area, id_item, cumple, fecha_evaluacion):
    query = text("""
    INSERT INTO Cumplimiento_Item (id_area, id_item, cumple, fecha_evaluacion)
    VALUES ((SELECT id_area FROM Area WHERE nombre = :nombre_area), :id_item, :cumple, :fecha_evaluacion);
    """)

    engine = obtener_conexion()
    with engine.begin() as conn:  # Se asegura de que la transacción se confirme al final del bloque
        conn.execute(query, {
            "nombre_area": nombre_area,
            "id_item": id_item,
            "cumple": cumple,
            "fecha_evaluacion": fecha_evaluacion
        })
    print(f"Análisis agregado para el área: {nombre_area}")

def verificar_insercion(nombre_area, fecha_evaluacion):
    query_verificacion = text("""
    SELECT * FROM Cumplimiento_Item
    WHERE id_area = (SELECT id_area FROM Area WHERE nombre = :nombre_area)
    AND fecha_evaluacion = :fecha_evaluacion
    """)
    
    engine = obtener_conexion()
    with engine.connect() as conn:
        resultado = conn.execute(query_verificacion, {
            "nombre_area": nombre_area,
            "fecha_evaluacion": fecha_evaluacion
        }).fetchall()
        
    if resultado:
        print("Datos insertados correctamente:", resultado)
    else:
        print("No se encontraron datos correspondientes.")
