'''
Generic functions for file readout
'''

import numpy as np
import uproot

def read_root_file(file_name):
    f=uproot.open(file_name)
    data=f['Data']
    data_dict={}
    for k in data.keys():
        data_dict[k]=data[k].array(library='np')
    if 'Samples' in data.keys():
        for i in range(len(data_dict['Samples'])):
            data_dict['Samples'][i] = np.array(data_dict['Samples'][i])
    return data_dict

def read_file(file_name):
    if file_name[-5:]==".root":
        return read_root_file(file_name)
    else:
        print("wrong format of the input file")
        return
