from collections import deque
# 행 열
N,M = list(map(int,input().split()))

grid = [
    list(map(int,input().split()))
    for _ in range(N)
]

def in_range(x,y):

    return 0<=x<N and 0<=y<M

def group_air():
    
    dxs,dys = [-1,1,0,0],[0,0,-1,1]
    visited = [
        [False] * M
        for _ in range(N)
    ]
    q = deque()
    q.append((0,0))
    while q :
        cx,cy = q.popleft()
        for dx,dy in zip(dxs,dys):
            nx,ny = cx + dx, cy + dy
            if in_range(nx,ny):
                if not visited[nx][ny] and grid[nx][ny] == 0 : 
                    visited[nx][ny] = True
                    q.append((nx,ny))
    return visited


def all_melted():
    for i in range(N):
        for j in range(M):
            if grid[i][j]:
                return False
    return True
 

def melt(is_air):

    grid_temp = [
        [0] * M 
        for _ in range(N)
    ]
    dxs,dys = [-1,1,0,0],[0,0,-1,1]

    for i in range(N):
        for j in range(M):
            if grid[i][j] == 1 :
                air_cnt = 0
                for dx,dy in zip(dxs,dys):
                    nx, ny = i + dx, j + dy
                    if in_range(nx,ny):
                        if is_air[nx][ny] :
                            air_cnt += 1
                if air_cnt < 2 : # 2변 이상이 외부공기이면
                    grid_temp[i][j] = 1
    
    for i in range(N):
        for j in range(M):
            grid[i][j] = grid_temp[i][j]

# Feedback :  빈 배열이 들어오는 것을 생각해서 time을 언제 추가할지 생각하기            
time = 0
while True :
    if all_melted() : 
        break
    air_group = group_air()
    melt(air_group)
    time += 1
print(time)