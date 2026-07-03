# Proyecto Automatidata: Análisis de Viajes en Taxi de la TLC de Nueva York

**Autor:** Yeison Moreno | Estudiante de Ciencia de Datos

## Descripción del Proyecto
Este proyecto tiene como objetivo inspeccionar, analizar y preparar los datos de la Comisión de Taxis y Limusinas de la Ciudad de Nueva York (TLC) para el desarrollo de futuros modelos predictivos. A través de una asociación con Automatidata, el análisis se centra en comprender las variables clave que influyen en los viajes, evaluar la calidad de la información y detectar anomalías o valores atípicos que requieran una fase de limpieza exhaustiva antes de la fase de modelado avanzado.

## Herramientas y Tecnologías
Para el desarrollo de este análisis y el manejo eficiente de los datos, se emplea el siguiente entorno de trabajo:
*   **Lenguaje:** Python.
*   **Análisis de Datos:** pandas y NumPy.
*   **Entorno de Desarrollo:** VS Code con la extensión de Jupyter Notebooks.

## Resumen Ejecutivo y Hallazgos Clave
El análisis exploratorio preliminar arrojó las siguientes conclusiones sobre el comportamiento y la calidad de los datos de la TLC:
*   El objetivo inicial se cumplió: se inspeccionaron los datos para entender las variables clave y asegurar que la información es adecuada para generar conocimientos claros.
*   Las variables identificadas como más útiles para construir modelos predictivos son `total_amount` (monto total) y `trip_distance` (distancia del viaje).
*   Se detectaron valores inusuales y anomalías graves en la relación distancia-costo; existen registros de viajes con distancias extremadamente cortas o nulas (0.00) que presentan cargos muy elevados (ej. $450.00 o $175.00).
*   Se sentaron las bases estructuradas para futuras visualizaciones y la creación de modelos de predicción.

## Metodología y Flujo de Trabajo (Marco PACE)
El proyecto se implementa siguiendo las fases del marco de trabajo PACE para garantizar un enfoque estructurado:
*   **Plan (Planificación):** La preparación incluyó revisar las instrucciones del proyecto, comprender el objetivo comercial, examinar el diccionario de datos, inspeccionar la estructura del conjunto de datos y organizar los archivos antes del análisis.
*   **Analyze (Análisis):** Se determinó que los datos eran suficientes para un análisis exploratorio inicial, utilizando métodos como `df.describe()` y `groupby()` para generar estadísticas, y `min()` / `max()` para evaluar los rangos.
*   **Construct (Construcción):** Esta etapa no se aplicó a este flujo de trabajo en particular, ya que el enfoque actual es estrictamente exploratorio.
*   **Execute (Ejecución):** Se recomendó realizar un proceso detallado de validación de datos previo al análisis profundo para investigar las anomalías detectadas.

## Preguntas y Respuestas del Análisis
Durante el desarrollo de esta fase, se plantearon y resolvieron las siguientes interrogantes clave:
*   **¿Cómo puedes prepararte mejor para entender y organizar la información proporcionada?** Revisando las instrucciones, comprendiendo el objetivo comercial, examinando el diccionario de datos y la estructura del conjunto antes de programar.
*   **¿Qué libros de códigos y herramientas de seguimiento te ayudarán a realizar este trabajo?** La documentación oficial de pandas, NumPy, Python y Jupyter Notebook, además de los materiales de referencia del marco de trabajo.
*   **¿La información disponible será suficiente para lograr el objetivo?** Sí, el conjunto de datos es suficiente para un análisis exploratorio gracias a variables como `total_amount`, `tip_amount`, `payment_type` y `vendor_id`. Sin embargo, existen problemas de calidad que deben resolverse.
*   **¿Cómo construirías las estadísticas de resumen del marco de datos y evaluarías el rango mínimo y máximo?** Usando métodos como `df.describe()` para variables numéricas, `groupby()` para desgloses categóricos, y las funciones `min()` y `max()`.
*   **¿Los promedios de alguna variable parecen inusuales o presentan anomalías?** Sí. El promedio de `tip_amount` para pagos en efectivo es 0.0. La variable `total_amount` contiene valores negativos inexplicables y presenta valores atípicos extremos con máximos que alcanzan aproximadamente los $1200.
*   **¿Qué recomendarías investigar más a fondo antes de realizar el análisis exploratorio?** Investigar la presencia de los valores negativos (para saber si son errores o reembolsos), revisar los valores atípicos extremos para confirmar si son reales, y verificar por qué las propinas en efectivo siempre marcan 0.0.
*   **¿Qué tipos adicionales de datos podrían fortalecer este conjunto?** Marcas de tiempo de recogida y entrega, datos de ubicación geográfica (zonas), identificadores de conductores, y factores externos como el clima o el tráfico.

## Próximos Pasos
Con el fin de avanzar hacia la fase de modelado predictivo, se establecen las siguientes acciones:
*   Realizar un Análisis Exploratorio de Datos (EDA) completo.
*   Ejecutar pasos de limpieza para comprender y tratar las variables inusuales y los valores atípicos.
*   Utilizar estadísticas descriptivas avanzadas.
*   Crear un modelo de regresión basado en las variables depuradas para predecir costos o comportamientos de los viajes.