from collections import deque

n, m = list(map(int,input().split()))

grid = [list(map(int,input().split())) for _ in range(n)]

hospital_pos = []
selected_pos = []
people_pos = []
min_dist = 1e9

for i in range(n):
    for j in range(n):
        if grid[i][j] == 2 :
            hospital_pos.append((i,j))
        elif grid[i][j] == 1 :
            people_pos.append((i,j))

def in_range(x,y):
    
    return 0<=x<n and 0<=y<n


def bfs():
    grid_temp = [[0]* n for _ in range(n)]
    visited = [[-1] * n for _ in range(n)]

    for px,py in people_pos:
        grid_temp[px][py] = 1
    for hx,hy in selected_pos :
        grid_temp[hx][hy] = 2
        visited[hx][hy] = 0
 
    dxs, dys = [-1,1,0,0],[0,0,-1,1]

    q = deque(selected_pos)
    dist_sum, people_cnt = 0, 0 
    while q and people_cnt != len(people_pos):
        cur_x, cur_y = q.popleft()
        for dx,dy in zip(dxs,dys):
            nx, ny = cur_x + dx, cur_y + dy
            if in_range(nx,ny) and visited[nx][ny] == -1:
                visited[nx][ny] = visited[cur_x][cur_y] + 1
                if grid_temp[nx][ny] == 1 :
                    dist_sum += visited[nx][ny]
                    people_cnt += 1
                q.append((nx,ny))

    return dist_sum
def select_hospital(idx,cnt):
    global min_dist
    
    if cnt == m :
        min_dist = min(min_dist,bfs())
        return
    
    if idx == len(hospital_pos):
        return

    selected_pos.append(hospital_pos[idx])
    select_hospital(idx+1,cnt+1)
    selected_pos.pop()

    select_hospital(idx+1,cnt)


select_hospital(0,0)
print(min_dist)