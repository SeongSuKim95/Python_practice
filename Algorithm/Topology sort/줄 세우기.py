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


# N, M = list(map(int,input().split()))

# graph = [[] for _ in range(N+1)]
# indegree = [0 for _ in range(N+1)]

# for _ in range(M):
#     a,b = list(map(int,input().split()))
#     graph[a].append(b)
#     indegree[b] += 1

# from collections import deque

# q = deque()
# for i in range(1,N+1):
#     if indegree[i] == 0 :
#         q.append(i)
# answer = []
# while q :
#     cur_node = q.popleft()
#     answer.append(cur_node)
    
#     for adj_node in graph[cur_node]:
#         indegree[adj_node] -= 1
#         if indegree[adj_node] == 0 :
#             q.append(adj_node)

# print(*answer)