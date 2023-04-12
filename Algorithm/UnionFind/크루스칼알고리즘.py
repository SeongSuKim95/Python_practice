# 백준 1197 최소 신장 트리
import sys
input = lambda : sys.stdin.readline().rstrip()

V, E = map(int,input().split())

parents = [i for i in range(V+1)]
edges = []

for _ in range(E):
    a,b,cost = map(int,input().split())
    edges.append((cost,a,b))

# edge cost를 오름차순 정렬
edges.sort()

def find_parent(x):

    if parents[x] != x :
        parents[x] = find_parent(parents[x])
    return parents[x]

def union(a,b):

    pa,pb = find_parent(a),find_parent(b)
    if pa > pb :
        parents[pa] = pb # a의 부모를 pb로
    else :
        parents[pb] = pa # b의 부모를 pa로

answer = 0

for cost,a,b in edges:
    if find_parent(a) != find_parent(b):
        union(a,b)
        answer += cost

print(answer)