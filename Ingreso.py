from Conexion import insertar_analisis_area, verificar_insercion

# Lista de datos a insertar
datos_a_insertar = [
    {"nombre_area": "Producción", "id_item": "A1.1", "cumple": 0, "fecha_evaluacion": "2024-10-26"},
    {"nombre_area": "Producción", "id_item": "A2.1", "cumple": 1, "fecha_evaluacion": "2024-10-26"},
    {"nombre_area": "Producción", "id_item": "A3.1", "cumple": 0, "fecha_evaluacion": "2024-10-26"},
    {"nombre_area": "Producción", "id_item": "B1.1", "cumple": 0, "fecha_evaluacion": "2024-10-26"},
    {"nombre_area": "Producción", "id_item": "B2.1", "cumple": 0, "fecha_evaluacion": "2024-10-26"},
    {"nombre_area": "Producción", "id_item": "B3.1", "cumple": 0, "fecha_evaluacion": "2024-10-26"}
]

# Insertar cada análisis de área en la base de datos
for datos in datos_a_insertar:
    insertar_analisis_area(
        datos["nombre_area"],
        datos["id_item"],
        datos["cumple"],
        datos["fecha_evaluacion"]
    )

# Verificar si la inserción fue exitosa
verificar_insercion("Producción", "2024-10-26")

