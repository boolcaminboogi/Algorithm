import copy
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
