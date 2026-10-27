import numpy as np
import matplotlib.pyplot as plt
from scipy import signal

# ==========================================
# 1. Definición de la señal de entrada
# ==========================================
# Frecuencia de muestreo (Hz) y duración
fs = 1000  # 1000 muestras por segundo
t = np.linspace(0, 1.0, fs, endpoint=False)

# Creación de una señal compuesta por tres frecuencias:
# - Low frequency (señal de interés): 5 Hz
# - Mid frequency (señal deseada/intermedia): 50 Hz
# - High frequency (ruido no deseado): 200 Hz
f_baja = 5
f_media = 50
f_alta = 200

seno_bajo = np.sin(2 * np.pi * f_baja * t)
seno_medio = np.sin(2 * np.pi * f_media * t)
ruido_alto = 0.5 * np.sin(2 * np.pi * f_alta * t)
ruido_blanco = 0.3 * np.random.normal(size=t.shape)

# Señal combinada con ruido
senal_original = seno_bajo + seno_medio + ruido_alto + ruido_blanco

# ==========================================
# 2. Diseño de Filtros Digitales
# ==========================================
# Frecuencia de Nyquist
nyq = 0.5 * fs

# A. Filtro Pasa Bajas (IIR Butterworth) - Corta frecuencias > 15 Hz
fc_low = 15.0
b_iir_low, a_iir_low = signal.butter(N=4, Wn=fc_low / nyq, btype='low')

# B. Filtro Pasa Altas (IIR Chebyshev Tipo I) - Corta frecuencias < 100 Hz
fc_high = 100.0
b_iir_high, a_iir_high = signal.cheby1(N=4, rp=1, Wn=fc_high / nyq, btype='high')

# C. Filtro Pasa Bandas (FIR con Ventana Hamming) - Pasa frecuencias entre 30 Hz y 70 Hz
f_corta1, f_corta2 = 30.0, 70.0
numtaps = 101  # Orden del filtro FIR
b_fir_band = signal.firwin(numtaps, [f_corta1 / nyq, f_corta2 / nyq], pass_zero=False, window='hamming')
a_fir_band = 1.0  # Los filtros FIR no tienen denominador en H(z)

# ==========================================
# 3. Aplicación de los Filtros
# ==========================================
filtrada_pasa_bajas = signal.filtfilt(b_iir_low, a_iir_low, senal_original)
filtrada_pasa_altas = signal.filtfilt(b_iir_high, a_iir_high, senal_original)
filtrada_pasa_banda = signal.lfilter(b_fir_band, a_fir_band, senal_original)

# ==========================================
# 4. Visualización de los Resultados en el Tiempo
# ==========================================
plt.figure(figsize=(12, 10))

plt.subplot(4, 1, 1)
plt.plot(t, senal_original, color='gray', label='Señal Ruidosa Original')
plt.title('Análisis de Filtros Digitales en el Dominio del Tiempo')
plt.ylabel('Amplitud')
plt.legend(loc='upper right')
plt.grid(True)

plt.subplot(4, 1, 2)
plt.plot(t, filtrada_pasa_bajas, color='blue', label='Filtro Pasa Bajas Butterworth (fc = 15 Hz)')
plt.ylabel('Amplitud')
plt.legend(loc='upper right')
plt.grid(True)

plt.subplot(4, 1, 3)
plt.plot(t, filtrada_pasa_altas, color='red', label='Filtro Pasa Altas Chebyshev (fc = 100 Hz)')
plt.ylabel('Amplitud')
plt.legend(loc='upper right')
plt.grid(True)

plt.subplot(4, 1, 4)
plt.plot(t, filtrada_pasa_banda, color='green', label='Filtro Pasa Bandas FIR Hamming (30 - 70 Hz)')
plt.xlabel('Tiempo [s]')
plt.ylabel('Amplitud')
plt.legend(loc='upper right')
plt.grid(True)

plt.tight_layout()
plt.savefig('comparativa_senales.png', dpi=300)
plt.show()

# ==========================================
# 5. Respuesta en Frecuencia de los Filtros
# ==========================================
w_low, h_low = signal.freqz(b_iir_low, a_iir_low, fs=fs)
w_high, h_high = signal.freqz(b_iir_high, a_iir_high, fs=fs)
w_band, h_band = signal.freqz(b_fir_band, a_fir_band, fs=fs)

plt.figure(figsize=(10, 6))
plt.plot(w_low, 20 * np.log10(abs(h_low)), 'b', label='Pasa Bajas (Butterworth)')
plt.plot(w_high, 20 * np.log10(abs(h_high)), 'r', label='Pasa Altas (Chebyshev)')
plt.plot(w_band, 20 * np.log10(abs(h_band)), 'g', label='Pasa Bandas (FIR Hamming)')
plt.title('Respuesta en Frecuencia de los Filtros Diseñados')
plt.xlabel('Frecuencia [Hz]')
plt.ylabel('Magnitud [dB]')
plt.ylim(-80, 5)
plt.grid(True)
plt.legend(loc='lower right')
plt.savefig('respuesta_frecuencia.png', dpi=300)
plt.show()
