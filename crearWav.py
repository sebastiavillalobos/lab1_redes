#!/usr/bin/python3
# -*- coding: cp1252 -*-
# Se importa numpy para usar las funciones sen,
# array y la constante pi
import numpy as np
# Se importa para generar el archivo de audio
import wave
# Se importa struct para empaquetar los valores
# de las muestras en hexadecimal
import struct
# Se utiliza para generar gráficos
import matplotlib.pyplot as plt

# Se utiliza para realizar la transformada de fourier
import scipy.fft 

# aqui estoy agregando comentarios :)?

# aqui algo?

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

'''
onda = []

for x in range(numeroDeMuestras) :
    valor = 2 * np.pi * frecuencia * x/tasaDeMuestreo
    onda.append(valor)
'''

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

# LINEAS QUE GENERAN EL GRÁFICO
'''
# Se genera la recta de la primera onda
grafico = plt.plot(onda[0:100], label='onda 1')
# Se genera la recta de la segunda onda 
grafico2 = plt.plot(onda2[0:100], label='onda 2')

# Se genera la recta de la segunda onda 
grafico3 = plt.plot(onda3[0:100], label='onda 3')

# Se genera el gráfico de la onda resultante 
grafico3 = plt.plot(ondaResultante[0:100], label='onda resultante')

'''
freq = scipy.fft.fft(ondaResultante)
xf = scipy.fft.fftfreq(numeroDeMuestras, 1/tasaDeMuestreo)

plt.plot(xf, np.abs(freq))
# Se agrega un título al gráfico 
plt.title('Señal mostrada')
# Se muestra la leyenda para identificar las ondas 
#plt.legend()
# Se muestra el gráfico por pantalla
plt.show()