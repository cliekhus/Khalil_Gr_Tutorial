# -*- coding: utf-8 -*-
"""
Created on Sun Aug 16 17:24:20 2020

@author: chelsea
"""


green = '#009E73'
blue = '#0072b2'
yellow = '#e69f00'
red = '#c70039'

lightgreen = '#00d39a'
lightyellow = '#ffbc2b'
darkred = '#8c0028'
darkerred = '#64001c'
darkblue = '#005280'



def plot_data(pro_data, color, marker):
    
    import matplotlib.pyplot as plt
    
    plt.plot(pro_data.time, pro_data.e_slice, label = str((pro_data.min_energy + pro_data.max_energy)/2) + ' eV', \
             color = color, linestyle = 'none', marker = marker, markersize = 2)
    plt.plot(pro_data.time, pro_data.fit, color = color)
    

 
def make_rect(pro_data, linewidth):
    from matplotlib.patches import Rectangle
    
    delta_t = (pro_data.time[1]-pro_data.time[0])/4
    rect = Rectangle((pro_data.time[1]+delta_t, pro_data.min_energy), \
                 pro_data.time[-2]-pro_data.time[1]-delta_t, pro_data.max_energy-pro_data.min_energy, \
                 facecolor = 'None', edgecolor = 'black', linewidth = linewidth)

    return rect



def plot_two_data(pro_data1, pro_data2):
    
    import matplotlib.pyplot as plt
    
    import numpy as np

    from mpl_toolkits.axes_grid1.inset_locator import inset_axes
    from .Plot_Functions import make_color_map
    
    
    
    time_matrix, energy_matrix = np.meshgrid(pro_data1.time, pro_data1.energy)
    
    
    ################ slice plots with inset ####################

    fig, ax = plt.subplots(figsize=(3.3, 4))


    plot_data(pro_data1, yellow, 'o')
    plot_data(pro_data2, blue, 's')
    
    leg = plt.legend()
    leg.get_frame().set_edgecolor('k')
    leg.get_frame().set_linewidth(0.8)
    plt.xlabel('time (fs)')
    
    

    axins = inset_axes(ax, width=.9, height=.5, bbox_to_anchor=(.95, .28), bbox_transform=ax.transAxes)
    
    cmap_alt = make_color_map(darkblue, lightyellow)
    axins.pcolor(time_matrix, energy_matrix, pro_data1.data_matrix, cmap = cmap_alt)
    
    rect1 = make_rect(pro_data1, 1.5)
    axins.add_patch(rect1)
    
    rect2 = make_rect(pro_data2, 1.5)
    axins.add_patch(rect2)
    
    plt.tight_layout()

    
    
    

    ################ data matrix plot with rectangles ####################

    fig, ax = plt.subplots(1, figsize=(3.3, 4))
    plt.pcolor(time_matrix, energy_matrix, pro_data1.data_matrix, cmap = cmap_alt)#'viridis')
    plt.ylabel('energy (eV)')
    plt.xlabel('time (fs)')
    plt.colorbar()
    
    rect1 = make_rect(pro_data1, 2)
    ax.add_patch(rect1)
    
    rect2 = make_rect(pro_data2, 2)
    ax.add_patch(rect2)
    
    plt.tight_layout()
    
    
    

    
    ################ slice as top figure of data matrix ####################
    
    xlim_min = -100
    xlim_max = 1000
    
    fig, ax = plt.subplots(figsize = (3.3,5))
    ax = plt.subplot2grid((10,1), (0,0), colspan = 1, rowspan = 2)
    plot_data(pro_data1, yellow, 'o')
    plot_data(pro_data2, blue, 's')
    
    
    leg = plt.legend(bbox_to_anchor=(0.6,0.55))
    leg.get_frame().set_edgecolor('k')
    leg.get_frame().set_linewidth(0.8)
    leg.get_frame().set_alpha(1)
    plt.xlim((xlim_min, xlim_max))
    
    
    ax = plt.subplot2grid((10,1), (2,0), colspan = 1, rowspan = 8)
    im = plt.pcolor(time_matrix, energy_matrix, pro_data1.data_matrix, cmap = cmap_alt)
    
    rect1 = make_rect(pro_data1, 2)
    ax.add_patch(rect1)
    
    rect2 = make_rect(pro_data2, 2)
    ax.add_patch(rect2)
    
    plt.ylabel('energy (eV)')
    plt.xlabel('time (fs)')
    plt.colorbar(im, orientation = 'horizontal')
    plt.xlim((xlim_min, xlim_max))
    
    plt.tight_layout()

    
    