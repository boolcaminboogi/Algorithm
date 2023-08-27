import graph
from queue import PriorityQueue


class SSSP:    
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

 