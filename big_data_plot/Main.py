# -*- coding: utf-8 -*-
"""
Created on Thu Aug 27 13:00:26 2020

@author: chelsea
"""

from common.Load_Data import load_raw_data
from pathlib import Path
import pickle

input_folder = "C:/Users/chelsea/OneDrive/Documents/etc/ScienceThinks/Python_Course"
save_folder = "D:/python_practice"


reload_raw = False #True means reload the raw data, false means use pickled data


min_energy_p = 350
max_energy_p = 450

max_energy_m = 300
min_energy_m = 200



print('_____________________________________________________')
print('start rawdata')
print('_____________________________________________________')



if reload_raw:
    raw_data = load_raw_data(input_folder, save_folder)
else:

    with open(Path(save_folder) / 'rawdata.pkl', 'rb') as f:
        raw_data = pickle.load(f)
        
        
        
        
print('_____________________________________________________')
print('start prodata')
print('_____________________________________________________')



pro_data_p = raw_data.make_slice(min_energy_p, max_energy_p)
pro_data_m = raw_data.make_slice(min_energy_m, max_energy_m)

pro_data_p.fit_slice(False)
pro_data_m.fit_slice(False)


pro_data_p.plot_two_data(pro_data_m)











