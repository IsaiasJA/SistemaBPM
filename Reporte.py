import pandas as pd
from reportlab.lib.pagesizes import A4
from reportlab.lib import colors
from reportlab.lib.units import inch
from reportlab.pdfgen import canvas
from Conexion import obtener_datos_por_fecha

def generar_reporte_pdf(dataframe, nombre_archivo, fecha):
    c = canvas.Canvas(nombre_archivo, pagesize=A4)
    c.setTitle(f"Reporte de Cumplimiento de Buenas Prácticas - {fecha}")

    # Encabezado
    c.setFont("Helvetica-Bold", 14)
    c.drawString(1 * inch, 10.5 * inch, f"Reporte de Cumplimiento por Área - Fecha: {fecha}")

    # Columnas
    c.setFont("Helvetica-Bold", 12)
    c.drawString(1 * inch, 10 * inch, "Área")
    c.drawString(3 * inch, 10 * inch, "Total de Incumplimientos")
    c.drawString(5.5 * inch, 10 * inch, "Semáforo")  # Ajusta la posición para más espacio

    # Datos de cada área
    c.setFont("Helvetica", 10)
    y = 9.5 * inch  # Posición Y inicial

    for _, row in dataframe.iterrows():
        # Columna: Nombre del Área
        c.drawString(1 * inch, y, row["nombre"])

        # Columna: Total de Incumplimientos
        c.drawString(3 * inch, y, str(row["total_incumplimientos"]))

        # Columna: Semáforo
        color = colors.red if row["semaforo"] == "rojo" else colors.yellow if row["semaforo"] == "amarillo" else colors.green
        c.setFillColor(color)
        c.drawString(5.5 * inch, y, row["semaforo"].capitalize())
        c.setFillColor(colors.black)  # Restablecer el color a negro para el texto siguiente

        y -= 0.3 * inch  # Reducir la posición Y para la siguiente fila

    c.save()
    print(f"Reporte generado: {nombre_archivo}")

# Definir la fecha deseada
fecha_reporte = "2024-10-01"

# Obtener los datos filtrados por la fecha
df = obtener_datos_por_fecha(fecha_reporte)

# Generar el nombre del archivo PDF basado en la fecha
nombre_archivo_pdf = f"Reporte_Cumplimiento_Areas_{fecha_reporte}.pdf"

# Generar el reporte PDF con la fecha
generar_reporte_pdf(df, nombre_archivo_pdf, fecha_reporte)
