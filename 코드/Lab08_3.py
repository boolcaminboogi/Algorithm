

parent = dict()
rank = dict()

graph={
    'vertices':['A','B','C','D','E','F','G','H','I'],
    'edges':[(31,'A','B'),(29,'A','D'),(31,'B','A'),(9,'B','C'),(18,'B','E'),
             (9,'C','B'),(1,'C','F'),(29,'D','A'),(44,'D','E'),
             (18,'E','B'),(44,'E','D'),(14,'E','F'),(1,'F','C'),
             (14,'F','E'),(33,'G','D'),(48,'G','H'),(48,'G','H'),
             (48,'G','H'),(48,'G','H'),(48,'G','H'),(48,'H','G'),
             (3,'H','E'),(20,'H','I'),(20,'I','H'),(24,'I','F'),
]}
def make_set(vertice):
    parent[vertice]=vertice
    rank[vertice]=0
    
def find(vertice):
    if parent[vertice]!=vertice:
        parent[vertice]=find(parent[vertice])
    return parent[vertice]

def union(vertice1, vertice2):
    root1=find(vertice1)
    root2=find(vertice2)
    
    if root1 != root2:
        if rank[root1]>rank[root2]:
            parent[root2]=root1
        else:
            parent[root1]=root2
            if rank[root1]==rank[root2]:
                rank[root2]+=1

def kruskal(graph):
    minimum_spanning_tree=[]
    
    for vertice in graph['vertices']:
        make_set(vertice)
        
    edges=graph['edges']
    edges.sort()
    
    for edge in edges:
        weight, vertice1, vertice2 = edge
        if find(vertice1) != find(vertice2):
            union(vertice1, vertice2)
            minimum_spanning_tree.append(edge)
            
    return minimum_spanning_tree

print(kruskal(graph))

input = sys.stdin.readline

n,m=map(int,input().split())
graph=collections.defaultdict(list)
visited=[0]*(n+1)

for i in range(m):
    u,v,weight=map(int,input().split())
    graph[u].append([weight,u,v])
    graph[v].append([weight,v,u])
    
def prim(graph,start_node):
    visited[start_node]=1
    candidate = graph[start_node]
    heapq.heapify(candidate)
    mst=[]
    total_weight=0
    
    while candidate:
        weight,u,v=heapq.heappop(candidate)
        if visited[v]==0:
            visited[v]=1
            mst.append((u,v))
            total_weight+=weight
            
            for edge in graph[v]:
                if visited[edge[2]]==0:
                    heapq.heappush(candidate, edge)
                    
    return total_weight

print(prim(graph, 'A'))

    