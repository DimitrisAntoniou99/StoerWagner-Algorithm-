# Ford Fulkerson Algorithm
# By Carson Forsyth
# From Professor Mingfu Shao
# CMPSCI 465 @ PSU, FA2020
#S.O.S DIAVASEI TA ORISMATA APO TO CMD
# An algorithm to calculate the maximum network flow through a directed graph.
# A greedy function to solve in O(Ef); f is the graphs maximum flow, E is the
# number of edges; input is given as a .txt. The first line gives two numbers n and m;
# n is the number of vertices, m is the number of edges. Each of the following lines
# gives three integers a, b, c separated by space which means
# there is an edge from a to b with capacity c.

# Simple depth first algorithm to fill in a list of prior nodes to reach node at each list index.
def dfs(g, prev, u):
    for x in range(1, num_v):
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

# Get input nodes and run ford-fulkerson
num_v, num_e = [int(x) for x in input().split()]
graph = [[0]*num_v for v in range(num_v)]
for i in range(num_e):
    edge = ([int(x) for x in input().split()])
    graph[edge[0]-1][edge[1]-1] += edge[2]
print(ford_fulkerson(graph, num_v, 1, num_v))