# -*- coding: utf-8 -*-
"""
Created on Mon Apr 10 16:15:44 2017

@author: JHNLYD001
"""
from Ass1 import edges
import numpy as np

deltalst = []


def coords(d,drs):
    dr = np.deg2rad(drs)
    dx = d*np.cos(dr)
    dy = d*np.sin(dr)    
    
    deltalst.append(dy)
    deltalst.append(dx)
    
    


