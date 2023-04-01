from collections import deque

def print_array(array):

    for row in array:
        print(*row)
    print()

n, m = list(map(int,input().split()))
# 우 하 좌 상
dirs = [(0,1),(1,0),(0,-1),(-1,0)]

grid = [
    list(map(int,input().split()))
    for _ in range(n)
]
dice = [0,1,2,3,4,5,6]
cluster_grid = [
    [0 for _ in range(n)]
    for _ in range(n)
]

def in_range(x,y):

    return 0<=x<n and 0<=y<n

def bfs():

    dxs,dys = [-1,1,0,0],[0,0,-1,1]
    
    visited = [
        [False for _ in range(n)]
        for _ in range(n)
    ]
    
    for i in range(n):
        for j in range(n):
            if not visited[i][j]:
                q = deque()
                cur_x,cur_y = i,j
                q.append((cur_x,cur_y))
                visited[cur_x][cur_y] = True
                cluster,cnum = [(cur_x,cur_y)], grid[cur_x][cur_y] 
                while q :
                    cx,cy = q.popleft()
                    for dx,dy in zip(dxs,dys):
                        nx,ny = cx + dx, cy +dy
                        if in_range(nx,ny) and not visited[nx][ny] and grid[nx][ny] == cnum:
                            visited[nx][ny] = True
                            cluster.append((nx,ny))
                            q.append((nx,ny))
                score = len(cluster) * cnum
                for x,y in cluster:
                    cluster_grid[x][y] = score
# 우 : 0
# U, F, R -> 7 - R, F, U
# 하 : 1
# U, F, R -> 7 - F, U, R
# 좌 : 2
# U, F, R -> R, F, 7 - U
# 상 : 3 
# U, F, R -> F, 7 - U, R

def simulate(cdir,cx,cy):

    global score,U,F,R

    for _ in range(m):
        dx,dy = dirs[cdir]
        nx,ny = cx + dx, cy + dy
        if in_range(nx,ny):
            pass
        else :
            cdir = (cdir + 2 + 4) % 4
            dx,dy = dirs[cdir]
            nx,ny = cx + dx, cy + dy
        
        score += cluster_grid[nx][ny]

        if cdir == 0 :
            U, F, R = 7-R, F, U
        elif cdir == 1 :
            U, F, R = 7-F, U, R
        elif cdir == 2 :
            U, F, R = R, F, 7-U
        elif cdir == 3 :
            U, F, R = F, 7-U, R
        
        if grid[nx][ny] < dice[7-U]:
            cdir = (cdir + 1 + 4) % 4
        elif grid[nx][ny] > dice[7-U]:
            cdir = (cdir - 1 + 4) % 4
        else:
            pass
        cx,cy = nx,ny

U,F,R = 1,2,3
bfs()
score = 0
simulate(0,0,0)
print(score)