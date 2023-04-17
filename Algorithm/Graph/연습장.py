import heapq
import sys

input = sys.stdin.readline

INF = int(1e9)

n,m = map(int,input().split())
start = int(input())

graph = [[] for i in range(n+1)]
visited = [False] * (n+1)
distance = [INF] * (n+1)

for _ in range(m):
    a,b,c = map(int,input().split())
    graph[a].append(b,c)
    
def dijkstra(start):
    
    queue = []
    heapq.heappush(queue,(0,start))
    
    while queue:
        dist, now = heapq.heappop(queue)
        
        if distance[now] < dist :
            continue
            
        for adj_node,adj_dist in graph[now]:
            cost = dist + adj_dist
            if cost < distance[adj_node]:
                distance[adj_node] = cost
                heapq.heappush(queue,(cost,adj_node))
             


dijkstra(start)