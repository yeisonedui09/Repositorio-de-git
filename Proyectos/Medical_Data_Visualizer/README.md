# Medical Data Visualizer 🏥📊

Este proyecto se enfoca en el análisis exploratorio de datos (EDA) y la visualización de un conjunto de datos médicos recopilados de exámenes de pacientes. Se analizan las relaciones entre enfermedades cardiovasculares, variables fisiológicas (presión arterial, colesterol) y hábitos de vida (tabaquismo, alcohol, actividad física).

## 📋 Etapas del Análisis y Limpieza
1. **Ingeniería de Características:** Creación de la variable `overweight` (sobrepeso) calculando el Índice de Masa Corporal (IMC) y determinando si el valor supera el umbral clínico de 25.
2. **Normalización de Indicadores:** Transformación de las variables de colesterol y glucosa, asignando `0` para niveles normales y `1` si están por encima de lo normal.
3. **Data Cleaning Estricto (Remoción de Outliers):** Filtrado de registros erróneos basados en criterios de consistencia biológica:
   * Presión diastólica mayor que la sistólica.
   * Altura o peso por debajo del percentil 2.5% o por encima del percentil 97.5%.
4. **Visualización Gráfica Avanzada:** Construcción de gráficos categóricos y una matriz de correlación triangular regularizada.

## 📊 Fórmulas Aplicadas
El **Índice de Masa Corporal (IMC)** se define como el peso en kilogramos dividido por el cuadrado de la altura en metros:

$$\text{IMC} = \frac{\text{peso (kg)}}{\text{altura (m)}^2}$$

Para evaluar la fuerza y dirección de las dependencias lineales entre los signos vitales tras la limpieza de datos, se genera una matriz utilizando el **Coeficiente de Correlación de Pearson ($r$)**:

$$r = \frac{\sum (x_i - \bar{x})(y_i - \bar{y})}{\sqrt{\sum (x_i - \bar{x})^2 \sum (y_i - \bar{y})^2}}$$

## 🛠️ Tecnologías y Librerías
* **Python 3.x**
* **Pandas:** Limpieza multivariable y formateo de datos de formato ancho (*wide*) a formato largo (*long*) usando `pd.melt()`.
* **Matplotlib y Seaborn:** Uso de `sns.catplot()` para gráficos de barras de variables categóricas segregadas por estado de enfermedad, y `sns.heatmap()` combinado con máscaras matriciales booleanas (`np.triu()`) para ocultar la sección superior redundante del mapa de calor.

## 📂 Estructura sugerida del Repositorio
* `medical_data_visualizer.py`: Funciones para generar el gráfico categórico y el mapa de calor.
* `medical_examination.csv`: Dataset con las métricas clínicas de los pacientes.
* `main.py`: Orquestador para ejecutar la generación y guardado automático de las imágenes en alta resolución (`.png`).
