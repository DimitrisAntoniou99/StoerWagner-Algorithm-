from DIAOFRA.CreateGraph import CreateGraph
import numpy as np
import copy
import networkx as nx
from matplotlib import pyplot as plt
from time import time as t
import os
global counter
counter=0

def MinCutPhase(Graph,Vertex):
    A = [Vertex]
    #modify
    Vlist = copy.deepcopy(Graph.V)
    Vlist.remove(Vertex)
    #######
    
    #modify2
    weightlist = {}
    for v in Vlist:
        weightlist[v] = Graph.graph[v,Vertex]
    while len(A) != len(Graph.V):
        maxw_k = 0
        maxw = 0
        for k,v in weightlist.items():
            if v>maxw:
                maxw = v
                maxw_k = k
        del weightlist[maxw_k]
        for k,v in weightlist.items():
            v += Graph.graph[k,maxw_k]
            weightlist[k] = v
        A.append(maxw_k)
        Vlist.remove(maxw_k)
    cut_of_phase = np.sum(Graph.graph[A[-1],:])

    #merging the last two vertexes added
    for v,w in enumerate(Graph.graph[A[-1],:]):
        if w != 0 and v != A[-2]:
            Graph.graph[A[-2],v] += w
            Graph.graph[v,A[-2]] += w
        Graph.graph[A[-1],v] = 0
        Graph.graph[v,A[-1]] = 0
    Graph.V.remove(A[-1])
    return cut_of_phase,A

def MinCut(Graph,Vertex):
    minimum = 1e10
    while (len(Graph.V)) > 1:
        cut_of_phase = MinCutPhase(Graph,Vertex)
        if cut_of_phase[0] < minimum:
            minimum = cut_of_phase[0]
    return minimum
#------------plotting--------------
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

if __name__ == "__main__":
    print("An Implementation of the Stoer-Wagner Algorithm.")
    print("Dimitrios Antoniou, August 2022.")
    cases={'Manually':'m','Read file':'r','Plot Graph':'p'}
    print 
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
        G = CreateGraph(x) #### orizo korifes tou grafimatos kai tis apothikeuo sto parakato lexiko 
             #### orizo tis akmes tou grafimatos  metaksi ton korifon 
        w=G.addedge(edges)
        for i in range(x):
            counter+=1 ############## metritis ton korifon
            while len(edges)<y:
                key=input("Enter a edge: ")
                value=input("Enter a value of edge: ") 
                edges[key]=value
               # plotG.addedge(int(key[0]),int(key[2]),weight=value)
                w=G.addedge(edges)
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
         print(y)
         file.close()
          #paidi mou giati ftiaxneis ta txt etsi. ntrph
         x=1
         for i in range(y): 
            v=findv[i].split(' ')
            #findv[i]=findv[i].replace(" \n","\n")
            temp=max(int(v[0]),int(v[1]))
            print(temp)
            if x<=temp:
                x=temp
         G=CreateGraph(x)
         w=G.addedge(edges)
         a=0
         for i in range(y):
            contents=findv[i].split(' ')
            #findv[i]=findv[i].replace(" \n","\n")
            key=contents[0]+'-'+contents[1]
            if i<y:
                value=contents[2][:-1]
            else:
                value=contents[2] 
            edges[key]=value
            s=edges
            #plotG.addedge(int(contents[0]),int(contents[1]),weight=value)
            w=G.addedge(edges)
            print(w)
            a+=i
            with open(graphfile,'r') as file:
                line=file.readline()
                a=0

         print(x)
    start=t()
    w=G.addedge(edges)
    print("The Final Min Cut of the Graph is :",MinCut(G,w,a))
    elapsed=t()-start
    print('Runtime(sec): '+str(elapsed))   
    if plotting==cases['Plot Graph']:
            plot_graph(plotG)
    
