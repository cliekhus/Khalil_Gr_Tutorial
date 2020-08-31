# -*- coding: utf-8 -*-
"""
Created on Fri Aug 14 14:27:57 2020

@author: chelsea
"""

def convolved(t,a,rate,offset,t0,sig):
    
    import math
    import scipy.special as sp
    import numpy as np
    
    out = a*(1-sp.erf(1/math.sqrt(2)*(sig/rate-(t-t0)/sig)))*np.exp(-(t-t0)/rate)+offset
    
    #note, signal amplitude is actually: amp = a*2/exp(sig^2/(2*rate^2))
    
    #IRF = 2*sqrt(2*ln(2))*sig
    return out


def convolved_two(t,a1,a2,rate,offset1,offset2,t0,sig):

    import numpy as np
    
    out1 = convolved(t,a1,rate,offset1,t0,sig)
    out2 = convolved(t,a2,rate,offset2,t0,sig)
    
    return np.concatenate((out1, out2))
