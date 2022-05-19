
def factorial(n):
    if n <=1:
        return 1  
    return n * factorial(n-1)

print(factorial(5))

# 유클리드 호제법
# 두 자연수 A,B에 대하여 (A>B) A를 B로 나눈 나머지를 R
# A,B의 최대공약수는 B,R의 최대공약수와 같다

def gcd(a,b):

    if a % b == 0 :
        return b
    else :
        return gcd(b,a%b)
print(gcd(192,162))

# DFS

# 각 노드가 연결된 정보 표현 하는 방법 ? --> 2차원 리스트 사용

def dfs(graph,v,visited):
    
    visited[v] = True
    print(v,end='')


graph = [
    [], # index 0은 사용하지 않기 위해 쓰는 trick
    [2,3,8],
    [1,7],
    [1,4,5],
    [3,5],
    [3,4],
    [7],
    [2,6,8],
    [1,7]
]

# 각 노드가 방문된 정보를 표현하는 list(1차원 리스트)
visited = [False] * 9

def dfs(graph,v,visited): # graph정보, 노드 번호, 노드 방문 list
    visited[v] = True
    print(v,end='')
    for i in graph[v]: # v노드의 인접 노드들에 대해
        if not visited[i]:
            dfs(graph,i,visited)

dfs(graph,1,visited)

# BFS 
from collections import deque

visited = [False] * 9

def bfs(graph,start,visited):
    queue = deque([start])
    visited[start] = True
    while queue: 
        v = queue.popleft()
        print(v, end = ' ')
        for i in graph[v]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True

bfs(graph,1,visited)

