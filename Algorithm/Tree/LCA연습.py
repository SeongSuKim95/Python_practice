import sys
N = int(input())
graph = [[] for _ in range(N+1)]

for _ in range(N-1):
    a,b = list(map(int,input().split()))
    graph[a].append(b)
    graph[b].append(a)
    
# 깊이 측정
depth_lst = [0 for _ in range(N+1)]
visited = [False for _ in range(N+1)]
# 부모 표시(바로 윗 노드를 의미)
parent = [0 for _ in range(N+1)]

def find_depth(node,depth):
    
    visited[node] = True
    depth_lst[node] = depth
    for adj in graph[node]:
        if not visited[adj]:
            find_depth(adj,depth+1)
            parent[adj] = node
    
root,depth = 1,0
find_depth(root,depth)

M = int(input())

for _ in range(M):
    a,b = list(map(int,input().split()))
    
    while depth_lst[a] != depth_lst[b]:
        if depth_lst[a] > depth_lst[b]:
            a = parent[a]
        else :
            b = parent[b]
    
    while a != b:
        a,b = parent[a],parent[b]
    
    print(a)
        
