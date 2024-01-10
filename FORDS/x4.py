# Ford-Fulkerson Algorithm
# By Dimitris Antoniou

import time
import datetime as dt
import numpy as np
import queue

def bfs(C, F, s, t):
    stack = [s]
    paths = {s: []}
    if s == t:
        return paths[s]
    while (stack):
        u = stack.pop()
        for v in range(len(C)):
            if (C[u][v] - F[u][v] > 0) and v not in paths:
                paths[v] = paths[u] + [(u, v)]
                #print(paths)
                if v == t:
                    return paths[v]
                stack.append(v)
    return None

def max_flow(C, s, t):
    n = len(C)  # C is the capacity matrix
    F = [[0] * n for i in range(n)]
    path = bfs(C, F, s, t)
    while path != None:
        flow = min(C[u][v] - F[u][v] for u, v in path)
        for u, v in path:
            F[u][v] += flow
            F[v][u] -= flow
        path = bfs(C, F, s, t)
    return sum(F[s][i] for i in range(n))

print("------------------Ford-Fulkerson Algorithm-------------------")
time1 = dt.datetime.now()
k=input("Give a text file:")
f = open(k)
a = f.readline()
a = a.split()
m = int(a[0])
n = int(a[1])
edges=[]
#print(m)
C = np.zeros((m+1,m+1))
for i in range(m):
    a = f.readline()
    a = a.split()
    x = int(a[0])
    edges.append(x)
    y = int(a[1])
    edges.append(y)
    z = int(a[2])
    C[x][y]=z
    s=1
    x+=1
    t=x
    print(x)
    print(s,x,max_flow(C,s,x))