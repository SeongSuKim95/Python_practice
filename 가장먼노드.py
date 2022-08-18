# 내코드

from collections import deque, defaultdict
def solution(n, vertex):
    
    data = defaultdict(list)
    for i in vertex:
        data[i[0]].append(i[1])
        data[i[1]].append(i[0])
    
    queue = deque(data[1])
    
    dists = [0] * (n+1)
    dist = 1
    while queue:
        for i in queue:
            dists[i] = dist
        dist += 1
        for i in range(len(queue)):
            cur = queue.popleft()
            for j in data[cur]:            
                if not dists[j]:
                    queue.append(j)
    dists = dists[2:]
    
    return dists.count(max(dists))

# 정답 코드 
import collections
def solution(n, vertex):
    dists = {i:0 for i in range(1, n+1)}  #(1)  
    edge = collections.defaultdict(list)
    
    for v, u in vertex:                   #(2)
        edge[v].append(u)
        edge[u].append(v)
        
    q = collections.deque(edge[1])        #(3)
    dist = 1 
    while q:                              
        for i in range(len(q)):
            v = q.popleft()
            
            if dists[v] == 0:
                dists[v] = dist
                
                for w in edge[v]:
                    q.append(w)
        dist += 1        
    
    del dists[1]                          #(4)
    
    max_value = max(dists.values())
    
    answer = 0
    for v in dists.values():              #(5)
        if v == max_value:
            answer += 1
        
    return answer

# Distance 행렬을 딕셔너리 형태로 생성 한다! 각 노드에 대한 정보를 담을 수 있도록 하기 위함
