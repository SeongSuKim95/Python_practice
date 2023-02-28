from collections import deque

N, M = list(map(int,input().split()))

map_ = [list(map(int,input().split())) for _ in range(N)]

ice_cnt = 0
for i in range(N):
    for j in range(M):
        if map_[i][j]:
            ice_cnt += 1

dxs,dys = [-1,1,0,0],[0,0,-1,1]

visited = [[False] * M for _ in range(N)]

def in_range(x,y):

    return 0 <= x < N and 0<= y <M and not visited[x][y] 

def bfs():
    global ice_cnt

    q = deque()
    visited[0][0] = True
    q.append((0,0))
    time = 0 
    while True :
        cur_ice_cnt = 0 
        next_q = deque()
        while q :
            cur_x, cur_y = q.popleft()
            for dx,dy in zip(dxs,dys):
                nx , ny = cur_x + dx, cur_y + dy
                if in_range(nx,ny):
                    if map_[nx][ny] == 0:
                        visited[nx][ny] = True
                        q.append((nx,ny))
                    elif map_[nx][ny] == 1:
                        visited[nx][ny] = True
                        cur_ice_cnt += 1
                        next_q.append((nx,ny))
                        ice_cnt -= 1 
        q = next_q.copy()
        time += 1
        if not ice_cnt :
            break

    print(time, cur_ice_cnt)

bfs()