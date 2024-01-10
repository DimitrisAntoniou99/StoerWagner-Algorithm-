import numpy as np
def dfs(g, prev, u):
    for x in range(1, m):
        if g[u-1][x] > 0 and prev[x] == -1:
            prev[x] = u
            dfs(g, prev, x+1)

# Ford-fulkerson algorithm taking in a directed graph, number of vertices, source and sink.
def ford_fulkerson(g, num_v, s, t):
    flow = 0
    while True:
        prev = [-1] * num_v
        min_c = float("inf")
        dfs(g, prev, s)
        if prev[-1] == -1:
            return flow
        v = num_v
        while prev[v-1] != -1:
            min_c = min(min_c, g[prev[v-1]-1][v-1])
            v = prev[v-1]
        v = num_v
        while prev[v-1] != -1:
            g[prev[v-1]-1][v-1] -= min_c
            g[v-1][prev[v-1]-1] += min_c
            v = prev[v-1]
        flow += min_c


print("------------------Ford-Fulkerson Algorithm-------------------")
#time1 = dt.datetime.now()
k=input("Give a text file:")
f = open(k)
a = f.readline()
a = a.split()
m = int(a[0])
n = int(a[1])
edges=[]
#print(m)
g = np.zeros((m+1,m+1))
for i in range(m):
    a = f.readline()
    a = a.split()
    x = int(a[0])
    edges.append(x)
    y = int(a[1])
    edges.append(y)
    z = int(a[2])
    g[x][y]=z
    s=1
    x+=1
    t=x
    #print(x)
print(ford_fulkerson(g,m,1,9))