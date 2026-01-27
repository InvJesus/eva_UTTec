# Análisis de Contenido del Repositorio eva_UTTec

Este documento presenta un análisis detallado del contenido y estructura del repositorio `eva_UTTec`.

## Visión General del Proyecto

El repositorio aloja un sistema de **Evaluación Digital** basado en tecnologías web (HTML, CSS con Tailwind, JavaScript). El sistema está diseñado para realizar exámenes en línea con tres tipos de actividades y generar resultados verificables mediante códigos QR.

## Arquitectura del Sistema

El sistema utiliza un diseño desacoplado donde la lógica de la interfaz (Frontend) está separada de los datos de la evaluación (Configuración).

*   **Frontend (HTML/JS):** Archivos `.html` que contienen la estructura de la página, estilos y lógica en JavaScript. Se encargan de:
    *   Autenticación del usuario (Clave predeterminada: `Admin123.@`).
    *   Renderizado de las secciones de preguntas.
    *   Lógica de los juegos (Ahorcado) y validaciones.
    *   Cálculo de puntajes y generación de QR.
*   **Datos (JSON):** Archivos `.json` alojados externamente (o localmente) que definen:
    *   Metadatos generales (Título, Subtítulo, Profesor).
    *   Preguntas de opción múltiple (Sección 1).
    *   Pares de conceptos para relacionar (Sección 2).
    *   Palabras y pistas para el juego del ahorcado (Sección 3).

El Frontend carga dinámicamente el JSON configurado en la variable `JSON_CONFIG_URL` al iniciar o autenticarse.

## Inventario de Contenido

Se han identificado las siguientes evaluaciones disponibles en el repositorio:

### 1. Administración de Bases de Datos
*   **Archivo HTML:** `UTTec_1ro_AdmDB.html`
*   **Configuración JSON:** `UTTec_1ro_AdmDB.json`
*   **Temas:** Planificación de escalabilidad, seguridad, copias de seguridad (completa, diferencial, espejo), monitoreo y cumplimiento normativo.
*   **Estructura:**
    *   Sección 1: 15 preguntas.
    *   Sección 2: 13 pares de conceptos.
    *   Sección 3: 12 palabras (Ahorcado).

### 2. Cómputo en la Nube (Cloud Computing)
*   **Archivo HTML:** `UTTec_1ro_Computo_Nube.html`
*   **Configuración JSON:** `cCNUbe.json`
*   **Temas:** Modelos de servicio (IaaS, PaaS, SaaS), modelos de implementación (Pública, Privada, Híbrida), escalabilidad, interoperabilidad y casos de uso.
*   **Estructura:**
    *   Sección 1: 15 preguntas.
    *   Sección 2: 8 pares de conceptos.
    *   Sección 3: 10 palabras (Ahorcado).

### 3. Extracción de Conocimiento en Bases de Datos (Big Data / Data Warehousing)
*   **Archivo HTML:** `UTTec_1ro_ECBD.html` y `UTTec_1ro_ECBD9IDS1.html`
*   **Configuración JSON:** `cECDB.json` y `cECDB9IDS1.json`
*   **Temas:** Data Warehouse, ETL vs ELT, Big Data (Vs), Machine Learning, Minería de Datos, Esquemas (Estrella, Copo de Nieve, Constelación).
*   **Variantes:** `cECDB9IDS1.json` parece ser una versión específica para el grupo "9IDS1", con contenido muy similar a `cECDB.json`.
*   **Estructura:**
    *   Sección 1: 15 preguntas.
    *   Sección 2: 8 pares de conceptos.
    *   Sección 3: 10 palabras (Ahorcado).

### 4. Tecnologías para Manejo Masivo de Datos
*   **Archivo HTML:** `UTTec_1ro_MMD.html`
*   **Configuración JSON:** `UTTec_MMD1ro.json`
*   **Temas:** Estrategia de datos, Big Data, Data Warehouse (Inmon vs Kimball), IoT, Data Lakes, Procesamiento Distribuido.
*   **Estructura:**
    *   Sección 1: 15 preguntas.
    *   Sección 2: 10 pares de conceptos.
    *   Sección 3: 10 palabras (Ahorcado).

### 5. Archivo Base
*   **Archivo HTML:** `cuestbase.html`
*   **Configuración JSON:** Apunta a `cECDB9IDS1.json`.
*   **Descripción:** Parece ser una plantilla base o una copia de desarrollo. Contiene un título hardcodeado en HTML ("TECNOLOGÍAS PARA MANEJO MASIVO DE DATOS") que no coincide con el JSON configurado ("EXTRACCIÓN DE CONOCIMIENTO..."), aunque el script actualiza el título dinámicamente.

## Observaciones Técnicas

1.  **Dependencias Externas:**
    *   TailwindCSS (CDN) para estilos.
    *   QRious (CDN) para generación de códigos QR.
    *   Los archivos JSON se cargan desde `https://invjesus.github.io/eva_UTTec/`, lo que implica que el repositorio funciona como un GitHub Pages o similar.

2.  **Seguridad:**
    *   Implementa bloqueos básicos de interfaz (deshabilitar clic derecho, F12) mediante JavaScript.
    *   Autenticación simple en cliente (clave hardcodeada en JS).

3.  **Inconsistencias Menores:**
    *   Los valores de ponderación (%) mostrados en el HTML inicial (antes de cargar el JSON) a veces difieren de los valores reales en el JSON. Sin embargo, el script actualiza estos valores en la interfaz una vez cargada la configuración, por lo que el usuario final ve la información correcta tras autenticarse.
