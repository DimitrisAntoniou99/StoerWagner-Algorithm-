#Imlementation of the Stoer-Wagner with NetworkX
#Dimitris Antoniou AM:4027

import networkx as nx
from time import time as t
from matplotlib import pyplot as plt
print("------------------Stoer-Wagner with NetworkX-------------------")
print("Note. The contents of the file should be given as: vertex vertex weight.")
l=input("Give As Input Text File :")
g=nx.read_weighted_edgelist(l,comments='#',delimiter=None,create_using=nx.Graph(),nodetype=None,encoding='utf-8')
start=t()
elapsed=t()-start
sp=nx.circular_layout(g,scale=6)
plt.axis('off')
nx.draw_networkx(g,pos=sp,with_labels=False,node_size=35)
g.number_of_nodes()
cut_value,partition= nx.stoer_wagner(g)
elapsed=t()-start
print("The Min Cut of the graph is :",cut_value)
print('Runtime: ',(elapsed),"Second")
plt.show()
