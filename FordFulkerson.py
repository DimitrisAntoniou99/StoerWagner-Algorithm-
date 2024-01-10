
###################################################################################################
#Implementation of the Global Ford-Fulkerson in Python 
# Dimitris Antoniou AM:4027
'''
The Ford–Fulkerson method or Ford–Fulkerson algorithm (FFA) is a greedy algorithm that computes the maximum flow in a flow network.
It is sometimes called a "method" instead of an "algorithm" as the approach to finding augmenting paths in a residual graph is not fully specified[1]
or it is specified in several implementations with different running times.
'''

'''https://www.geeksforgeeks.org/ford-fulkerson-algorithm-for-maximum-flow-problem/'''
import sys
import networkx as nx 
import platform
import snap
import numpy as np
from matplotlib import pyplot as plt 
from time import time as t 

__author__="Dimitris Antoniou"
__email__="dimanton1999@gmail.com"
__version__="Final Version,10.0"
__url__="https://www.cs.uoi.gr/~cse74027/?fbclid=IwAR1ASfRHaXnjs4uoM43dSCfMz3dmlHBKyo8PzSk1R4olpmzH_CZy_UcZgnk"

#------------------Global Variables-------------------------
global FLowLst
global listA
global listB
global id
FLowLst = list()
listA = list()
listB = list()
id=0
#------------------Class Graph-------------------------
class UndirectedGraph:
    def __init__(self, entry):
        self.entry = str(entry)
        self.vertex = None
        with open(str(self.entry)) as file:
            num=0
            self.load = [[int(num) for num in line.split()] for line in file]
            self.column,self.row,self.vertex = self.load[0][0],self.load[0][0],self.load[0][0]
            self.edges = self.load[0][1]
            self.graph = [[0 for x in range(self.vertex)] for y in range(self.vertex)]
            # Edges values
            for line in self.load[1:]:
                self.graph[line[0]][line[1]] = int(line[2])
                self.graph[line[1]][line[0]] = int(line[2])
            self.source = 0
            self.sink = [i for i in range(1, self.vertex)]
            self.graph_ = [i[:] for i in self.graph]
            self.base = [i[:] for i in self.graph]
    def resetGraph(self):
        self.graph = [i[:] for i in self.base]
#------------------Class BFS-------------------------
''''''
class BFS:
    def bfs(self, graph, s, t, parent):
        visited = [False] * len(graph)
        queue = []
        queue.append(s)
        visited[s] = True
        while queue:
            u = queue.pop(0)
            for ind, val in enumerate(graph[u]):
                if val > 0 and visited[ind] == False:
                    queue.append(ind)
                    visited[ind] = True
                    parent[ind] = u
        if visited[t]:
            return True
        return  False

#------------------corteSt Function -------------------------

def MaxFLowLST(results):
    global  id
    value = float('inf')
    for i, maxFlow in enumerate(results):
        if maxFlow[2] < value:
            value = maxFlow[2]
            id = i
    return results[id]
#------------------ Set Function -------------------------

def Set(Flow, graph):
    VertexLst = list()
    for i in range(graph.row):
        value = 0
        for j in range(graph.column):
            value = value+graph.graph_[i][j]
        if value == Flow[2]:
            VertexLst.append(i)
    return VertexLst
#------------------Ford Fulkerson Function -------------------------
def FordFulkerson(graph, s, terminal, search):
    parent = [-1] * graph.row
    maxFlow = 0
    list1=list()
    list2=list()
    while search.bfs(graph.graph, s, terminal, parent):
        t = terminal
        path = float('inf')
        while t != s:
            t_ = parent[t]
            path = min(path, graph.graph[t_][t])
            t = parent[t]
        maxFlow += path
        v = terminal
        while (v != s):
            u = parent[v]
            graph.graph[u][v] -= path
            graph.graph[v][u] += path
            v = parent[v]
    for i in range(graph.row):
        for j in range(graph.column):
            if graph.graph_[i][j] > 0 and graph.graph[i][j] == 0:
                list1.append(i)
                list2.append(j)
    return list1, list2, maxFlow



#-------------main------------------------------------------------------
if __name__ == '__main__':
    print("------------------Ford-Fulkerson Algorithm-------------------")
    x=input("Give As Input Text File:")
    g=UndirectedGraph(x)
    start=t()
    FlowLst=[]
    for sink in g.sink:
        maxFlow = FordFulkerson(g,g.source,sink,BFS())
        FlowLst.append(maxFlow)
        g.resetGraph()
        Flow = MaxFLowLST(FlowLst)
        vs = Set(Flow,g)
        if len(vs) == g.vertex:
            k=dict(Flow[1])
            vs = set(k)
        Ford = Flow[2]
    print("Τhe number of Vertices is",sink+1, "and edges of the graph is",(g.edges))
    print("The Global Max Flow of the Graph is:",Ford)
    elapsed = t() - start
    print('Runtime:',(elapsed),"Second")
    print('Runtime:',(elapsed) * 1000000000, "ns")
    G = nx.read_edgelist(x, delimiter=' ', nodetype=int, encoding="utf-8", data=(('value', int),))
    sp = nx.spring_layout(G)
    plt.axis('off')
    nx.draw_networkx(G, pos=sp, with_labels=False, node_size=10)
    plt.show()

###################################################################################################
############################## FILES ##############################################################
############ The following file show us the hardware of the system when we run our program ########################
    my_system = platform.uname()
    f=open("DATA!/resultsFlow.txt", "w")
    f.write("------------------------------Section System-Information-----------------------------\n\n\n")
    f.write(f"System: {my_system.system}\n")
    f.write(f"Node Name: {my_system.node}\n")
    f.write(f"Release: {my_system.release}\n")
    f.write(f"Version: {my_system.version}\n")
    f.write(f"Machine: {my_system.machine}\n")
    f.write(f"Processor: {my_system.processor}\n\n")
    f.write("------------------------------Section Results----------------------------------------\n\n\n")
    #f.write(f"Number of Vertex of the is: {x},and the weights of each edges is: {edges}\n\n")
    f.write(f"The Global Max Flow  of  the Graph is : {Ford}\n")
    f.close()

