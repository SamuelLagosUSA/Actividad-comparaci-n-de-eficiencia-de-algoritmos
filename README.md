# Comparación de Factorial Recursivo vs. Iterativo (Python y C)

## Propósito de la tarea
La finalidad de este proyecto fue comparar la ejecución y uso de memoria de dos versiones del cálculo del factorial de un número entero positivo:

- Versión recursiva  
- Versión iterativa  

Se realizaron las pruebas tanto en Python como en C, con el fin de observar las diferencias en tiempo de ejecución y consumo de memoria entre ambos enfoques y lenguajes.

---

## Aplicación de las funciones

### Python
En Python se desarrollaron dos funciones:  

- **factorial_recursivo(n)**: llama a sí misma hasta llegar al caso base (n == 0 o n == 1).  
- **factorial_iterativo(n)**: utiliza un bucle `for` para multiplicar a todos los números enteros del 2 al n.  

Para minimizar la variabilidad en los resultados, cada función se ejecutó **10 000 veces** y se calculó el tiempo promedio.

### C
En C se empleó la misma lógica:  

- **factorial_recursivo(int n)**: implementación recursiva clásica.  
- **factorial_iterativo(int n)**: implementación con un bucle `for`.  

En ambos casos, el resultado se almacenó en una variable **unsigned long long** para soportar números grandes.

---

## Métodos de medición

### Python
- **Tiempo**: se utilizó `time.perf_counter()` para obtener una medición precisa antes y después de la ejecución.  
- **Memoria**: se empleó la librería `memory_profiler` y su función `memory_usage()` para capturar el pico de memoria.

### C
- **Tiempo**: medido con la función `clock()` de `<time.h>`.  
- **Memoria**: con `getrusage()` de `<sys/resource.h>` para obtener el uso máximo de memoria en KB.

Los resultados en C se guardaron directamente en **resultados.csv** para su análisis posterior.

---

## Resumen de hallazgos

- **Tiempo de ejecución**: la versión iterativa fue siempre más rápida en ambos lenguajes, debido a que la recursión añade sobrecarga por llamadas a función.  
- **Consumo de memoria**: la recursiva usó más memoria por el uso de la pila en cada llamada, mientras que la iterativa mantuvo un uso constante.  
- **Python vs C**: C tuvo tiempos mucho menores gracias a ser compilado y tener menos sobrecarga, aunque la diferencia recursivo/iterativo se mantuvo.

---

## Comparaciones gráficas

En Python se generaron:  
- **comparacion_tiempo.png**: muestra cómo crece el tiempo con n, favoreciendo la versión iterativa.  
- **comparacion_memoria.png**: evidencia que la recursión consume más memoria, especialmente con valores grandes de n.  

En C, los datos de **resultados.csv** permiten generar gráficos equivalentes que confirman las mismas conclusiones.

---

## Archivos generados

- **comparacion_tiempo.png** — gráfico de tiempos en Python.  
- **comparacion_memoria.png** — gráfico de memoria en Python.  
- **resultados.csv** — resultados crudos de las pruebas en C.  

---

## Conclusión
La implementación iterativa es más eficiente en tiempo y memoria. La recursiva, aunque más clara conceptualmente, no es óptima para valores grandes de n y puede causar desbordamientos de pila en ciertos entornos.


Conclusión
La implementación iterativa es más eficiente en tiempo y memoria. La recursiva, aunque más clara conceptualmente, no es óptima para valores grandes de n y puede causar desbordamientos de pila en ciertos entornos.
