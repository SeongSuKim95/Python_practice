import sys
input = sys.stdin.readline
G = int(input())
P = int(input())

parent = [i for i in range(G+1)]

def find_parent(x):
    if x != parent[x]:
        parent[x] = find_parent(parent[x])
    return parent[x]

def union(a,b): # a < b

    a,b = find_parent(a),find_parent(b)
    parent[b] = a

cnt = 0
for _ in range(P):

    plane = int(input())
    
    plane = find_parent(plane)

    if plane == 0 :
        break
    union(plane-1,plane)
    cnt += 1
print(cnt)