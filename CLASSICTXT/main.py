"""
Implementation of maximum flow
hackerearth.com/practice/algorithms/graphs/maximum-flow/tutorial/:~:text=It%20is%20defined%20as%20the,Fulkerson%20algorithm%20and%20Dinic's%20Algorithm.
Ford-Fulkerson algo:
https://www.geeksforgeeks.org/ford-fulkerson-algorithm-for-maximum-flow-problem/#:~:text=Residual%20Graph%20of%20a%20flow,which%20indicates%20additional%20possible%20flow.&text=Every%20edge%20of%20a%20residual,current%20capacity%20of%20the%20edge.
Find augmenting path in residual grpah by DFS or BFS
Update the residual graph
- By taking value of minimum capacity and subtracting from edges of that path
Implementation of Ford-Fulkerson Algorithm with BFS is also called Edmonds-karp Algorithm
This uses adjacency matrix so BFS is O(V^2) and then we are iterating through
all vertices and edges so O(EV^3)
"""
from collections import defaultdict,deque

class Graph:
	def __init__(self,graph):
		"""
		Construct directed graph from adjacency matrix.
		"""
		self.graph=graph

	def bfs(self,s,t,P):
		vis=set([s])
		dq=deque([s])
		while dq:
			node = dq.popleft()
			for neighbor,cap in enumerate(self.graph[node]):
				if neighbor not in vis and cap>0:
					dq.append(neighbor)
					vis.add(neighbor)
					P[neighbor]=node
		return True if t in vis else False


	def FFA(self,s,t):
		"""
		This is the ford fulkerson algorithm that takes a graph as input in form of adjacency list and takes a
		source and sink node.
		"""
		P=[-1]*len(self.graph)
		max_flow=0
		inf=float('inf')

		while self.bfs(s,t,P):
			path_flow=inf
			node=t
			while node!=s:
				parent=P[node]
				path_flow=min(path_flow,self.graph[parent][node])
				node=parent
			max_flow+=path_flow
			# Update the capacities for the edges.
			node=t
			while node!=s:
				parent=P[node]
				self.graph[parent][node]-=path_flow
				self.graph[node][parent]+=path_flow
				node=parent

		return max_flow
"""
Implementation of Dinic's Algorithm
Dinic's algo is faster:
level graphs
residual graphs
augmenting paths
blocking flow
"""

"""
Constructing my inputs for the problem
Inputs are space separated n, source node, and sink node
Then it contains all the edges on the following n lines with
space separated strings for input node, output node, and the minimum capacity
"""
with open("ffa_outputs.txt","w") as fo:
	with open("input_random_01_10.txt","r") as fi:
		n,source,sink=fi.readline().split()
		n=int(n)
		D=defaultdict(list)
		index_map=defaultdict(int)
		vis=set()
		i=0
		for _ in range(n):
			u,v,cap=fi.readline().split()
			cap=int(cap)
			if u not in vis:
				index_map[u]=i
				i+=1
				vis.add(u)
			if v not in vis:
				index_map[v]=i
				i+=1
				vis.add(v)
			D[index_map[u]].append((index_map[v],cap))
		m=len(D.keys())
		M=[[0]*(m+1) for _ in range(m+1)]
		for i in range(m):
			for v,cap in D[i]:
				M[i][v]=cap
		graph=Graph(M)
		fo.write(f"Max flow = {graph.FFA(0,m)}")