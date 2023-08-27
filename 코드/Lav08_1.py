import heapq

graph = {
    'v1':{'v2':2, 'v4':1},
    'v2':{'v4':3, 'v5':10},
    'v3':{'v1':4, 'v5':5},
    'v4':{'v3':2, 'v5':2, 'v6':8, 'v7':4},
    'v5':{'v7':6},
    'v6':{},
    'v7':{'v6':1}
    }

def dijkstra(graph, start):
    distances={node: float('inf') for node in graph}
    distances[start]=0
    queue=[]
    heapq.heappush(queue, [distances[start],start])
    
    while queue:
        current_distance, current_destination = heapq.heappop(queue)
        
        if distances[current_destination] < current_distance:
            continue
        
        for new_destination, new_distance in graph[current_destination].items():
            distance=current_distance+new_distance
            if distance < distances[new_destination]:
                distances[new_destination]=distance
                heapq.heappush(queue, [distance, new_destination])
                
    return distances

print(dijkstra(graph,'v1'))
    