
import pandas as pd
import sqlite3
import os

# Configuración de rutas y nombres
file_data = "2026_tramites_servicios.csv"
file_dict = "2026_diccionario_tramites_servicios.csv"
db_name = "gobierno.db"

# Función de Extracción y Transformación 
def procesar_datos_robusto(file_path):
    df = pd.read_csv(file_path, encoding='latin-1', low_memory=False)
    
    # Limpieza de nombres de columnas
    df.columns = df.columns.str.strip()
    
    # Conversión de fechas de texto a formato fecha real
    columnas_fechas = ['fecha_inicio', 'fecha_termino', 'fecha_actualizacion']
    for col in columnas_fechas:
        if col in df.columns:
            df[col] = pd.to_datetime(df[col], dayfirst=True, errors='coerce')
    
    # Manejo de nulos
    if 'tipo_tramite_servicio' in df.columns:
        df['tipo_tramite_servicio'] = df['tipo_tramite_servicio'].fillna('No especificado')
    
    return df

def cargar_sql(df_para_cargar):

    conn = sqlite3.connect(db_name)
    df_para_cargar.to_sql("tramites", conn, if_exists="replace", index=False)
    print(f"Éxito: Datos cargados en la tabla 'tramites' de {db_name}")
    conn.close()

def consultar_metricas():

    conn = sqlite3.connect(db_name)
    
    query = """
    SELECT modalidad_tramite, COUNT(*) AS total
    FROM tramites
    GROUP BY modalidad_tramite
    ORDER BY total DESC
    """
    
    resultados = pd.read_sql(query, conn)
    print("\n--- Métricas por Modalidad ---")
    print(resultados)
    
    conn.close()

if __name__ == "__main__":
    try:
        # Paso 1: Procesar
        df_limpio = procesar_datos_robusto(file_data)
        print("1. Transformación completada.")
        
        # Paso 2: Cargar
        cargar_sql(df_limpio)
        print("2. Carga a SQL completada.")
        
        # Paso 3: Consultar
        consultar_metricas()
        print("3. Consulta ejecutada con éxito.")
        
    except Exception as e:
        print(f"Hubo un error en el pipeline: {e}")
