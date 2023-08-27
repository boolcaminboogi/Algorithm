
from collections import OrderedDict
from queue import PriorityQueue

class Graph:

    def __init__(self, directed=False,gdict=None):
        if gdict is None:
            gdict = {}
        self.gdict = gdict
        self.directed=directed
        self.keyIndex = {}
    
    def __repr__(self):
        gs=""
        for vtx in self.gdict:
            gs+= "{} : {} \n".format(vtx,self.gdict[vtx])
        return gs

    def __str__(self):
        gs=""
        for vtx in self.gdict:
            gs+= "{} : {} \n".format(vtx,self.gdict[vtx])
        return gs 
           
    def getOrder(self):
        return len(self.gdict.keys())
    
    def isDirected(self):
        return self.directed
         
    def addVertex(self, vtx):
        if vtx in self.gdict.keys():
            print("Node is already in the graph")
        else:
            self.gdict
            self.gdict[vtx]=[];
            self.keyIndex[vtx]=len(self.keyIndex)+1
    
 
    def addEdge(self, e):
        if e.getU() in self.gdict:
            self.gdict[e.getU()].append(e)
            
        if(not self.directed):
            e2=Edge(e.getV(),e.getU(), e.getW())
            self.gdict[e2.getU()].append(e2)

        else:
            print(" Vertex not found")    

    def getAdjList(self):
            adjList = {}
            for vtx in self.gdict:
                adjList[vtx]=set(self.getNeighborVertices(vtx))
            return adjList

    def getNeighborVertices(self,vtx):
        elist=self.gdict.get(vtx)
        vlist=[]
        for e in elist:
            vlist.append(e.getV())
        return vlist 
    
    def getNeighborEdges(self,vtx):
        return self.gdict[vtx]
    
    
    def printAdjList(self):
        print("\n Adjacency List:")
        adjList=self.getAdjList()
        for vtx in adjList:
            print("{} : {}".format(vtx,adjList[vtx]))
        
    def getVertexList(self):
        dict1 = OrderedDict(sorted(self.keyIndex.items()))
        return list(dict1.keys()) 
    
    def getDegree(self, vtx):
        return self.getOutDegree(vtx) + self.getInDegree(vtx)
    
    def printDegree(self):
        for vtx in self.gdict:
            print("Degree of vertex {} = {} ".format(vtx,self.getDegree(vtx)))
    
    def getOutDegree(self, vtx):
        return len(self.gdict[vtx])
    
    def printOutDegree(self):
        for vtx in self.gdict:
            print("Out degree of vertex {} = {} ".format(vtx,self.getOutDegree(vtx)))

    def printInDegree(self):
        for vtx in self.gdict:
            print("In degree of vertex {} = {} ".format(vtx,self.getInDegree(vtx)))
    def getInDegree(self, vtx):
        return len(self.getInwardEdges(vtx))
                   
    def getInwardEdges(self, vtx):
        elist=[]
        for e in self.getEdgeList():
            if vtx==e.getV():
               elist.append(e)
        return elist
    
    
    def getEdgeList(self):
        eList=[]
        for vtx in self.gdict:
            for e in self.gdict[vtx]:
                eList.append(e)
            
        return eList
    
    def getSize(self):
        size=len(self.getEdgeList())
        if not self.isDirected():
            size//=2
        return size
    
    def getAdjMatrix(self):
        size=len(self.keyIndex)
        adjMatix= [[0.0 if i==j else float('inf') for j in range(size)] for i in range(size)]
        for e in self.getEdgeList():
            adjMatix[self.keyIndex[e.getU()]-1][self.keyIndex[e.getV()]-1]=e.getW()
        return adjMatix
    
    def printAdjMatrix(self):
        print("\n Adjacency Matrix:") 
        adjMatix= self.getAdjMatrix()
        for i in range(0, len(self.keyIndex)): 
            print() 
            for j in range(0, len(self.keyIndex)): 
                print(" {:.2f} ".format(float(adjMatix[i][j])), end ="")     
        print()
        
    def getWeight(self):
        w=0
        for e in self.getEdgeList():
            w += e.getW()
        
        if not self.isDirected():
            w=w//2;
        
        return w

class Edge:
    def __init__(self,  u=None, v=None, w=None,):
        self.u = u
        self.v = v
        self.w = w
    
    def __eq__(self, rhs):      return self.w == rhs.w
    def __ne__(self, rhs):      return self.w != rhs.w
    def __lt__(self, rhs):      return self.w <  rhs.w
    def __le__(self, rhs):      return self.w <= rhs.w
    def __gt__(self, rhs):      return self.w >  rhs.w
    def __ge__(self, rhs):      return self.w >= rhs.w
    def __hash__(self):         return hash(self.w)
    def __repr__(self):  return str(self.u) + '->' + str(self.v) + " (" + str(self.w) + ")"  
    def __str__(self):  return str(self.u) + '->' + str(self.v) + " (" + str(self.w) + ")"  
    
    
    def setU(self, u):   self.u = u
    def setV(self, v):   self.v = v
    def setW(self, w):   self.w = w

    def getU(self):      return self.u
    def getV(self):      return self.v
    def getW(self):      return self.w

class Vertex:
    def __init__(self, key=None):
        self.key=key
    
    def __repr__(self):         return str(self.key)
    def __str__(self):          return str(self.key)
    
    
    def setData(self, key):    self.key = key
    def getData(self):          return self.key
    
    def __hash__(self):         return hash(self.key)    
    def __eq__(self, rhs):      return self.key == rhs.key
    def __ne__(self, rhs):      return self.key != rhs.key
    def __lt__(self, rhs):      return self.key <  rhs.key
    def __le__(self, rhs):      return self.key <= rhs.key
    def __gt__(self, rhs):      return self.key >  rhs.key
    def __ge__(self, rhs):      return self.key >= rhs.key
    
    
    