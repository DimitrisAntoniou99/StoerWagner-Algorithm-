import math
import numpy as np
import random 
import sys 
import snap
global counter
counter=0
class UndirectedGraph(object):
    def __init__(self,Vertex):
        self.Vertex = Vertex
        self.Vertex = [v for v in range(Vertex)]
        self.G=np.zeros((Vertex,Vertex)).astype(int)
        #self.G=int(np.zeros((Vertex,Vertex)))
    
    def add_vertex(self,Vertex):
        self.Vertex.append(Vertex)
        self.edges[(Vertex,Vertex)] = 0    
    
    def add_edge(self,edges): #orizo tin akmi 
        self.edges=edges
        for edge,weight in edges.items():
            u = int(edge.split('-')[0]) - 1
            v = int(edge.split('-')[1]) - 1
            self.G[(u,v)] = weight
            self.G[(v,u)] = weight
   
    def setData(self,Vertex) :
        self.Vertex = Vertex
        if (self.Vertex <= 0) :
            print("\nEmpty Graph")
        else :
            index=0
            while (index < self.Vertex) :
                #  Set initial node value
                self.node[index]=Vertex(index)
                index =index+1

if __name__ == "__main__":
    x=int(input("Give the number of Vertices: "))
    y=int(input("Give the number of edges: "))
    G = UndirectedGraph(x)
    edges={}
    w=G.add_edge(edges)
    for i in range(x):
        while len(edges)<y:
            key=input("Enter a edge: ")
            value=input("Enter a value of edge: ")
            edges[key]=value
            counter+=1 ############## metritis ton korifon
            G = UndirectedGraph(x)
            #edges = {'1-2':2,'1-5':3,'2-5':2,'5-6':3,'2-6':2,'2-3':3,'6-7':1,'3-7':2,'3-4':4,'4-7':2,'7-8':3,'4-8':2}
            w=G.add_edge(edges)
            a=i
