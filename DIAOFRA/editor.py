import networkx as nx
import matplotlib.pyplot as plt
import time
import sys
from memory_profiler import profile

# To compute number of sugmenting paths needed for computing max flow
numberOfPaths = 0

"""
Instructions to execute the code
run as : python3 filename.py <choice> <source> <sink>
example: python3 FordFulkerson.py 1 0 8
arguments are:
argv[0] - filename
argv[1] - choice : can be 1 (neural dataset) or 2 (US airports dataset) (strictly integer)
argv[2] - source node (strictly integer)
argv[3] - sink node (strictly integer)
"""

"""
The variables used throughout the code are:
    G : It is the networkX graph object
    s : It is the source of the graph
    t : It is the sink of the graph
    p : Augmenting path
    step: This defines if the code should print intermediate increases in 
          flow for each augmenting path
This function performs the following steps:
    1)  Looks for an augmenting path(DFS)
    2)  If present adds the flow to the cumulative flow
    3)  Then increases the flow along the augmenting path
    4)  If step function is provided then it calls the intermediate print function
"""
#@profile   #Used for memory profiling
def fordFulkerson(G, s, t, step=None):
    #initialise cumulative flow and path
    cumulativeFlow, p = 0, True
    
    #Till there is an augmenting path keep looking for increase in flow
    while p:
        # Using depth first search, look for a path
        # Add the flow returned by that path to the cumulative flow
        p, flow = depthFirstSearch(G, s, t)
        cumulativeFlow += flow

        # To compute number of sugmenting paths needed for computing max flow
        global numberOfPaths
        numberOfPaths += 1

        # Increase the flow along the augmenting path
        # x and y is the edge in that path
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

"""
This function performs the following steps:
    1)  Creates a set of explored nodes to keep track for DFS
    2)  keep searching the neighbours
    3)  Then increase or redirect the flow along the path
    4)  Select min weight from the edges
    5)  Return min weight as flow and path from s to t
"""
def depthFirstSearch(G, s, t):
    undirected = G.to_undirected()
    #maintain a set of explored nodes
    explored = {s}
    #maintain a stack of the nodes for the source
    stack = [(s, 0, dict(undirected[s]))]
    
    while stack:
        v, _, adjacent = stack[-1]
        # the node and sink is the same break
        if v == t:
            break
        
        # search the next neighbour
        while adjacent:
            u, e = adjacent.popitem()
            # if the edge is not explored then stop
            if u not in explored:
                break
        else:
            stack.pop()
            continue
        
        # current flow and capacity
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

def stepFlow(G, path, flow, cumulativeFlow):
    print('Flow increased by', flow, 
          'at path', path,
          '; current flow', cumulativeFlow)
    #Uncomment this if you want to visualize graph after every increment in the flow
    #visualizeGraph(G)

########################################################################
#This part of code is same as above just applied for the airport dataset
########################################################################

#@profile   #Used for memory profiling
def fordFulkersonAirport(G, s, t, step=None):
    #initialise cumulative flow and path
    cumulativeFlow, p = 0, True
    
    #Till there is an augmenting path keep looking for increase in flow
    while p:
        # Using depth first search, look for a path
        # Add the flow returned by that path to the cumulative flow
        p, flow = depthFirstSearchAirport(G, s, t)
        cumulativeFlow += flow
        global numberOfPaths
        numberOfPaths += 1

        # Increase the flow along the augmenting path
        # This is same as the residual graph
        # x and y is the edge in that path
        for y, x in zip(p, p[1:]):
            if G.has_edge(y, x):
                #increase flow if edge is present
                G[y][x]['flow'] += flow
            else:
                #reverse the flow if edge is not present
                G[x][y]['flow'] -= flow
        
        # Print the intermediate augmenting flow results
        if callable(step):
            step(G, p, flow, cumulativeFlow)
    return cumulativeFlow        

"""
This function performs the following steps:
    1)  Creates a set of explored nodes to keep track for DFS
    2)  keep searching the neighbours
    3)  Then increase or redirect the flow along the path
    4)  Select min weight from the edges
    5)  Return min weight as flow and path from s to t
"""
def depthFirstSearchAirport(G, s, t):
    undirected = G.to_undirected()
    explored = {s}
    stack = [(s, 0, dict(undirected[s]))]
    
    while stack:
        v, _, adjacent = stack[-1]
        # the node and sink is the same break
        if v == t:
            break
        
        # search the next neighbour
        while adjacent:
            u, e = adjacent.popitem()
            # if the edge is not explored then stop
            if u not in explored:
                break
        else:
            stack.pop()
            continue
        
        # current flow and capacity
        inDirection = G.has_edge(v, u)
        capacity = e['value']
        flow = e['flow']
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


# Driver code for the program
if __name__ == '__main__':

    """
    To choose dataset:
        1: is to choose elegans neural network dataset
        2: is to choose US airport dataset
    """
    choice = sys.argv[1]
    if choice=="1":
        
        print("Min-Cut Max-Flow dataset")
        # read the list of edges in networkx graph object
        G = nx.read_edgelist('ford.txt', delimiter=' ', nodetype=int,encoding="utf-8",data=(('value', int),))
        # add flow attribute as 0 to the graph
        nx.set_edge_attributes(G, 0, 'flow')

        # Uncomment this to visualize initial graph
        # visualizeGraph(G)

        # Start the execution time to check performance
        start_time = time.time()

        # initialise source(s) and sink (t)
        s = int(sys.argv[2])
        t = int(sys.argv[3])
        flow = fordFulkersonAirport(G, s, t, stepFlow)
        print("Flow: ", flow)
        print("Number of augmenting paths: ", numberOfPaths - 1)
        # print execution time of the algorithm
        print("--- %s seconds ---" % (time.time() - start_time))
    else:
        print("Error")