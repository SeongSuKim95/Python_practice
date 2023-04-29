import heapq
import sys

INF = int(1e9)
n,m = list(map(int,input().split()))
start = int(input())

graph = [[] for i in range(n+1)]
visited = [False] * (n+1)
distance = [INF] * (n+1)

for _ in range(m):
    a,b,c = list(map(int,input().split()))
    graph[a].append((b,c))

def dijkstra_heapq(start):
    
    queue = []
    heapq.heappush(queue,(0,start)) # (Distance, Node)
    
    while queue:
        dist, now = heapq.heappop(queue)
        
        if distance[now] < dist :
            continue
        
        for adj_node,adj_dist in graph[now]:
            cost = dist + adj_dist
            if distance[adj_node] < cost :
                distance[adj_node] = cost
                queue.append(queue,(cost,adj_node))      
## Floyd Warshall

INF = int(1e9)
# 노드 개수
N = int(input())
# 간선 개수
M = int(input())

graph = [[INF]*(N+1) for _ in range(N+1)]

for i in range(1,N+1):
    for j in range(1,N+1):
        if i == j :
            graph[i][j] = 0
            
# a에서 b로 가는 경로 (단방향)
for _ in range(m):
    a,b,w = list(map(int,input().split()))
    graph[a][b] = w
    
for k in range(1,N+1):
    
    for i in range(1,N+1):
        for j in range(1,N+1):
            graph[i][j] = min(graph[i][j],graph[i][k]+graph[k][j])
    