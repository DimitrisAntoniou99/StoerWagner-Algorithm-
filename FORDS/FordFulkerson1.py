###################################################################################################
#Implementation of the Ford-Fulkerson Max-Flow in Python 
# Dimitris Antoniou AM:4027
import networkx as nx
import time
import sys
from memory_profiler import profile

global numberOfPaths
numberOfPaths=0

def fordFulkerson(G, s, t, step=None):
    global numberOfPaths
    cumulativeFlow,p=0
    #Till there is an augmenting path keep looking for increase in flow
    while p:
        p, flow = dFS(G, s, t)
        cumulativeFlow += flow
        numberOfPaths += 1
        for y, x in zip(p, p[1:]):
            if G.has_edge(y, x):
                #increase flow if edge is present
                G[y][x][0]['flow'] += flow
            else:
                #decrease the flow if edge is not present
                G[x][y][0]['flow'] -= flow
        
        # Print the intermediate augmenting flow results
        if callable(step):
            step(G, p, flow, cumulativeFlow)
    return cumulativeFlow        

def dFS(G, s, t):
    undirected = G.to_undirected()
    explored = {s}
    stack = [(s, 0, dict(undirected[s]))]
    
    while stack:
        v, _, adjacent = stack[-1]
        # the node and sink is the same break
        while adjacent:
            u, e = adjacent.popitem()
            # if the edge is not explored then stop
            if u not in explored:
                break
        else:
            stack.pop()
            continue
        inDirection = G.has_edge(v, u)
        capacity = e[0]['value']
        flow = e[0]['flow']
        adjacent = dict(undirected[u])
        # increase or redirect flow at the edge
        if inDirection and flow < capacity:
            # increase the flow at the edge and append to stack
            stack.append((u, capacity - flow, adjacent))
            explored.add(u)
        elif not inDirection and flow:
            # redirect the flow at the edge and append to stack
            stack.append((u, flow, adjacent))
            explored.add(u)
    # min weight of all the edges is set as flow
    flow = min((f for _, f, _ in stack[1:]), default=0)
    # augmenting path from s to t
    path = [v for v, _, _ in stack]    
    return path, flow

def MaxFlow(G, s, t, step=None):
    global numberOfPaths
    cumulativeFlow, p=0, True
    while p:
        p, flow = dFS1(G, s, t)
        cumulativeFlow += flow
        numberOfPaths += 1
        for y, x in zip(p, p[1:]):
            if G.has_edge(y, x):
                G[y][x]['flow'] += flow
            else:
                G[x][y]['flow'] -= flow
        if callable(step):
            step(G, p, flow, cumulativeFlow)
    return cumulativeFlow        

def dFS1(G, s, t):
    undirected = G.to_undirected()
    explored = {s}
    stack = [(s, 0, dict(undirected[s]))]
    while stack:
        v, _, adjacent = stack[-1]
        # the node and sink is the same break
        if v==t:
            break
        while adjacent:
            u, e = adjacent.popitem()
            if u not in explored:
                break
        else:
            stack.pop()
            continue
        inDirection = G.has_edge(v, u)
        capacity = e['value']
        flow = e['flow']
        adjacent = dict(undirected[u])
        if inDirection and flow < capacity:
            # increase the flow at the edge and append to stack
            stack.append((u, capacity - flow, adjacent))
            explored.add(u)
        elif not inDirection and flow:
            # redirect the flow at the edge and append to stack
            stack.append((u, flow, adjacent))
            explored.add(u)
    # min weight of all the edges is set as flow
    flow = min((f for _, f, _ in stack[1:]), default=0)
    # augmenting path from s to t
    path = [v for v, _, _ in stack]
    return path, flow 

###################################################################################################
############################## MAIN ###############################################################
print("----------------Ford Fulkerson Algorithm----------------")
x = input("Give a input file with txt extension: ")
    # read the list of edges in networkx graph object
G = nx.read_edgelist(x, delimiter=' ', nodetype=int, encoding="utf-8", data=(('value', int),))
nx.set_edge_attributes(G, 0, 'flow')
x = list(G.nodes)
s=x[0]
x.pop(0)
t=x[42]
print(t)
flow = MaxFlow(G, s, t, None)
print(s, t, " Max Flow: ", flow)

'''
s = x[0]
t = x[2]
flow = MaxFlow(G, s, t, None)
print(s, t, " Max Flow: ", flow)
'''
'''
    # add flow attribute as 0 to the graph
    start_time = time.time()
    # initialise source(s) and sink (t)
    for i in range(len(x)):
        t=x[4]
        flow = MaxFlow(G, s, t, None)
        print(s,t," Max Flow: ",flow)
    # print execution time of the algorithm
    print("--- %s seconds ---" % (time.time() - start_time))
    '''