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
    
    
                