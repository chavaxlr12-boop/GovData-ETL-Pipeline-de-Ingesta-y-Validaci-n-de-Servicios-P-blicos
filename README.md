# GovData-ETL: Pipeline de Procesamiento de Trámites Públicos

## 📝 Descripción
Este proyecto consiste en un **Pipeline ETL (Extract, Transform, Load)** desarrollado en Python para procesar, limpiar y estructurar datos abiertos sobre trámites y servicios gubernamentales. El objetivo principal es transformar datos crudos de archivos CSV en una base de datos relacional SQL, garantizando la integridad de la información y facilitando su análisis.

Este desarrollo fue diseñado siguiendo los requerimientos técnicos para vacantes de **Data Engineer**, enfocándose en la resiliencia del código y la calidad de los datos.

## 🚀 Características
- **Ingesta Dinámica:** Lectura de archivos CSV con manejo de codificación `latin-1` para soporte de caracteres especiales.
- **Limpieza de Esquema:** Normalización automática de nombres de columnas (eliminación de espacios y caracteres invisibles).
- **Data Transformation:** Conversión de tipos de datos (Strings a Datetime), manejo de valores nulos y estandarización de campos de texto.
- **Almacenamiento SQL:** Carga automatizada en **SQLite**, permitiendo persistencia de datos local sin dependencias de nube.
- **Análisis de Datos:** Incluye un módulo de consultas SQL para extraer métricas clave como el conteo de trámites por modalidad.

## 🛠️ Tecnologías Utilizadas
- **Lenguaje:** Python 3.x
- **Librerías de Datos:** Pandas (Data Wrangling)
- **Base de Datos:** SQLite3 (Motor relacional)
- **Entorno:** Local

## 📂 Estructura del Proyecto
```text
├── 2026_tramites_servicios.csv             # Dataset original (Fuente)
├── 2026_diccionario_tramites_servicios.csv # Diccionario de datos (Metadata)
├── main.py                                 # Script principal del Pipeline
├── gobierno.db                             # Base de datos generada (Target)
└── README.md                               # Documentación del proyecto
