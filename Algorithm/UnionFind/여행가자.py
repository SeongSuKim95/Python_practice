N = int(input())
M = int(input())

adj = [
    list(map(int,input().split()))
    for _ in range(N)
]

parent = [i for i in range(N+1)]

def find_parent(x):
    
    if parent[x] != x :
        parent[x] = find_parent(parent[x])
    return parent[x]

def union(a,b):
    pa,pb = find_parent(a),find_parent(b)
    
    if pa > pb :
        parent[pa] = pb
    else:
        parent[pb] = pa
    
for i in range(N):
    for j in range(i+1,N):
        if adj[i][j] :
            union(i+1,j+1)

lst = list(set(map(int,input().split())))

def check(lst):
    group = 0
    for i in lst:
        if group == 0:
            group = find_parent(i)
        else :
            if group != find_parent(i):
                print("NO")
                return 
    print("YES")
    return

check(lst)

            


