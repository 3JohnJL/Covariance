# -*- coding: utf-8 -*-
"""
Created on Mon Apr 10 15:59:01 2017

@author: JHNLYD001
"""

import networkx as nx
import numpy as np
import sympy as sp




data = open("Ass1data.csv")
for t in range(0,1):
    data.readline()

    G = nx.DiGraph()
    
for line in data:
    s = line.split(';')
    node0 = s[0]
    node1 = s[1]
    dist = s[2]
    direc = s[3]
    erdist = float(s[4])
    erdrn = float(s[5])
    attribs = {'distance': int(dist), 'direction': int(direc), 'sigmadist':(erdist) ,'sigmadrn':(erdrn)}

    G.add_edge(node0, node1, attribs)
    
 

edges = G.edges()

coord_dict = {}

  
P1 = (100,200)

for edge in G.edges():
    data = G.get_edge_data(edge[0], edge[1])
    
    
    if G.in_degree(edge[0]) == 0:
        start = edge[0]
        coord_dict[edge[0]] = P1
test = list(nx.bfs_edges(G,start))
print(test)
 
d,z,xq,yq = sp.symbols('d z xq yq')
data_dict = {}
for point in test:
    data = G.get_edge_data(point[0], point[1])
    data_dict[point[1]] = data
    y = yq + d*sp.sin(z)
    x = xq + d*sp.cos(z)
    
    if point[0] == start:
        yf =y.subs({yq:P1[0], d:data['distance'], z:np.deg2rad(data['direction'])})
        xf =x.subs({xq:P1[1], d:data['distance'], z:np.deg2rad(data['direction'])})
        coord_dict[point[1]] = (yf,xf)   
        
    if point[0] in coord_dict.keys():
        p = point[0]
        yf = y.subs({yq:coord_dict[p][0], d:data['distance'], z:np.deg2rad(data['direction'])})
        xf = x.subs({xq:coord_dict[p][1], d:data['distance'], z:np.deg2rad(data['direction'])})
        coord_dict[point[1]] = (yf,xf)   
        
    