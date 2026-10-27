# Actividad Formativa 3: Implementación y Evaluación de Filtros Digitales

Este repositorio contiene el código y análisis para el diseño, implementación y evaluación de filtros digitales (FIR e IIR) aplicados a señales con ruido empleando Python.

## Objetivos
- Diseñar e implementar filtros Pasa Bajas, Pasa Altas y Pasa Bandas.
- Evaluar la respuesta en frecuencia de filtros IIR (Butterworth, Chebyshev) y FIR (Ventana Hamming).
- Comparar las señales contaminadas antes y después del filtrado en el dominio del tiempo y la frecuencia.

## Requisitos
Para ejecutar el código se requiere Python 3.x y las siguientes librerías:
- `numpy`
- `scipy`
- `matplotlib`

## Descripción del Código (`actividad3.py`)
1. **Generación de Señal:** Se genera una señal compuesta por tres frecuencias (5 Hz, 50 Hz y 200 Hz) con ruido blanco.
2. **Diseño de Filtros:**
   - **Pasa Bajas:** Butterworth de 4to orden ($f_c = 15\text{ Hz}$).
   - **Pasa Altas:** Chebyshev Tipo I ($f_c = 100\text{ Hz}$).
   - **Pasa Bandas:** FIR con ventana Hamming ($30 - 70\text{ Hz}$).
3. **Visualización:** Genera las gráficas comparativas en el dominio del tiempo y en la respuesta en frecuencia.
