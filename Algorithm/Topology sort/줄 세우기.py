from collections import deque

N, M = list(map(int,input().split()))

indegree = [0 for _ in range(N+1)] 
graph = [[] for _ in range(N+1)]

for _ in range(M):
    
    s, e = list(map(int,input().split()))
    graph[s].append(e)
    indegree[e] += 1

q = deque()
for i in range(1,N+1):
    if indegree[i] == 0:
        q.append(i)

result = []

while q :
    cur = q.popleft()
    result.append(cur)
    for i in graph[cur]:
        indegree[i] -= 1
        if indegree[i] == 0 :
            q.append(i)
print(*result)