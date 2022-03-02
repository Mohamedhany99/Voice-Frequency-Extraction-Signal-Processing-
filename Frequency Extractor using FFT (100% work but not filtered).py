# -*- coding: utf-8 -*-
"""
Created on Sun Mar 29 00:52:24 2020

@author: aa
"""
from scipy.io import wavfile
#import wave
#import struct
import numpy as np
#first way to enter the wave file data (nframes + frame rate) using the wave lib
#wave_file = wave.open("HH3.wav",'r')
#nframes = wave_file.getnframes()
#data = wave_file.readframes(nframes)
#frate = wave_file.getframerate
#wave_file.close()
#data = struct.unpack('{n}h'.format(n=data_size), data)


#second way to enter the wave file data (nframes + frame rate) using wavfile lib (100% work done but it is not filtered)
fname = "test.wav"
frate, data = wavfile.read(fname)


data = np.array(data)
w = np.fft.fft(data)
freqs = np.fft.fftfreq(len(w))
print(freqs.min(), freqs.max())
# (-0.5, 0.499975)

# Find the peak in the coefficients
idx = np.argmax(np.abs(w))
freq = freqs[idx]
freq_in_hertz = abs(freq * frate)
print(freq_in_hertz)
# 439.8975 for the test.wav
