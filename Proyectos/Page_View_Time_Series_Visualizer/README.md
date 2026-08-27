# Page View Time Series Visualizer 📈📅

Este proyecto demuestra el dominio de las técnicas de análisis y visualización de **Series Temporales (Time Series)** utilizando registros diarios de páginas vistas en el foro de desarrollo de freeCodeCamp desde el año 2016 hasta el 2019. El objetivo principal es identificar patrones de crecimiento, variaciones estacionales y tendencias multianuales sin distorsiones provocadas por anomalías esporádicas.

## 📋 Fases del Pipeline Analítico
1. **Indexación Temporal:** Configuración del índice del DataFrame mapeado como objetos `DatetimeIndex` nativos de Pandas.
2. **Limpieza del Ruido Estocástico:** Filtrado de datos atípicos eliminando las observaciones correspondientes a picos de tráfico inusuales o caídas del servidor. Se remueven los días que caen dentro del top 2.5% y del fondo 2.5% de la distribución total de vistas.
3. **Modelado Gráfico Estacional:**
   * **Gráfico de Línea:** Representación cronológica pura para observar la tendencia lineal general a largo plazo.
   * **Gráfico de Barras Anual-Mensual:** Agrupación cronológica secundaria para contrastar el comportamiento del tráfico promedio por mes a través de los años.
   * **Gráficos de Caja (Box Plots):** Descomposición de la serie temporal en dos diagramas adyacentes: uno enfocado en la tendencia interanual y otro en la estacionalidad mensual interna.

## 📊 Metodología Estadística de los Box Plots
Los diagramas de caja segmentan las vistas diarias para ilustrar de forma visual la dispersión y simetría de los datos mediante los componentes estadísticos:

$$\text{Mediana } (Q_2) \quad \text{;} \quad \text{Rango IQR} = Q_3 - Q_1$$

Esto permite comprobar empíricamente en qué meses del año se concentra de forma consistente el mayor volumen de visitas (por ejemplo, debido a campamentos de programación de fin de año o inicios de semestres).

## 🛠️ Tecnologías y Librerías
* **Python 3.x**
* **Pandas:** Remuestreo, filtrado basado en cuantiles (`df.quantile()`), y extracción de propiedades de fecha (`df.index.year`, `df.index.strftime('%b')`).
* **Matplotlib & Seaborn:** Creación de subplots analíticos complejos para la comparación lado a lado de tendencias.

## 📂 Estructura sugerida del Repositorio
* `time_series_visualizer.py`: Lógica de transformación temporal y diseño de los tres diagramas principales.
* `fcc-forum-pageviews.csv`: Dataset original indexado por fecha.
* `main.py`: Ejecutable para procesar los gráficos y almacenarlos de forma local en la carpeta raíz.
