# Dijkstra Algorithm

# 최단 거리 테이블은 각 노드에 대한 현재까지의 최단 거리 정보를 가짐
# 최단 거리 테이블은 처음에 모든 노드에 대해 inf로 설정한다.
# 그리디 알고리즘 : 매 상황에서 방문하지 않은 가장 비용이 적은 노드를 선택해 임의의 과정을 반복
# 단계를 거치며 한번 처리된 노드의 최단거리는 고정되어 바뀌지 않음
# 한 단계당 하나의 노드에 대한 최단 거리를 확실히 찾는것이므로, 다익스트라 알고리즘을 수행한 뒤에 테이블에 각 노드까지의 최단 거리 정보가 저장


import sys

input = sys.stdin.readline
INF = int(1e9)

# 노드의 개수, 간선의 개수를 입력받기
n,m = map(int,input().split())
# 시작 노드 번호 입력받기
start = int(input())
# 각 노드에 연결되어 있는 노드에 대한 정보를 담을 리스트
graph = [[] for i in range(n+1)]
# 방문한 적이 있는지 체크하는 목적의 리스트를 만들기
visited = [False] * (n+1)
# 최단 거리 테이블을 모두 무한으로 초기화
distance = [INF] * (n+1)

# 모든 간선 정보를 입력받기
for _ in range(m):
    a,b,c = map(int,input().split*())
    # a번 노드에서 b번 노드로 가는 cost = c
    graph[a].append((b,c))
# 방문하지 않은 노드 중에서, 가장 최단거리가 짧은 노드의 번호를 반환

def get_smallest_node():
    min_value = INF
    index = 0 # 가장 최단 거리가 짧은 노드 (인덱스)
    for i in range(1, n+1):
        if distance[i] < min_value and not visited[i]:
            min_value = distance[i]
            index = i
        return index


def dijkstra(start):
    # 시작 노드에 대해 초기화
    distance[start] = 0 
    visited[start] = True
    for j in graph[start]:
        distance[j[0]] = j[1]
    # 시작 노드를 제외한 전체 n-1개의 노드에 대해 반복
    for i in range(n-1):
        # 현재 최단 거리가 가장 짧은 노드를 꺼내서, 방문 처리
        now = get_smallest_node()
        visited[now] = True
        # 현재 노드와 연결된 다른 노드를 확인
        for j in graph[now]:
            cost = distance[now] + j[1]
            # 현재 노드를 거쳐서 다른 노드로 이동하는 거리가 더 짧은 경우
            if cost < distance[j[0]]:
                distance[j[0]] = cost
    
dijkstra(start)

for i in range(1,n+1):
    if distance[i]==INF:
        print("INFINITY")
    else:
        print(distance[i])
