#Imlementation of the Edge-Connectivity with NetworkX
#Dimitris Antoniou AM:4027
'''
In graph theory, a connected graph is k-edge-connected if it remains connected whenever fewer than k edges are removed.
The edge-connectivity of a graph is the largest k for which the graph is k-edge-connected.
'''
import networkx as nx
from time import  time as t
from matplotlib import pyplot as plt
from networkx.algorithms.connectivity import edge_connectivity
print("------------------Edge Connectivity-------------------")
print("Note. The contents of the file should be given as: vertex vertex weight.")
x=input("Give As Input Text File :")
start=t()
G = nx.read_edgelist(x, delimiter=' ', nodetype=int,encoding="utf-8",data=(('value', int),))
sp=nx.spring_layout(G)
plt.axis('off')
nx.draw_networkx(G,pos=sp,with_labels=False,node_size=35)
value= nx.edge_connectivity(G)
elapsed=t()-start
print('Runtime: ',(elapsed),"Second")
print("The Edge Connectivity of the graph is :",value)
plt.show()

