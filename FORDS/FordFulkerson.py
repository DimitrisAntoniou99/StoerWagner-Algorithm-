import networkx as nx
import networkx as nx
from networkx.algorithms.flow import edmonds_karp,maximum_flow_value
g=nx.Graph()
g=nx.read_weighted_edgelist("../input48_1128.txt", comments='#', delimiter=None, create_using=nx.Graph(), nodetype=int, encoding='utf-8')
f=g.number_of_nodes()
l=g.number_of_edges()
x=list(g.nodes)
y=x[0]
x.pop(0)
#print(x1)
#print(x2)
#R = edmonds_karp(g, s=x1, t=x2)

for i in range(len(x)):
    k=x[i]
    #print(k)
    value=nx.maximum_flow(g,'0','39',capacity=None)
    print(value)

#inf_capacity_flows = R.graph['inf_capacity_flows']
#flow_value, flow_dict == nx.maximum_flow_value(G, '1', '8',flow_func=maximum_flow_value)
