# -*- coding: utf-8 -*-
"""
Created on Mon Apr 10 16:15:44 2017

@author: JHNLYD001
"""
from Ass1 import edges
import numpy as np
import sympy as sp
deltalst = []
P1 = (100,200)


def delta(d,drs):
    
    
    dr = np.deg2rad(drs)
    dx = d*np.cos(dr)
    dy = d*np.sin(dr)    
        
    deltalst.append(dy)
    deltalst.append(dx)
    return(dy,dx)
    


    
