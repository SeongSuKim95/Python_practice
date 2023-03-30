from collections import deque

def print_array(array):

    for row in array:
        print(*row)
    print()

HEAD = 1
TAIL = 3
BODY = 2
ROUTE = 4
n,m,k = list(map(int,input().split()))

# 우 상 좌 하
dxs,dys = [0,-1,0,1],[1,0,-1,0]

score = 0

grid = [
    list(map(int,input().split())) for _ in range(n)
]

def in_range(x,y):

    return 0<=x<n and 0<=y<n and grid[x][y] 

def move_team(hx,hy):

    new_grid = [row[:] for row in grid]
    cur_x,cur_y = hx,hy
    p_x,p_y = 0,0
    nhx,nhy = -1,-1
    team_pos = []
    while True :
        cur_state = grid[cur_x][cur_y]
        if cur_state == TAIL:
            new_grid[p_x][p_y] = TAIL
            team_pos.append((p_x,p_y))
            if (nhx,nhy) != (cur_x,cur_y):
                new_grid[cur_x][cur_y] = ROUTE
            break
        for dx,dy in zip(dxs,dys):
            nx, ny = cur_x + dx, cur_y + dy
            if in_range(nx,ny):
                if cur_state == HEAD:
                    if grid[nx][ny] == BODY :
                        next_x,next_y = nx,ny
                    elif grid[nx][ny] == ROUTE or grid[nx][ny] == TAIL :
                        new_grid[nx][ny] = HEAD
                        team_pos.append((nx,ny))
                        nhx,nhy = nx,ny
                elif cur_state == BODY :
                    if (nx,ny) != (p_x,p_y):
                        next_x,next_y = nx,ny

        if cur_state == HEAD:
            p_x,p_y = cur_x,cur_y
            cur_x,cur_y = next_x,next_y

        elif cur_state == BODY:
            new_grid[p_x][p_y] = BODY
            team_pos.append((p_x,p_y))
            p_x,p_y = cur_x,cur_y
            cur_x,cur_y = next_x,next_y

    for i in range(n):
        for j in range(n):
            grid[i][j] = new_grid[i][j]

    return team_pos

def move_all():

    head_pos = []
    pos_info = []
    for i in range(n):
        for j in range(n):
            if grid[i][j] == HEAD:
                head_pos.append((i,j))
    for hx,hy in head_pos :
        pos = move_team(hx,hy)
        pos_info.append(pos[:])

    return pos_info

def get_score(x,y,pos_info):
    global score
    cur_x,cur_y = x,y
    # print(pos_info)
    for team_pos in pos_info:
        if (x,y) in team_pos:
            score += (team_pos.index((x,y)) + 1)**2
            break

    hx,hy = team_pos[0]
    tx,ty = team_pos[-1]

    grid[hx][hy] = TAIL
    grid[tx][ty] = HEAD

def throw_ball(turn,pos_info):
    # turn은 0 부터
    # (x,y,dir)
    ways = [
        [(i,0,0) for i in range(n)],
        [(n-1,i,1) for i in range(n)],
        [(n-1-i,n-1,2) for i in range(n)],
        [(0,n-1-i,3) for i in range(n)]
    ]
    div,mod = (turn // n) % 4, turn % n
    sx,sy,d = ways[div][mod]
    dx,dy = dxs[d],dys[d]    

    for i in range(n):
        cx,cy = sx + i * dx, sy + i * dy
        if grid[cx][cy] and grid[cx][cy] != ROUTE:
            get_score(cx,cy,pos_info)
            break

for i in range(k):
    pos_info = move_all()
    throw_ball(i,pos_info)


# print(score)
# print_array(grid)
print(score)