import sys
input = lambda : sys.stdin.readline().rstrip()
sys.setrecursionlimit(int(100000))
N = int(input())
LENGTH = 20
# root = 1번 노드
graph = [[] for _ in range(N+1)]
node_depth = [0 for _ in range(N+1)]
visited = [False for _ in range(N+1)]
parent = [[0]*LENGTH for _ in range(N+1)] # 여기서의 parent는 바로 윗 노드를 의미

for _ in range(N-1):
    a,b = map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)

def dfs(node,depth):

    visited[node] = True
    node_depth[node] = depth
    for adj in graph[node]:
        if visited[adj] : # 바로 윗 노드를 정해주는 과정이 이후에 처리되어야하므로 loop안에서 방문 여부를 체크
            continue
        parent[adj][0] = node # 바로 위 parent
        dfs(adj,depth+1)

root,depth = 1,0

dfs(root,depth)
for i in range(1,LENGTH):
    for j in range(1,N+1):
        parent[j][i] = parent[parent[j][i-1]][i-1] # parent[j][i] = parent[parent[j][i-1]][i-1]


M = int(input())

def find_least_ancestor(a,b):

    if node_depth[a] > node_depth[b]:
        a,b = b,a
    for i in range(LENGTH-1,-1,-1):
        if node_depth[b] - node_depth[a] >= 2**i:
            b = parent[b][i]
    if a == b:
        return a
    for i in range(LENGTH-1,-1,-1):
        if parent[a][i] != parent[b][i]:
            a,b = parent[a][i],parent[b][i]
    return parent[a][0]

for _ in range(M):
    a,b = map(int,input().split())
    print(find_least_ancestor(a,b))