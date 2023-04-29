# 최소 신장 트리

V, E = map(int,input().split())

parent = [i for i in range(V+1)]
edges = []

for _ in range(E):
    
    a,b,w = list(map(int,input().split()))
    edges.append((w,a,b))

def find_parent(x):
    
    if parent[x] != x :
        parent[x] = find_parent(parent[x])
    return parent[x]

def merge(a,b):
    
    a,b = find_parent(a),find_parent(b)
    if a < b :
        parent[b] = a
    else :
        parent[a] = b

edges.sort()
answer = 0
for w,a,b in edges:
    if find_parent(a) != find_parent(b):
        merge(a,b)
        answer += w
print(answer)