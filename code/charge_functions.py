import os
import numpy as np
import matplotlib.pyplot as plt
import scipy
import uproot
import matplotlib
matplotlib.rcParams.update({'font.size': 22})

def wave(fname):
    f = uproot.open(fname)
    data = f['Data']
    
    # convert to np arrays
    data_dict = {}
    for k in data.keys():
        print(k)
        data_dict[k] = data[k].array(library='np')
    for i in range(len(data_dict['Samples'])):
        data_dict['Samples'][i] = np.array(data_dict['Samples'][i])    
    plt.figure(figsize=(15,7), facecolor='w')

    plt.plot(data_dict['Samples'][0])
         
    plt.grid()
    
    
def waveform(data_dict, n):
    plt.figure(figsize=(15,7), facecolor='w')

    for i in range(min(n,len(data_dict['Samples']))):
        plt.plot(data_dict['Samples'][i])
         
    plt.grid()
    plt.show()

def integrate_waveform(wave):
    shifted_waveform = wave-250
    mask = (shifted_waveform<0)
    
    return -sum(shifted_waveform[mask])

def get_charge_array(samples):
    q = np.zeros(len(samples))
    for i in range(len(samples)):
        q[i] = integrate_waveform(samples[i])
    return q
    