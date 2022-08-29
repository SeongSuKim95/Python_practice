from collections import deque

def solution(maps):
    answer = bfs(0,0,maps) # 시작지점은 0,0!
    return -1 if answer == 1 else answer


def bfs(x,y,maps): # 좌표를 입력을 받는다.
    
    queue = deque()
    
    dx = [0,0,-1,1] # 상하좌우
    dy = [-1,1,0,0]
    
    queue.append((x,y)) # 현재 지점 queue에 추가
    
    while queue: # Queue가 빌때까지 반복한다.
        
        x,y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            
            if nx < 0 or nx >= len(maps) or ny < 0 or ny >=len(maps[0]): continue
            # map 범위 넘어가면 고려 X
            if maps[nx][ny] == 0: continue
            # 벽이면 고려 X
            if maps[nx][ny] == 1 :
                maps[nx][ny] = maps[x][y] + 1 # 현 지점 값에서 +1
                queue.append((nx,ny)) # queue값에 추가해주기 
    return maps[len(maps)-1][len(maps[0])-1]
    
    
# 내코드

from collections import deque

def solution(maps):
    answer = bfs(0,0,maps)
    if answer == 1:
        return -1
    else :
        return answer


def bfs(x,y,maps):
    
    # 상 하 좌 우 
    dx = [0,0,-1,1]
    dy = [-1,1,0,0]
    
    queue = deque() # 항상 0,0에서 시작 , 2차원 좌표를 queue에 넣을 때는 (x,y) 형식으로 넣는다!
    queue.append((x,y))  # deque 선언하고, (x,y)를 넣어줘야함   
    while queue:
        x,y= queue.popleft()
        
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            # 좌표가 범위를 넘어갈때
            if nx < 0 or ny < 0 or ny >= len(maps) or nx >= len(maps[0]):
                continue
            # 벽일때
            if maps[ny][nx] == 0 :
                continue
            # 갈수있는 길이면! maps[nx][ny] != 0 이 아님에 주의 
            if maps[ny][nx] == 1:
                queue.append((nx,ny))
                maps[ny][nx] = maps[y][x] +1

                
    return maps[-1][-1]

# 주의할점 !!! 
# deque에 tuple 을 넣을때는 deque()을 선언하고, append로 (x,y) 형태로 넣어준다
# 2차원 배열을 생각 할때 maps[y축][x축] 이 들어가야 한다. 좌표와 map에서 indexing을 헷갈리지 않기!