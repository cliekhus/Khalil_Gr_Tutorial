# -*- coding: utf-8 -*-
"""
Created on Fri Aug 28 20:12:17 2020

@author: chelsea
"""

def make_color_map(start_color, end_color):
    
    #from matplotlib import cm
    from matplotlib.colors import ListedColormap
    import numpy as np
    
    rbg_start = start_color.lstrip('#')
    rbg_start = tuple(int(rbg_start[i:i+2], 16) for i in (0, 2, 4))
    
    rbg_end = end_color.lstrip('#')
    rbg_end = tuple(int(rbg_end[i:i+2], 16) for i in (0, 2, 4))
    
    
    number_colors = 1000

    
    R = np.linspace(rbg_start[0]/255, rbg_end[0]/255, number_colors)
    G = np.linspace(rbg_start[1]/255, rbg_end[1]/255, number_colors)
    B = np.linspace(rbg_start[2]/255, rbg_end[2]/255, number_colors)
    
    new_colors = np.transpose(np.vstack((R, G, B, np.ones(number_colors))))
    
    return ListedColormap(new_colors)