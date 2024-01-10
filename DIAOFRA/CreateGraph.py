import numpy as np

class CreateGraph(object):
    def __init__(self,V):
        self.V = [v for v in np.arange(V)]
        self.graph = np.zeros((V,V)).astype(np.int64)

    def addedge(self,edges):
        for edge,weight in edges.items():
            v1 = int(edge.split('-')[0]) - 1
            v2 = int(edge.split('-')[1]) - 1
            self.graph[v1,v2] = weight
            self.graph[v2,v1] = weight
            #self.graph

if __name__ == "__main__":
    graph = CreateGraph(8)
    edges = {"1-2":15,"1-3":10,"2-3":3,"2-4":6,"3-5":12,"4-6":4,"5-7":6,"4-7":6,"5-6":3,"6-7":1,"6-8":10,"7-8":5}
    graph.addedge(edges)
    print(graph.graph,graph.V,graph.graph.dtype)
