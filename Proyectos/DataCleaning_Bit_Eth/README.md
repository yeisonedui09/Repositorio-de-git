# Data Cleaning & Analysis: Bitcoin & Ethereum 🪙📊

Este proyecto está enfocado en la adquisición, limpieza profunda, alineación y análisis exploratorio avanzado de series temporales financieras correspondientes a los precios históricos de cierre de Bitcoin (BTC) y Ethereum (ETH).

## 📋 Objetivos del Proyecto
1. **Importación y Estructuración:** Carga de datos crudos distribuidos en diferentes formatos temporales y unificación bajo un mismo huso horario e índice cronológico.
2. **Tratamiento de Datos Faltantes (Data Imputation):** Identificación de "gaps" temporales y aplicación de técnicas de interpolación lineal y *Forward Fill* (ffill) justificadas por la naturaleza continua 24/7 de los mercados cripto.
3. **Detección y Mitigación de Outliers:** Implementación de filtros estadísticos basados en el Z-Score y el Rango Intercuartílico (IQR) para separar la volatilidad extrema natural de errores de registro en el feed de datos.
4. **Análisis de Rendimientos:** Transformación de precios absolutos a rendimientos logarítmicos para un análisis estadístico estacionario.

## 📊 Marco Teórico y Fórmulas
Para evitar el sesgo por escala y estabilizar la varianza de las series temporales, los precios de cierre se transforman en **Rendimientos Logarítmicos ($R_t$)**:

$$R_t = \ln\left(\frac{P_t}{P_{t-1}}\right) = \ln(P_t) - \ln(P_{t-1})$$

Para la detección de anomalías o valores atípicos que no correspondan al comportamiento del mercado, se aplica el criterio del **Rango Intercuartílico (IQR)**:

$$\text{IQR} = Q_3 - Q_1$$
$$\text{Límite Inferior} = Q_1 - 1.5 \times \text{IQR} \quad \text{;} \quad \text{Límite Superior} = Q_3 + 1.5 \times \text{IQR}$$

## 🛠️ Tecnologías y Librerías
* **Python 3.x**
* **Pandas:** Conversión de tipos de datos con `to_datetime()`, remuestreo temporal (`resample()`), y métodos de imputación avanzada.
* **NumPy:** Computación vectorizada para el cálculo exponencial y logarítmico de los retornos.
* **Seaborn & Matplotlib:** Visualización de distribuciones (KDE plots) y diagramas de caja (Box Plots) pre y post-limpieza.

## 📂 Estructura sugerida del Repositorio
* `data_cleaning_crypto.py` / `DataCleaning.ipynb`: Script/Notebook con el pipeline completo de ETL.
* `dataset_bitcoin.csv` y `dataset_ethereum.csv`: Datos históricos de precios.
* `cleaned_crypto_portfolio.csv`: Dataset final unificado listo para modelos de Machine Learning.
