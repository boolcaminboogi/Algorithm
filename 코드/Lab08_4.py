import sys
import heapq

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