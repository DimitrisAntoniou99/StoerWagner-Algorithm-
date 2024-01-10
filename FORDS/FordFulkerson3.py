###################################################################################################
#Implementation of the Ford-Fulkerson Max-Flow in Python
# Dimitris Antoniou AM:4027
import networkx as nx
import time
import sys



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

C = [[0, 3, 3, 0, 0, 0],  # s
     [0, 0, 2, 3, 0, 0],  # o
     [0, 0, 0, 0, 2, 0],  # p
     [0, 0, 0, 0, 4, 2],  # q
     [0, 0, 0, 0, 0, 2],  # r
     [0, 0, 0, 0, 0, 0]]  # t


source = 0  # s
sink = 1  # t
print("Ford-Fulkerson algorithm")
max_flow_value = max_flow(C, source, sink)
print("max_flow_value is: ", max_flow_value)

def bfs(C, F, s, t):
    undirected=G.to_undirected()
    stack = [s]
    paths = undirected({s: []})
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

###################################################################################################
############################## MAIN ###############################################################
if __name__ == '__main__':
    print("----------------Ford Fulkerson Algorithm----------------")
    x = input("Give a input file with txt extension: ")
    # read the list of edges in networkx graph object
    G = nx.read_edgelist(x, delimiter=' ', nodetype=int, encoding="utf-8", data=(('value', int),))
    nx.set_edge_attributes(G, 0, 'flow')
    y=list(G.edges)
    print(y)
    z=list(G.nodes)
    s=z[0]
    z.pop(0)
    # add flow attribute as 0 to the graph
    start_time = time.time()
    # initialise source(s) and sink (t)
    for i in range(len(z)):
        t = z[4]
        flow = max_flow(G, s, t)
        print(s, t, " Max Flow: ", flow)
    # print execution time of the algorithm
    print("--- %s seconds ---" % (time.time() - start_time))