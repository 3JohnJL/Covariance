# -*- coding: utf-8 -*-
"""
Created on Mon Apr 10 19:00:03 2017

@author: JHNLYD001
"""
import networkx as nx
import sympy as sp
import numpy as np
from Ass1 import test,G,coord_dict,P1,data_dict


error_list = []
error_dict = {}
for edge in test:
    data = G.get_edge_data(edge[0], edge[1])  
    errors = data['sigmadist']
    errord = np.deg2rad(data['sigmadrn']/3600)     
    error_list.append(errors**2)
    error_list.append(errord**2)
    error_dict[edge[1]] = (errors,errord)

covar_obs = np.diag(error_list)    

points = G.nodes
    
#print(covar_obs)
#___________________________________________
P1 = (100,200)
d2,z2,d3,z3,d4,z4,d5,z5,d6,z6,d7,z7,d8,z8,d9,z9 = sp.symbols('d2,z2,d3,z3,d4,z4,d5,z5,d6,z6,d7,z7,d8,z8,d9,z9')

p2y = P1[0] + d2*sp.sin(z2)
p2x = P1[1] + d2*sp.cos(z2)
p3y = P1[0] + d3*sp.sin(z3)
p3x = P1[0] + d3*sp.sin(z3)
p4y = p3y + d4*sp.sin(z4)
p4x = p3x + d4*sp.cos(z4)
p5y = p3y + d5*sp.sin(z5)
p5x = p3x + d5*sp.cos(z5)
p6y = p5y + d6*sp.sin(z6)
p6x = p5x + d6*sp.cos(z6)
p7y = p5y + d7*sp.sin(z7)
p7x = p5x + d7*sp.cos(z7)
p8y = p6y + d8*sp.sin(z8)
p8x = p6x + d8*sp.cos(z8)
p9y = p6y + d9*sp.sin(z9)
p9x = p6x + d9*sp.cos(z9)

P1d, P1z, P2d, P2z, P3d, P3z, P4d, P4z, P5d, P5z, P6d, P6z, P7d, P7z, P8d, P8z, P9d, P9z = sp.symbols('P1d P1z P2d P2z P3d P3z P4d P4z P5d P5z P6d P6z P7d P7z P8d P8z P9d P9z')


idmat = np.matrix([[1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                   [1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                   [0,0,1,1,0,0,0,0,0,0,0,0,0,0,0,0],
                   [0,0,1,1,0,0,0,0,0,0,0,0,0,0,0,0],
                   [0,0,1,1,1,1,0,0,0,0,0,0,0,0,0,0],
                   [0,0,1,1,1,1,0,0,0,0,0,0,0,0,0,0],
                   [0,0,1,1,0,0,1,1,0,0,0,0,0,0,0,0],
                   [0,0,1,1,0,0,1,1,0,0,0,0,0,0,0,0],
                   [0,0,1,1,0,0,1,1,1,1,0,0,0,0,0,0],
                   [0,0,1,1,0,0,1,1,1,1,0,0,0,0,0,0],
                   [0,0,1,1,0,0,1,1,0,0,1,1,0,0,0,0],
                   [0,0,1,1,0,0,1,1,0,0,1,1,0,0,0,0],
                   [0,0,1,1,0,0,1,1,1,1,0,0,1,1,0,0],
                   [0,0,1,1,0,0,1,1,1,1,0,0,1,1,0,0],
                   [0,0,1,1,0,0,1,1,1,1,0,0,0,0,1,1],
                   [0,0,1,1,0,0,1,1,1,1,0,0,0,0,1,1]])

Cv = idmat*covar_obs
P = sp.Matrix([[p2y],[p2x],[p3y],[p3x],[p4y],[p4x],[p5y],[p5x],[p6y],[p6x],[p7y],[p7x],[p8y],[p8x],[p9y],[p9x]])
J = P.jacobian([d2,z2,d3,z3,d4,z4,d5,z5,d6,z6,d7,z7,d8,z8,d9,z9])
Js = J.subs({d2:error_dict['P2'][0],z2:error_dict['P2'][1],d3:error_dict['P3'][0],d3:error_dict['P3'][1],d4:error_dict['P4'][0],z4:error_dict['P4'][1],d5:error_dict['P5'][0],z5:error_dict['P5'][1],d6:error_dict['P6'][0],z6:error_dict['P6'][1],d7:error_dict['P7'][0],z7:error_dict['P7'][1],d8:error_dict['P8'][0],z8:error_dict['P8'][1],d9:error_dict['P9'][0],z9:error_dict['P8'][1],d9:error_dict['P9'][0],z9:error_dict['P9'][1]})


Covar = Js*Cv*(Js.T)






#route_dict = {}
#for edge in G.edges():
#    data = G.get_edge_data(edge[0], edge[1])
#    
#    position = nx.shortest_path(G,source='P1',target=edge[1],weight=None)
#    route_dict[edge[1]] = position
#    
#
#for k in route_dict.keys():
#    n = route_dict[k]
#    print(n)
#    for i in range(1,len(n)):
#        deltas = delta(data_dict[n[i]]['distance'],data_dict[n[i]]['direction'])
#        new_dict[n[i]] = deltas
#
#print(new_dict)    
##
#
#
#        
        
#p2y = P1[0] + d*(sp.sin(z))
#p2x = P1[1] + d*(sp.cos(z))




#for i in test:
#    yy = coord_dict[i[0]][0]
#    xx = coord_dict[i[0]][1]
#    
#    data = G.get_edge_data(i[0],i[1])
#    dd = data['distance']
#    zz = np.deg2rad(data['direction'])
#
#    eqns(xx,yy,dd,zz)
#deltalst = []
#
#
#def coords(d,drs):
#    dr = np.deg2rad(drs)
#    dx = d*np.cos(dr)
#    dy = d*np.sin(dr)    
#    
#    deltalst.append(dy)
#    deltalst.append(dx)
