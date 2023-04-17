import sys
N = int(input())
graph = [[] for _ in range(N+1)]

node_depth = [0] * (N+1)

parent = [0] * (N+1)

visited = [False] * (N+1)

def dfs(node,depth):
    
    visited[node] = True
    node_depth[node] = depth
    for child in graph[node]:
        if visited[child]:
            continue
        parent[child] = node
        dfs(child,depth+1)

for _ in range(N-1):
    a,b = list(map(int,input().split()))
    graph[a].append(b)
    graph[b].append(a)

root,depth = 1,0
dfs(root,depth)

M = int(input())

def find_least_ancestor(a,b):
    
    while node_depth[a] != node_depth[b]:
        if node_depth[a] > node_depth[b]:
            a = parent[a]
        else :
            b = parent[b]
            
    while a != b :
        
        a = parent[a]
        b = parent[b]
    
    return a
    
    
    
for _ in range(M):
    a,b = list(map(int,input().split()))
    print(find_least_ancestor(a,b))