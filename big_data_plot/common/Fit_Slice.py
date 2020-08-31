# -*- coding: utf-8 -*-
"""
Created on Fri Aug 28 11:55:14 2020

@author: chelsea
"""

def fit_slice(pro_data, plots_on):

    from .Fit_Functions import convolved
    import matplotlib.pyplot as plt
    from scipy.optimize import curve_fit
    
    a_start = 160 
    rate_start = 200
    offset_start = 150
    t0_start = 200
    sig_start = 80
    
    fit_start = convolved(pro_data.time, a_start, rate_start, offset_start, t0_start, sig_start)
    
    params, covs = curve_fit(convolved, pro_data.time, pro_data.e_slice, p0 = \
                             [a_start, rate_start, offset_start, t0_start, sig_start])
    
    fit_end = convolved(pro_data.time, *params)
    
    if plots_on:
        plt.figure()
        plt.plot(pro_data.time, pro_data.e_slice)
        plt.plot(pro_data.time, fit_start)
        plt.plot(pro_data.time, fit_end)
        
    return fit_end