# -*- coding: utf-8 -*-
"""task2.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1n3j6tPjkRTrQj2sBjQJ0BMRg-IC5IJiJ
"""

import heapq
import math 

def Dijkstra(graph,source):

    dist = [0]*(len(graph)+1)
    visited = [False]*(len(graph)+1)
    prev = [0]*(len(graph)+1)
    queue = []

    for vertex in graph :
        if vertex != source:
            dist[vertex] = math.inf  
            prev[vertex] = None 
        heapq.heappush(queue,[dist[vertex],vertex])
       
    while queue: 
        u= heapq.heappop(queue)[1]
        if visited[u] == False :  
            visited[u] = True
            
            for v in graph[u]:
                val = dist[u] + graph[u][v]
                if val < dist[v]:   
                    dist[v] = val 
                    if u not in prev :
                        prev[v] = u 

                    idx = queue.index([math.inf,v])
  
                    if idx in queue:
                        queue.pop(idx)
                    heapq.heappush(queue,[dist[v], v])
  
    return dist

f = open("/content/input2.txt","r")
f_w = open("/content/output2.txt","w")
f = f.read()
f = f.split('\n')
T = int(f[0])
f = f[1:]
lis = []
for j in range(T):
    N = int(f[0].split()[0])
    M =int(f[0].split()[1])  

    f=f[1:]

    graph={}
    weight=0
 
    for j in range(M):  
        u=int(f[j].split()[0])
        v=int(f[j].split()[1])
        w=int(f[j].split()[2])


        if u in graph.keys():
            graph[u][v]=w

        else:
            graph[u]={}
            graph[u][v]=w
            
        if v in graph.keys():
            graph[v][u]=w

        else:
            graph[v]={}
            graph[v][u]=w
    weight=Dijkstra(graph,1)  
    lis.append(weight[len(graph)])
    f = f[M:]
    if len(f) <= 0 :
        break 
for i in lis :
    f_w.write(f'{i} \n')

f_w.close()