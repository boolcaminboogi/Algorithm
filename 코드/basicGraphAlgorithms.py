from graph import *
from queue import Queue
from queue import LifoQueue
from collections import defaultdict

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
           