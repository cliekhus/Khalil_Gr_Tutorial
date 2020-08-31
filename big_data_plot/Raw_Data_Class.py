# -*- coding: utf-8 -*-
"""
Created on Thu Aug 27 13:21:20 2020

@author: chelsea
"""

class raw_data:
    
    _defaults = ("energy", "time", "data_matrix")
    
    _default_value = None
    
    def __init__(self, **kwargs):
        
        self.__dict__.update(dict.fromkeys(self._defaults, self._default_value))
        self.__dict__.update(kwargs)
        
    def change_value(self, **kwargs):
        self.__dict__.update(kwargs)
        
    def get_keys(self):
        return self.__dict__.keys()
    
    def make_slice(self, min_energy, max_energy):
        import numpy as np
        from Pro_Data_Class import pro_data as PDC
        
        pro_data = PDC()
        
        good_index = np.logical_and(self.energy < max_energy, self.energy > min_energy)
        e_slice = np.sum(self.data_matrix[good_index, :], axis = 0)
        
        pro_data.change_value(energy = self.energy, time = self.time, e_slice = e_slice, \
                              min_energy = min_energy, max_energy = max_energy, data_matrix = self.data_matrix)
        
        return pro_data