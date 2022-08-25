# Dijkstra Algorithm

# 최단 거리 테이블은 각 노드에 대한 현재까지의 최단 거리 정보를 가짐
# 최단 거리 테이블은 처음에 모든 노드에 대해 inf로 설정한다.
# 그리디 알고리즘 : 매 상황에서 방문하지 않은 가장 비용이 적은 노드를 선택해 임의의 과정을 반복
# 단계를 거치며 한번 처리된 노드의 최단거리는 고정되어 바뀌지 않음
# 한 단계당 하나의 노드에 대한 최단 거리를 확실히 찾는것이므로, 다익스트라 알고리즘을 수행한 뒤에 테이블에 각 노드까지의 최단 거리 정보가 저장
import heapq
import sys
input = sys.stdin.readline


INF = int(1e9) # distance를 담는 배열을 초기
n,m = map(int,input().split())
start = int(input())


graph = [[] for i in range(n+1)]
visited = [False] * (n+1)
distance = [INF] * (n+1)

for _ in range(m):
    a,b,c = map(int,input().split()) # node (a,b) distance c
    graph[a].append((b,c))

def get_smallest_node():
    
    min_value = INF
    index = 0 # 가장 최단 거리가 짧은 노드
    for i in range(1,n+1): # 방문하지 않은 노드중에서 가장 짧은 최단거리를 가진 index 찾기
        if distance[i] < min_value and not visited[i]:
            min_value = distance[i]
            index = i
    return index


def dijkstra(start): # Start 노드에서 출발하여 다른 노드로 가는 각각의 최단경로를 구해주는 알고리즘
    
    distance[start] = 0 
    visited[start] = True
    
    for j in graph[start]:
        distance[j[0]] = j[1] # 시작 노드와 연결된 node 거리 초기화

    for i in range(n-1): # node 개수 - 1 만큼 반복한다. 각 node의 최단거리는 매 node를 처리하는 순간 결정되기 때문에 마지막 node는 안해도 됨!
        # 현재 최단 거리가 가장 짧은 노드를 꺼내서, 방문 처리
        now = get_smallest_node() # Node의 index 반환
        visited[now] = True
        
        for j in graph[now]:
            cost = distance[now] + j[1]
            if cost < distance[j[0]]: # 최단거리 업데이트
                distance[j[0]] = cost

def dijkstra_heapq(start):

    queue = []
    heapq.heappush(queue,(0,start)) # (Distance, Node), Start 에서 start까지의 거리는 0이니까!

    while queue: # Queue가 빌때까지

        dist, now = heapq.heappop(queue) # Distance가 가장 작은 node를 pop
        
        if distance[now] < dist: # 우선순위 queue에서 꺼낸 node가 이미 처리된 node일때 발생하는 현상
                continue
        
        for i in graph[now]:
            cost = dist + i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(queue,(cost,i[0]))

dijkstra_heapq(start)
# dijkstra(start)

# 출발 지점부터 모든 노드까지의 최단 거리 출력

for i in range(1,n+1):

    if distance[i] == INF:
        print("INFINITY")
    else:
        print(distance[i])

# Priority queue를 사용한 개선된 dijkstra 알고리즘













