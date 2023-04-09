import sys
input = sys.stdin.readline
sys.setrecursionlimit(100000)

N, M = list(map(int,input().split()))

parent = [i for i in range(N)]

def find_parent(x):
    
    if x != parent[x]:
        parent[x] = find_parent(parent[x])
    return parent[x]

def union(a,b):
    
    pa,pb = find_parent(a), find_parent(b)
    if pa < pb :
        parent[pb] = pa
    else:
        parent[pa] = pb


def simulate():
    for i in range(M):
        x, y = list(map(int,input().split()))
        if find_parent(x) == find_parent(y): # 사이클 생성됨!
            print(i+1)
            return    
        union(x,y)
    print(0)
    return 
simulate()