# -*- coding: utf-8 -*-
"""
Created on Wed Aug 26 13:26:43 2020

@author: chelsea
"""

class pro_data:
    
    _defaults = ("energy", "time", "e_slice", "min_energy", "max_energy", "data_matrix")
    
    _default_value = None
    
    def __init__(self, **kwargs):
        
        self.__dict__.update(dict.fromkeys(self._defaults, self._default_value))
        self.__dict__.update(kwargs)
        
    def change_value(self, **kwargs):
        self.__dict__.update(kwargs)
        
    def get_keys(self):
        return self.__dict__.keys()
    
    def plot_two_data(self, pro_data):
        from common.Plot_Data import plot_two_data

        plot_two_data(self, pro_data)
     
    def fit_slice(self, plots_on):
        from common.Fit_Slice import fit_slice
        
        fit = fit_slice(self, plots_on)
        
        self.fit = fit

