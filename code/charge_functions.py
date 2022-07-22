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
    