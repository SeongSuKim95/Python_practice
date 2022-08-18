# 이코테 알고리즘 유형별 기출문제 Q 15

from collections import deque, defaultdict

N,M,K,X = map(int,input().split())

data = defaultdict(list)

for i in range(M):
    a,b = map(int,input().split())
    data[a].append(b)
    data[b].append(a) 


def solution(data,N,K,X):

    visited = [False] * (N+1)
    dists = {i : 0 for i in range(1,N+1)}
    queue = deque([X])
    dist = 1
    visited[X] = True
    while queue:        
        cur = queue.popleft()
        for node in data[cur]:
            if visited[node] == False :
                dists[node] = dist
                visited[node] = True
                queue.append(node)
        dist +=1

    if K not in dists.values():
        print(-1)
    for key,value in dists.items():
        if value == K:
            print(key)
        

# N,M,K,X = 4,4,2,1
# data = {1:[2,3],2:[1,3,4],3:[1,2],4:[2]}

solution(data,N,K,X)

