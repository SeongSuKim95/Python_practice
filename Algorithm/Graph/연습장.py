# 다익스트라 heapq 구현
import heapq
import sys

input = sys.stdin.readline

INF = 1e9
n,m = map(int,input().split())
start = int(input())
# 인접노드 저장
graph = [[] for _ in range(n+1)]
distance = [INF] * (n+1)

for _ in range(m):
    a,b,w = map(int,input().split())
    graph[a].append((b,w))
    # 양방향 그래프면 graph[b].append((a,w)) 해줘야함!!!

def dijkstra(start):

    q = []
    # (dist, node)
    heapq.heappush(q,(0,start))
    while q: # q 빌떄까지 돌리면 됨
        cur_dist,cur_node = heapq.heappop(q)
        if distance[cur_node] < cur_dist: # 우선순위 queue에서 꺼낸 node가 이미 처리된 node이면
            continue
        for adj_node in graph[cur_node]:
            cost = cur_dist + adj_node[1]
            if cost < distance[adj_node[0]] :
                distance[adj_node[0]] = cost
                heapq.heappush(q,(cost,adj_node[0]))

for i in range(1,n+1):

    if distance[i] == INF:
        print("INFINITY")
    else:
        print(distance[i])

# 플로이드 워셜

import sys

INF = sys.maxsize

n,m = list(map(int,input().split()))

dist = [
    [INF for _ in range(n+1)]
    for _ in range(n+1)
]

for _ in range(m):

    x,y,z = list(map(int,input().split()))
    dist[x][y] = min(dist[x][y],z)


for i in range(1,n+1):
    dist[i][i] = 0

for k in range(1,n+1): # 거쳐갈 노드 번호
    for i in range(1,n+1): # 모든 쌍 (i,j)에 대해 !
        for j in range(1,n+1):
            dist[i][j] = min(dist[i][j] , dist[i][k] + dist[k][j])

for i in range(1,n+1):
    for j in range(1,n+1):
        if dist[i][j] == INF :
            dist[i][j] = -1

for row in dist[1:]:
    print(*row[1:])