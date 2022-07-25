# -*- coding: utf-8 -*-
"""

Reads sampled signal from CSV file and takes FFT,
then saves file and prints the primary frequency of the signal.


Created on Fri Jul 22 20:24:27 2022

@author: dlens
"""

import numpy as np
from scipy.fft import rfft, rfftfreq
from matplotlib import pyplot as plt

# read csv

Raw_Signal = np.genfromtxt("data.csv", delimiter=",")
Signal = Raw_Signal.astype('float')

#Number of samples
N = Signal.size

#Sampling Rate (1 MHz)
SAMPLE_RATE = 1000000

#Take FFT and setup x-axis
yf = rfft(Signal)
xf = rfftfreq(N, 1 / SAMPLE_RATE)

#plot
plt.plot(xf, np.abs(yf))
plt.xlim(0, 150000)
plt.show()

#Find primary frequency
yf_abs = np.abs(yf)
PrimFreq_Amp = np.max(yf_abs)
for coef, freq in zip(yf_abs, xf):
    if (coef == PrimFreq_Amp):
        PrimFreq = freq
        print("The primary frequency is " + str(PrimFreq) + " Hz")
 
#Save complex values from FFT to a new CSV file
np.savetxt("FFTofData.csv", yf, 
              delimiter = ",")

#Save frequency and amplitude data to a new CSV file
f = open("FrequencySpectrum.csv", "w")
f.write("{},{}\n".format("Frequency (Hz)", "Amplitude"))
for x in zip(xf, yf_abs):
    f.write("{},{}\n".format(x[0], x[1]))
f.close()  
       
