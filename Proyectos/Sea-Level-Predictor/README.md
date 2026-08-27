# Sea Level Predictor 🌊📉

Este proyecto implementa un modelo de análisis de datos y regresión estadística para analizar el cambio en el nivel medio global del mar desde 1880 y generar una predicción matemática de su evolución hasta el año 2050.

## 📋 Objetivos del Proyecto
1. **Análisis Exploratorio (EDA):** Investigar la relación histórica entre el tiempo (años) y el ajuste del nivel del mar.
2. **Modelado Estadístico:** Utilizar regresión lineal simple para calcular la línea de mejor ajuste basada en los datos históricos completos.
3. **Predicción de Tendencias:** Generar una segunda línea de regresión utilizando únicamente datos del siglo XXI (año 2000 en adelante) para evaluar si el ritmo de aumento del nivel del mar se está acelerando, proyectando ambos escenarios hasta el año 2050.

## 📊 Marco Teórico y Fórmulas
Para modelar la tendencia del nivel del mar, se aplica el método de **Mínimos Cuadrados Ordinarios (OLS)** para una Regresión Lineal Simple, cuya ecuación fundamental es:

$$y = \beta_0 + \beta_1 x + \epsilon$$

Donde:
* $y$: Nivel del mar estimado (CSIRO Adjusted Sea Level).
* $x$: Tiempo (Año).
* $\beta_0$: Intercepto con el eje Y.
* $\beta_1$: Pendiente de la recta (ritmo de cambio anual).
* $\epsilon$: Término de error residual.

El cálculo de la pendiente ($\beta_1$) y el intercepto ($\beta_0$) se realiza mediante las siguientes expresiones estadísticas basadas en la covarianza y la varianza de los datos:

$$\beta_1 = \frac{\sum (x_i - \bar{x})(y_i - \bar{y})}{\sum (x_i - \bar{x})^2} \quad \text{;} \quad \beta_0 = \bar{y} - \beta_1\bar{x}$$

## 🛠️ Tecnologías y Librerías Utilizadas
* **Python 3.x**
* **Pandas:** Para la manipulación, limpieza y estructuración de las series temporales.
* **Matplotlib:** Para la generación de gráficos de dispersión de alta fidelidad y superposición de rectas de regresión.
* **SciPy (stats):** Específicamente la función `linregress` para extraer métricas estadísticas cruciales como la pendiente, el intercepto, el valor $p$ (p-value) y el error estándar.

## 📂 Estructura del Repositorio
Basado en la organización del directorio local, el proyecto se compone de:
* `sea_level_predictor.py`: Script principal que contiene las funciones de carga de datos, cálculo estadístico y graficación.
* `epa-sea-level.csv`: El dataset histórico con las mediciones del nivel del mar.
* `main.py`: Archivo ejecutable de control para correr los procesos y pruebas de rendimiento.
* `test_module.py`: Unidad de pruebas automatizadas para asegurar la precisión de los cálculos matemáticos del modelo.
