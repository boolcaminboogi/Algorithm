import copy

from queue import Queue
from queue import LifoQueue
from collections import defaultdict

from collections import OrderedDict
from queue import PriorityQueue

from graph import *

#1
class SSSP:
    def runDijkstra(self, graph, src):
        distances = {vertex: float('inf') for vertex in graph}
        distances[src] = 0

        priority_queue = [(0, src)]

        while priority_queue:
            current_distance, current_vertex = heapq.heappop(priority_queue)

            if current_distance > distances[current_vertex]:
                continue

            for neighbor, weight in graph[current_vertex].items():
                distance = current_distance + weight

                if distance < distances[neighbor]:
                    distances[neighbor] = distance
                    heapq.heappush(priority_queue, (distance, neighbor))

        return distances
    
    def printConfiguration(self, Known, Dv, Pv):
        print ("Configration:")
        for vtx in Known:
            print("{} -  {}  -  {}  -  {} ".format(
                vtx, Known[vtx], Dv[vtx], Pv[vtx]))

    def runDijkstra(self, G, src):
        Known = {}
        Dv = {}
        Pv = {}

        for vtx in G.getVertexList():
            Known[vtx] = False
            Dv[vtx] = float("inf")
            Pv[vtx] = None

        Known[src] = True
        Dv[src] = 0.0

        PQ = PriorityQueue()
        PQ.put((0, src))
        edgeDistance = 0.0
        newDistance = 0.0
        
        while  not PQ.empty():
            self.printConfiguration(Known, Dv, Pv)
            emin = PQ.get()[1]
            for e in G.getNeighborEdges(emin):
                edgeDistance = e.getW()
                newDistance = Dv[e.getU()] + edgeDistance
                if (not Known[e.getV()] and Dv[e.getV()] > newDistance):
                    Dv[e.getV()] = newDistance
                    Pv[e.getV()] = e.getU()
                    PQ.put((newDistance, e.getV()))

            Known[e.getU()] = True

 
#2
class ASSP:
    def floydWarshall(self,adjMatrix):
        D = copy.deepcopy(adjMatrix)
        N=len(D)
        P = [[None for x in range(N)] for y in range(N)]

        for v in range(N):
            for u in range(N):
                if v == u:
                    P[v][u] = 0
                elif D[v][u] != float('inf'):
                    P[v][u] = v
                else:
                    P[v][u] = -1

        for k in range(N):
            for v in range(N):
                for u in range(N):
                    if D[v][k] != float('inf') and D[k][u] != float('inf') \
                        and (D[v][k] + D[k][u] < D[v][u]):
                        D[v][u] = D[v][k] + D[k][u]
                        P[v][u] = P[k][u]
        return D,P
    
    def printPath(self, path, v, u):
 
        if path[v][u] == v:
            return
 
        self.printPath(path, v, path[v][u])
        print(path[v][u], '->', end=' ')
 
    def printSolution(self, path):
        N=len(path)
        for v in range(N):
            for u in range(N):
                if u != v and path[v][u] != -1:
                    print(f"The shortest path from {v} —> {u} is ({v}", '->',end=' ')
                    self.printPath(path, v, u)
                    print(f"{u})")
                    
class BGA:
    def dfs(self, adjList, start, visited = set()):
        if start not in visited :           
            visited.add(start)              
            print(start, end=' ')           
            for nxt in adjList[start] - visited:
                self.dfs(adjList, nxt, visited)

    def dfs(self, adjList, start):
        visited = set()
        print("DFS starting with vertex" , start)
        visited.add(start)  
        stack = LifoQueue()
        stack.put(start)

        while not stack.empty():                        
            vertex = stack.get()        
            print(vertex, end=' -> ')        
            nbr = adjList[vertex]   
            for node in nbr:  
                if node not in visited:    
                    visited.add(node)
                    stack.put(node)
        print()
                
    def bfs(self, adjList, start):
        seen = set()
        print("BFS starting with vertex" , start)
        seen.add(start) 
        queue = Queue()
        queue.put(start)
                 
        while not queue.empty():                        
            vertex = queue.get() 
            print(vertex, end=' -> ')       
            nbr = adjList[vertex]   
            for node in nbr:
                if node not in seen:      
                    seen.add(node)
                    queue.put(node)
        print()            
    
    def findCC(self,adjList) : 
        visited = set()
        colorList = []

        for vtx in adjList :
            if vtx not in visited :
                color = self.dfsCC(adjList, [], vtx, visited)
                colorList.append( color )
        print("Connected Components = {}".format(len(colorList)))
        print(colorList) 
        
    def dfsCC(self, adjList, color, vertex, visited):
        if vertex not in visited :
            visited.add(vertex)
            color.append(vertex)
            nbr = adjList[vertex]
            for vtx in nbr:
                if vtx not in visited:
                    self.dfsCC(adjList, color, vtx, visited)
        return color
    
    # performs Topological Sort on a given DAG
    def doTopologicalSort(self, g):
        adjList=g.getAdjList()
        visited = defaultdict()
        for vtx in adjList:
            visited[vtx]=False 
        result=[]
        for vertex in visited:
            self.dfsTS(vertex,adjList,visited,result)
 
        print(result)      

    def dfsTS(self,vertex, adjList, visited, result):
        if not visited[vertex]:
            visited[vertex] = True
            for neighbor in adjList[vertex]:
                self.dfsTS(neighbor, adjList, visited, result)
            result.insert(0,vertex)


#3
class MST:
#3-1
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
    
#3-2
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