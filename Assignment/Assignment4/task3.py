# -*- coding: utf-8 -*-
"""task3.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1WOff8-qWTweQtJzYD1ZsfDzIbN9SVZeC
"""

arr = []
visited = []
def apply_DFS(dic,source,start): 
    if source not in visited:
        arr.append(source)
        for destin in dic[source]:
            if dic[source] != None and destin not in visited : 
                apply_DFS(dic,destin,start)
                visited.append(destin)
                dic[source].remove(destin)
    if dic[source] != None :
        start = source
        for destin in dic[source] :
            dic[source].remove(destin)
            apply_DFS(dic,source,start)
            
    return arr 

def print_arr(lis) :
    store = ''
    for i in lis :
        store += str(i) + ' '
    w.write(store)
   
f = open('/content/input3_1.txt','r')
w = open('/content/output3_1.txt','w')
f1 = f.readline().split()
v = int(f1[0])
c = int(f1[1].strip())
dic = {}
for i in range(1,v+1) :
    if i not in dic :
        dic[i] = []

for j in range(0,c) :
    rd = f.readline().split()
    source,destin = int(rd[0]),int(rd[1])
    if (source in dic) and (destin not in dic[source]) :
        dic[source].append(destin)
visited = [0]*(max(dic)+1)
for i,k in enumerate(dic.keys()) :
    if i == 0 :
        l = k 
        a = apply_DFS(dic,k,l)
print_arr(a)
        
w.close()