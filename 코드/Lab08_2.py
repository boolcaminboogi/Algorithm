import sys

def floyd(n,data):
    dist = [[sys.maxsize]*n for _ in range(n)]
    
    for i, j, edge in data:
        dist[i-1][j-1]=edge
        
    for k in range(n):
        dist[k][k]=0
        for i in range(n):
            for j in range(n):
                dist[i][j]=min(dist[i][j],dist[i][k]+dist[k][j])
                
    return dist

n=5
data=[[1,2,1],[2,1,9],[2,4,2],[2,3,3],[1,5,5],[5,1,3],[1,4,1],[4,5,3],[4,3,2],[3,4,4]]

print(floyd(n,data))


