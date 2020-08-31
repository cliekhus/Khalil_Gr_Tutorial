# -*- coding: utf-8 -*-
"""
Created on Wed Aug 26 12:16:20 2020

@author: chelsea
"""



def load_raw_data(input_folder, save_folder):
    
    import numpy as np
    from pathlib import Path
    import pickle
    import os
    from Raw_Data_Class import raw_data as RDC
    
    
    raw_data = RDC()
    
    folder = Path(input_folder)
    
    data = np.loadtxt(open(folder / 'data.csv', 'rb'), delimiter = ',')
    time = np.loadtxt(open(folder / 'time.csv', 'rb'), delimiter = ',')
    energy = np.loadtxt(open(folder / 'energy.csv', 'rb'), delimiter = ',')
    
    raw_data.change_value(energy = energy, time = time, data_matrix = data)
    
    raw_data.load_path = folder
    
    save_DIR = Path(save_folder) / 'rawdata.pkl'
    
    if not os.path.isdir(Path(save_folder)):
        os.mkdir(Path(save_folder))
        
    with open(save_DIR, 'wb') as f:
        pickle.dump(raw_data,f)
        
    return raw_data
    

    
    
    
    
    
    