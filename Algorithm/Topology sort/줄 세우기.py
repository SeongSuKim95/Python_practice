from collections import deque

N, M = list(map(int,input().split()))

# 진입 차수 정의
indegree = [0 for _ in range(N+1)]

# 방향 그래프 
graph = [[] for _ in range(N+1)]

for _ in range(M):
    s, e = list(map(int,input().split()))
    graph[s].append(e)
    indegree[e] += 1 

q = deque()
# 진입 차수 0인 노드 넣기
for i in range(1,N+1):
    if indegree[i] == 0:
        q.append(i)

result = []

while q :
    cur = q.popleft()
    result.append(cur)
    for i in graph[cur]:
        indegree[i] -= 1 # 진입차수 1빼기
        if indegree[i] == 0 :
            q.append(i)
print(*result)