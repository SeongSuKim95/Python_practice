from collections import deque

n, m = list(map(int,input().split()))

FIRE = 2
WALL = 1
NONE = 0

grid = [
    list(map(int,input().split()))
    for _ in range(n)
]

wall_pos,fire_pos = [],[]
empty_pos = []
selected_pos = []
for i in range(n):
    for j in range(m):
        if grid[i][j] == FIRE:
            fire_pos.append((i,j))
        elif grid[i][j] == WALL :
            wall_pos.append((i,j))
        elif grid[i][j] == NONE :
            empty_pos.append((i,j))

initial_empty = len(empty_pos)

max_safe = 0

dxs,dys = [-1,1,0,0],[0,0,-1,1]

def in_range(x,y):

    return 0<=x<n and 0<=y<m

def can_go(x,y,map_,visited):

    return map_[x][y] == NONE and not visited[x][y]


def bfs(map_):
    
    visited = [
        [False for _ in range(m)]
        for _ in range(n)
    ]
    
    for pos_x,pos_y in fire_pos :
        visited[pos_x][pos_y] = True

    q = deque(fire_pos)
    
    while q :
        cur_x, cur_y = q.popleft()
        for dx,dy in zip(dxs,dys):
            nx , ny = cur_x + dx, cur_y + dy
            if in_range(nx,ny) and can_go(nx,ny,map_,visited):
                visited[nx][ny] = True
                q.append((nx,ny))
    
    empty_cnt = 0

    for i in range(n):
        for j in range(m):
            if not visited[i][j]:
                empty_cnt += 1
    
    return empty_cnt - len(wall_pos) - 3



def select_pos(idx,cnt):
    global max_safe
    if cnt == 3:
        grid_temp = [row[:] for row in grid]
        for new_pos_x,new_pos_y in selected_pos:
            grid_temp[new_pos_x][new_pos_y] = WALL
        safe_cnt = bfs(grid_temp)
        max_safe = max(max_safe,safe_cnt)
        return
    
    if idx == initial_empty:
        return

    selected_pos.append(empty_pos[idx])
    select_pos(idx+1,cnt+1)
    selected_pos.pop()

    select_pos(idx+1,cnt)



select_pos(0,0)
print(max_safe)