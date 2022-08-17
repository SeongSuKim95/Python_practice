## BFS
def solution(n, computers):
    answer = 0
    visited = [False for i in range(n)]
    for com in range(n):
        if visited[com] == False:
            BFS(n, computers, com, visited)
            answer += 1
    return answer

def BFS(n, computers, com, visited):
    visited[com] = True
    queue = []
    queue.append(com)
    while len(queue) != 0:
        com = queue.pop(0)
        visited[com] = True
        for connect in range(n):
            if connect != com and computers[com][connect] == 1:
                if visited[connect] == False:
                    queue.append(connect)
                    
## DFS
def solution(n, computers):
    answer = 0
    visited = [False for i in range(n)]
    for com in range(n):
        if visited[com] == False:
            DFS(n, computers, com, visited)
            answer += 1 #DFS로 최대한 컴퓨터들을 방문하고 빠져나오게 되면 그것이 하나의 네트워크.
    return answer

def DFS(n, computers, com, visited):
    visited[com] = True
    for connect in range(n):
        if connect != com and computers[com][connect] == 1: #연결된 컴퓨터
            if visited[connect] == False:
                DFS(n, computers, connect, visited)


# 내 코드

def DFS(computers,com,visited):

    visited[com] = True
    
    for idx, connect in enumerate(computers[com]):
        if connect and visited[idx] == False:
            DFS(computers,idx,visited)
    
    
def solution(n, computers):

    answer = 0
    visited = [False] * n
    for com in range(n): # n개의 computer 연결관계를 탐색해야하니까!
        if visited[com] == False: # 방문 안한 곳에 대해
            DFS(computers,com,visited) # DFS 수행
            answer+=1 # 온전히 다 돌고 나오면 network개수 한개 추가
        
    
    return answer

from collections import deque


def solution(n, computers):
    answer = 0
    visited = [False for i in range(n)]
    for connect in range(n):
        if visited[connect] == False:
            BFS(n, computers, connect, visited)
            answer += 1
    return answer

def BFS(n, computers, connect, visited):
    
    visited[connect] = True
    queue = deque([connect])
    while queue :
        com = queue.popleft()
        for idx,i in enumerate(computers[com]):
            if i and visited[idx] == False:
                queue.append(idx)
                visited[idx] = True



# 연결된 group의 개수를 세는 것은 , DFS가 끝나는 시점을 세는것과 동일 하므로 DFS에 return 또는 종료조건을 다는것이 아닌 끝난 이후 main에서 count를 하면 된다.