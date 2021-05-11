# rama del seba, editada en ubuntu
import numpy as np
import wavio# Parameters
rate = 16000    # samples per second
T = 5           # sample duration (seconds)
f1= 440.0       # sound frequency (Hz)# Compute waveform samples
f2= 554.37       # sound frequency (Hz)# Compute waveform samples
f3= 629.25       # sound frequency (Hz)# Compute waveform samples
t = np.linspace(0, T, T*rate, endpoint=False)
x1 = np.sin(2*np.pi * f1 * t)
x2 = np.sin(2*np.pi * f2 * t)
x3 = np.sin(2*np.pi * f3 * t)
x4 = x1+x2+x3
wavio.write("sonidos/sine.wav", x4, rate, sampwidth=3)


