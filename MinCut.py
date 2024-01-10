
###################################################################################################
#Implementation of the Stoer Wagner Min-Cut in Python 
# Dimitris Antoniou AM:4027

'''
In graph theory, the Stoer–Wagner algorithm is a recursive algorithm to solve the minimum cut problem in undirected weighted graphs with non-negative weights.
It was proposed by Mechthild Stoer and Frank Wagner in 1995. The essential idea of this algorithm is to shrink the graph by merging the most intensive vertices,
until the graph only contains two combined vertex sets.[2]
At each phase, the algorithm finds the minimum s-t cut for two vertices s and t chosen at its will.
 Then the algorithm shrinks the edge between
 s and t to search for non s-t cuts. The minimum cut found in all phases will be the minimum weighted cut of the graph.
'''
###################################################################################################
import copy
from StructGraph import UndirectedGraph
import math
import numpy as np
import random 
import sys 
import snap
import platform 
import networkx as nx
from matplotlib import pyplot as plt
from time import time as t
import os

__author__="Dimitris Antoniou"
__email__="dimanton1999@gmail.com"
__version__="Final Version,10.0"
__url__="https://www.cs.uoi.gr/~cse74027/?fbclid=IwAR1ASfRHaXnjs4uoM43dSCfMz3dmlHBKyo8PzSk1R4olpmzH_CZy_UcZgnk"
###################################################################################################
#global variables
global edges
global z
global counter
global b
global a
a=0
counter=0
edges={}
b=0

print("------------------Stoer-Wagner Algorithm-------------------")
print("A simple Min-Cut Algorithm \n")

# Implement the MinimumCutPhase function
def MinimumCutPhase(G, w, a):
    A = [a]
    B = copy.deepcopy(G.Vertex)
    B.remove(a)
    while len(A) != len(G.Vertex):
        y = 0
        x = 0
        for i in B:
            c = 0
            for v in A:
                b = G.G[v][i]
                c += b
            if c > x:
                x = c
                y = i
            elif x > c:
                continue
            else:
                if i < y:
                    y = i
        A.append(y)
        B.remove(y)
    o = G.G[A[-1]][:]
    cut_of_phase = sum(o)
    for v, weights in enumerate(G.G[A[-1]]):
        if weights != 0 and v != A[-2]:
            G.G[A[-2]][v] += weights
            G.G[v][A[-2]] += weights
        G.G[A[-1]][v] = 0
        G.G[v][A[-1]] = 0
    G.Vertex.remove(A[-1])
    return cut_of_phase

# Implement the MinimumCut function
def MinimumCut(G, w):
    min_cut = float('inf')
    while len(G.Vertex) > 1:
        z = MinimumCutPhase(G, w, next(iter(G.Vertex)))
        if z < min_cut:
            min_cut = z
    return min_cut

#------------Plot Function----------------------------------------------
def plot_graph(plotG):
    gplot=nx.circular_layout(plotG, scale=6)
    nx.draw_networkx_nodes(plotG,gplot)
    edge_labels=dict([((u,v,),d['weight'])
             for u,v,d in plotG.edges(data=True)])
    nx.draw_networkx_labels(plotG,gplot,font_size=15,font_family='sans-serif')
    nx.draw_networkx_edges(plotG,gplot)
    plt.axis('off')
    nx.draw_networkx_edge_labels(plotG,gplot,edge_labels=edge_labels)
    nx.draw(plotG,gplot,edge_cmap=plt.cm.Reds) 
    plt.show()

#-------------main------------------------------------------------------
if __name__ == "__main__":
    print("Dimitrios Antoniou, February 2023.")
    cases={'Manually':'m','Read file':'r','Plot Graph':'p'}
    entering=str(input("Press m to enter the graph manually, r to read a file. "))
    print("Note. The contents of the file should be given as: vertex vertex weight.")
    while entering not in set(cases.values()):
            entering=str(input("Press m to enter the graph manually, r to read a file."))
    plotting=str(input("Enter p to plot (Not recommended for large graphs), anything else to skip. "))
    edges={}
    plotG=nx.Graph()
    if entering==cases['Manually']:
        x=int(input("Give the number of Vertices: "))
        y=int(input("Give the number of edges: "))
        G = UndirectedGraph(x)
        w=G.add_edge(edges)
        for i in range(x):
            counter+=1
            while len(edges)<y:
                key=input("Enter a edge: ")
                value=input("Enter a value of edge: ") 
                edges[key]=value
                plotG.add_edge(int(key[0]),int(key[2]),weight=value)
                w=G.add_edge(edges)
                a=i
        print("Number of Vertex of the graph is",counter,"and the weights of each edges is: ",edges)
    else:
          edges={}
          graphfile=str(input("Filename: "))
          while graphfile not in os.listdir():
              graphfile=str(input("Not found in current directory. New Filename: "))
          file=open(graphfile,'r')
          findv=file.readlines()
          y=len(findv)
          file.close()
          x=0
          for i in range(y): 
              v=findv[i].split(' ')
              temp=max(int(v[0]),int(v[1]))
              if x<temp:
                  x=temp
          G = UndirectedGraph(x)
          w=G.add_edge(edges)
          a=0
          for i in range(y):
              contents=findv[i].split(' ')
              key=contents[0]+'-'+contents[1]
              if i<y-1:
                  value=contents[2][:-1]
              else:
                 value=contents[2] 
              edges[key]=value
              plotG.add_edge(int(contents[0]),int(contents[1]),weight=value)
              w=G.add_edge(edges)

    start=t()
    w=G.add_edge(edges)
    print("Τhe number of Vertices is",x+1, "and edges of the graph is",y)
    print("The Final Min Cut of the Graph is :",MinimumCut(G,w))
    elapsed=t()-start
    print('Runtime: ',(elapsed),"sec")
    print('Runtime: ',(elapsed)*1000000000, "ns")
    if plotting==cases['Plot Graph']:
            plot_graph(plotG)
###################################################################################################
############################## FILES ##############################################################
############ The following file show us the hardware of the system when we run our program ########################
    my_system = platform.uname()
    f=open("DATA!/resultsMinCut.txt", "w")
    f.write("------------------------------Section System-Information-----------------------------\n\n\n")
    f.write(f"System: {my_system.system}\n")
    f.write(f"Node Name: {my_system.node}\n")
    f.write(f"Release: {my_system.release}\n")
    f.write(f"Version: {my_system.version}\n")
    f.write(f"Machine: {my_system.machine}\n")
    f.write(f"Processor: {my_system.processor}\n\n")
    f.write("------------------------------Section Results----------------------------------------\n\n\n")
    f.write(f"Number of Vertices of the is: {x},and the weights of each edges is: {edges}\n\n")
    f.write(f"The Final Min Cut of  the Graph is : {MinimumCut(G,w)}\n")
    f.close()
