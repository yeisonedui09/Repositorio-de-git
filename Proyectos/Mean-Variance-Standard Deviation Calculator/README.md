# Mean-Variance-Standard Deviation Calculator 🔢📐

Este proyecto consiste en el diseño e implementación de una herramienta matemática modular capaz de transformar listas unidimensionales de datos numéricos en matrices bidimensionales indexadas, calculando un conjunto completo de métricas estadísticas multidimensionales utilizando computación paralela con NumPy.

## 📋 Funcionamiento del Módulo
La función principal recibe una lista de 9 dígitos enteros. Si la lista contiene menos o más elementos, el sistema genera de forma controlada una excepción de tipo `ValueError`. 

Si la entrada es correcta, los datos se reestructuran en una matriz cuadrada de $3 \times 3$ y se calculan las siguientes métricas distribuidas en tres ejes (Eje 0: columnas, Eje 1: filas, y la matriz aplanada completa):
1. Media Aritmética (`mean`)
2. Varianza (`variance`)
3. Desviación Estándar (`standard deviation`)
4. Valores Máximos (`max`)
5. Valores Mínimos (`min`)
6. Sumatorias Totales (`sum`)

## 📊 Marco Teórico y Fórmulas Matemáticas
Las operaciones matemáticas implementadas de forma vectorizada a lo largo de las dimensiones de la matriz siguen las definiciones estadísticas fundamentales:

### Media ($\mu$)
$$\mu = \frac{1}{N} \sum_{i=1}^{N} x_i$$

### Varianza ($\sigma^2$)
$$\sigma^2 = \frac{1}{N} \sum_{i=1}^{N} (x_i - \mu)^2$$

### Desviación Estándar ($\sigma$)
$$\sigma = \sqrt{\sigma^2} = \sqrt{\frac{1}{N} \sum_{i=1}^{N} (x_i - \mu)^2}$$

## 🛠️ Tecnologías y Librerías
* **Python 3.x**
* **NumPy:** Uso del objeto central `ndarray`, métodos de remuestreo estructural (`reshape()`), y funciones estadísticas optimizadas en C (`np.mean()`, `np.var()`, `np.std()`, `np.max()`, `np.min()`, `np.sum()`) especificando el argumento `axis`.

## 📂 Estructura sugerida del Repositorio
* `mean_var_std.py`: Módulo lógico que procesa la matriz y retorna el diccionario estadístico estructurado.
* `main.py`: Archivo de ejecución rápida para pruebas de consola.
