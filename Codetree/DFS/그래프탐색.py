N, M = list(map(int,input().split()))

edges = [list(map(int,input().split())) for _ in range(M)]

graph = [[] for _ in range(N+1)]
visited = [False for _ in range(N+1)]
visited[1] = True

for s,e in edges:
    graph[s].append(e)
    graph[e].append(s)

cnt = 0
def dfs(vertex):
    global cnt
    for curVertex in graph[vertex]:
        if not visited[curVertex]:
            visited[curVertex] = True
            cnt += 1
            dfs(curVertex)
dfs(1)
print(cnt)