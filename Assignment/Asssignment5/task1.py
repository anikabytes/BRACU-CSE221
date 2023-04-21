# -*- coding: utf-8 -*-
"""task1.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1w6YyWAsKCtnGmN-XeJ0SK1dFgr6DQkqR
"""

import math

def Dijkstra(graph, source):

    dist = [math.inf] * len(graph)
    dist[source] = 0
    visited = [False] * len(graph)
    prev = [0] * len(graph)
    for cout in range(len(graph)):
        x = minDistance(graph,dist, visited)
        visited[x] = True 
        for y in range(0,len(graph)):
            if graph[x][y] > 0 and visited[y] == False : 
                if dist[y] > dist[x] + graph[x][y] : 
                    dist[y] = dist[x] + graph[x][y]
                    

    return dist

def minDistance(graph, dist, visited):
        min = math.inf
        for u in range(len(graph)):
            if dist[u] < min and visited[u] == False :
                min = dist[u]
                min_index = u
        return min_index


import numpy as np 
f = open('/content/input1.txt','r')
w = open('/content/output1.txt','w')
f1 = f.readlines()
lis = []
lis2 = []
for i in f1 :
    lis.append((i.strip()).split())

for i in range(0,len(lis)) : 
    if lis[i][0] not in lis2 :
        lis2.append(lis[i][0])
    if (lis[i][0] != lis[i][1]) and (lis[i][1] not in lis2) :
        lis2.append(lis[i][1])

arr = np.zeros((len(lis2),len(lis2)))

for k in range(0,len(lis))   : 
    src = 0 
    dest = 0 
    for j in range(0,len(lis2)) :
        if lis2[j] == lis[k][0] :
            src = j 
        if lis2[j] == lis[k][1] :
            dest = j 
    arr[src,dest] = lis[k][2]

distance = Dijkstra(arr,0)

for i in range(0,len(lis2)) :
    if (lis2[i] == 'MOGHBAZAR') :
        w.write(f'Shortest distance from Motijheel to MOGHBAZAR --> {distance[i]} ')

w.close()

"Here, Dijkstra Algorithm is used instead of BFS because traffic level is considered to be the weights of the edges connecting the nodes ,\
thus making this graph as a 'weighted graph'. \nBFS can only be used for unweighted graphs , \
and Dijkstra can be used for weighted graphs."