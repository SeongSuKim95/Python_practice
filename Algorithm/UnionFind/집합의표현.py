import sys
input = sys.stdin.readline
sys.setrecursionlimit(100000)
n,m = list(map(int,input().split()))

parent = [i for i in range(n+1)]

def find_parent(x):
    
    if parent[x] != x :
        parent[x] = find_parent(parent[x])
    return parent[x]

def union(a,b):
    
    pa,pb = find_parent(a),find_parent(b)
    if pa < pb :
        parent[pb] = pa
    else :
        parent[pa] = pb
    
for _ in range(m):
    op, a, b = list(map(int,input().split()))
    if not op :
        union(a,b) 
    else :
        if find_parent(a) == find_parent(b):
            print("YES")
        else:
            print("NO")
