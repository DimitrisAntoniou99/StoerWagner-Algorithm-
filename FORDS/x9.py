import time

import numpy as np


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
    n = len(C) # C is the capacity matrix
    F = [[0] * n for i in range(n)]
    path = bfs(C, F, s, t)
    while path != None:
        flow = min(C[u][v] - F[u][v] for u, v in path)
        for u, v in path:
            F[u][v] += flow
            F[v][u] -= flow
        path = bfs(C, F, s, t)
    return sum(F[s][i] for i in range(n))

C=np.loadtxt("input_random_01_10.txt").tolist()
print(C)
source=C[0][0]
print(source)
sink=C[-1][1]
print(sink)
max_flow_value = max_flow(C, source, sink)
print(source,sink ,"max_flow_value is: ", max_flow_value)