import sys
input = lambda : sys.stdin.readline().rstrip()
sys.setrecursionlimit(int(100000))
N = int(input())

# root = 1번 노드
graph = [[] for _ in range(N+1)]
node_depth = [0 for _ in range(N+1)]
visited = [False for _ in range(N+1)]
parent = [0] * (N+1) # 여기서의 parent는 바로 윗 노드를 의미

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
        parent[adj] = node # 바로 위 parent
        dfs(adj,depth+1)

root,depth = 1,0
dfs(root,depth)

M = int(input())

def find_least_ancestor(a,b):

    while node_depth[a] != node_depth[b]:
        if node_depth[a] > node_depth[b]:
            a = parent[a] # 한칸 거슬러 올라가기
        else :
            b = parent[b]
    
    while a != b :
        a = parent[a] # 한칸씩 거슬러 올라가며 찾기
        b = parent[b]
    
    return a

for _ in range(M):
    a,b = map(int,input().split())
    print(find_least_ancestor(a,b))