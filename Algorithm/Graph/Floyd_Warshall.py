# Floyd Warshall
# 겁먹지 말자 생각보다 쉽고 아이디어도 직관적이다

# node k를 경유하여 a에서 b로 간다고 할떄 
# Distance(a,b) = min(Dist_atob, Dist_atok + Dist_ktob)

INF = int(1e9) # 2차원 distance list 초기값

# 노드의 개수 및 간선의 개수 입력받기

n = int(input())
m = int(input())

# 2차원 리스트를 graph로 표현하고, 모든 값을 무한대로 초기화

graph = [[INF] * (n+1) for _ in range(n+1)]

# 자기 자신에 대한 distance는 0으로 초기화하기
for a in range(1,n+1):
    for b in range(1,n+1):
        if a == b:
            graph[a][b] = 0

# 간선 정보 입력 받아서 초기화 수행하기
for _ in range(m):
    # A에서 B로 가는 비용은 C라고 설정
    a,b,c = map(int,input().split())
    graph[a][b] = c

# Floyd Warshall Algorithm
# 시간복잡도는? --> O(n^3)
for k in range(1,n+1): # 경유하는 node
    for a in range(1,n+1): # 출발하는 node
        for b in range(1,n+1): # 도착하는 node
            graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])
            # a에서 출발하여 b로 도착하는 distance와!
            # a에서 k를 경유하여 b로 도착하는 distance 중!
            # 거리가 짧은 값으로 a-->b 의 최단거리를 update한다!

# 결과를 출력해보자!

for a in range(1,n+1):
    for b in range(1,n+1):
        # 도달할 수 없는 경우, 무한이라고 출력
        if graph[a][b] == INF:
            print("INFINITY",end =" ")
        # 도달할 수 있는 경우 거리를 출력
        else:
            print(graph[a][b],end= " ")
    print()



# 플로이드 워셜 알고리즘은 모든 노드 간 최단경로를 구하는 알고리즘으로, 다익스트라 알고리즘과는 다르게 음의 값을 가지는 간선에도 적용이 될 수 있다.
