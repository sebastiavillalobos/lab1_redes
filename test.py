import numpy as np
import wave
import struct
# Parameters

# Frencuencias 
frecuencia = 440

frecuencia2 = 554.37

frecuencia3 = 629.25

# Número de muestras tomadas
# numeroDeMuestras = 48000 

# Cuántas muestras tomo en un segundo
tasaDeMuestreo = 16000.0 

numeroDeMuestras = int(tasaDeMuestreo * 5)
# Amplitud
amplitud = 1000

# Nombre del archivo
salida = 'ejemplo13-05.wav'

# Ecuaciones
# Se genera un vector con el valor
# del la ecuación del seno, para cada muestra
# Se elimina el valor de
# amplitud del cálculo para añadir la amplitud a la onda resultante
onda = [np.sin(2 * np.pi * frecuencia * x/tasaDeMuestreo) for x in range(numeroDeMuestras)]

onda2 = [np.sin(2 * np.pi * frecuencia2 * x/tasaDeMuestreo) for x in range(numeroDeMuestras)]

onda3 = [np.sin(2 * np.pi * frecuencia3 * x/tasaDeMuestreo) for x in range(numeroDeMuestras)]

# Se suman las dos ondas para generar la señal compuesta
ondaResultante = np.array(onda) + np.array(onda2) + np.array(onda3)

# LINEAS QUE GENERAN EL WAV
# Se declara el número de muestras que se utilizarán para el wav
nframes = numeroDeMuestras
# Se determina el tipo y nombre de la compresión
# el número de canales y el ancho de muestras
comptype = 'NONE'
compname = 'not compressed'
nchannels = 1
sampwidth = 2
# Se abre el archivo en modo de escritura
archivoSalida = wave.open(salida, 'w')
# Se configuran los parámetros del archivo a escribir
archivoSalida.setparams((nchannels, sampwidth, int(tasaDeMuestreo), nframes, comptype, compname))

# Se escribe cada muestra de la onda3 en el archivo de salida
for muestra in ondaResultante:
    archivoSalida.writeframes(struct.pack('h', int(muestra * amplitud)))
    
# Se cierra el archivo de salida
archivoSalida.close()