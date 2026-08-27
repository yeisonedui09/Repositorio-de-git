# Demographic Data Analyzer 👥📈

Este proyecto realiza un análisis estadístico descriptivo exhaustivo sobre un dataset demográfico extraído del censo de una población. El objetivo es responder a preguntas clave sobre las características socioeconómicas, niveles educativos e ingresos de los individuos utilizando operaciones vectorizadas de Pandas.

## 📋 Preguntas Analíticas Resueltas
1. ¿Cuál es el conteo exacto de la población según su origen étnico (raza)?
2. ¿Cuál es la edad promedio de los hombres dentro de la muestra?
3. ¿Cuál es el porcentaje exacto de personas que poseen un título universitario avanzado (`Bachelors`, `Masters` o `Doctorate`)?
4. ¿Qué porcentaje de personas con educación avanzada ganan más de 50K anuales frente a aquellos sin estudios superiores?
5. ¿Cuál es el número mínimo de horas de trabajo por semana y qué porcentaje de las personas que trabajan ese mínimo ganan >50K?
6. ¿Qué país tiene el mayor porcentaje de personas que ganan >50K y cuál es ese porcentaje?

## 📊 Marco Teórico y Fórmulas
El análisis se fundamenta en la teoría de la **Estadística Descriptiva** y la probabilidad condicional empírica. Para calcular los porcentajes condicionales (por ejemplo, personas con ingresos altos dado un nivel educativo superior) se implementa la fórmula de la frecuencia relativa:

$$P(A|B) = \frac{n(A \cap B)}{n(B)} \times 100$$

Donde:
* $n(A \cap B)$: Cantidad de individuos que cumplen con la condición de educación superior **Y** ganan más de 50K.
* $n(B)$: Total de individuos que tienen educación superior en el dataset.

## 🛠️ Tecnologías y Librerías
* **Python 3.x**
* **Pandas:** Uso intensivo de indexación condicional (`loc`, `iloc`), agrupamientos complejos (`groupby()`), ordenamiento de valores (`sort_values()`) y métodos de agregación (`mean()`, `value_counts()`).

## 📂 Estructura sugerida del Repositorio
* `demographic_data_analyzer.py`: Código principal estructurado con las funciones analíticas.
* `adult.data.csv`: Base de datos censal original.
* `main.py`: Script para ejecutar el análisis y validar los resultados impresos en consola.
