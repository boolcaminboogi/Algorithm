from graph import *
from queue import PriorityQueue


class MST:
    def mstKruskal(self, G):
        T = Graph(G.isDirected())
        for vtx in G.getVertexList():
            T.addVertex(vtx)
        ds = DisjointSet()
        for vtx in G.getVertexList():
            ds.makeSet(vtx)

        PQ = PriorityQueue()
        for e in G.getEdgeList():
            PQ.put(e)

        while not PQ.empty():
            e = PQ.get()
            x = ds.find(e.getU())
            y = ds.find(e.getV())
            if (x != y):
                T.addEdge(e)
                ds.union(x, y)
        return T
    
    def runPrim(self, G, src):
        T = Graph(G.isDirected())
        eList=[]

        PQ = PriorityQueue()
        for e in G.getNeighborEdges(src):
            PQ.put(e)
        T.addVertex(src)

        while  T.getOrder() != G.getOrder():    
            minE = PQ.get()
            
            vxtV=minE.getV()
            
            if vxtV in T.getVertexList():
                continue
            T.addVertex(vxtV)
            eList.append(minE)
            for e in G.getNeighborEdges(vxtV):
                PQ.put(e)
        
        for e in eList:
            T.addEdge(e)            

        return T


class DisjointSet:
	def __init__(self):
		self.parent = dict()
		self.rank = dict()
	
	def makeSet(self, vtx):
		self.parent[vtx] = vtx
		self.rank[vtx] = 0
     
	def find(self, vtx):
		if self.parent[vtx] != vtx:
			self.parent[vtx] = self.find(self.parent[vtx])
		return self.parent[vtx]

	def union(self, vtx1, vtx2):
		root1 = self.find(vtx1)
		root2 = self.find(vtx2)
		if root1 != root2:
			if self.rank[root1] > self.rank[root2]:
				self.parent[root2] = root1
			else:
				self.parent[root1] = root2
				if self.rank[root1] == self.rank[root2]: self.rank[root2] += 1