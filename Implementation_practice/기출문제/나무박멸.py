n,m,k,c = list(map(int,input().split()))

EMPTY = 0
WALL = -1

grid = [
    list(map(int,input().split()))
    for _ in range(n)
]

dead = [
    [0 for _ in range(n)]
    for _ in range(n)
]

dxs,dys = [-1,1,0,0],[0,0,-1,1]
score = 0

def print_array(array):
    for row in array:
        print(*row)
    print()

def is_tree(x,y):

    return grid[x][y] > 0 

def in_range(x,y):

    return 0<=x<n and 0<=y<n

def grow():

    new_grid = [
        [EMPTY for _ in range(n)]
        for _ in range(n)
    ]
    for i in range(n):
        for j in range(n):
            if is_tree(i,j):
                cur_x,cur_y,tree_cnt = i,j,0
                for dx,dy in zip(dxs,dys):
                    nx, ny = cur_x + dx, cur_y + dy
                    if in_range(nx,ny) and is_tree(nx,ny):
                        tree_cnt += 1
                new_grid[i][j] = grid[i][j] + tree_cnt
            else : # 벽일떄
                new_grid[i][j] = grid[i][j]

    for i in range(n):
        for j in range(n):
            grid[i][j] = new_grid[i][j]

def can_go(x,y):

    return grid[x][y] == EMPTY and dead[x][y] == 0


def duplicate():

    new_grid = [
        [0 for _ in range(n)]
        for _ in range(n)
    ]

    for i in range(n):
        for j in range(n):
            if is_tree(i,j):
                cur_x,cur_y,cur_tree = i,j,grid[i][j]
                possible = [] 
                for dx,dy in zip(dxs,dys):
                    nx, ny = cur_x + dx, cur_y + dy
                    if in_range(nx,ny) and can_go(nx,ny):
                        possible.append((nx,ny))
                if possible :
                    p_tree = cur_tree // len(possible)
                    for px,py in possible :
                        new_grid[px][py] += p_tree
                
        
    for i in range(n):
        for j in range(n):
            grid[i][j] += new_grid[i][j]


def copy_dead(dead_temp):
    for i in range(n):
        for j in range(n):
            dead[i][j] = dead_temp[i][j]
                
    for i in range(n):
        for j in range(n):
            if dead[i][j] > 0 and grid[i][j] != WALL :
                dead[i][j] -= 1
                grid[i][j] = 0
            elif dead[i][j] >0 and grid[i][j] == WALL:
                dead[i][j] -= 1

def kill_trees():
    global score
    ddxs,ddys = [-1,1,-1,1],[1,1,-1,-1]

    max_cnt = (-1e9,-1e9,-1e9)
    max_dead = [
        [0 for _ in range(n)]
        for _ in range(n)
    ]
    for i in range(n):
        for j in range(n):
            # 벽, 빈칸에 뿌릴 수 있다.
            dead_temp = [
                row[:] for row in dead
            ]
            cur_x,cur_y,dead_cnt = i,j,0

            if grid[cur_x][cur_y] == WALL or grid[cur_x][cur_y] == EMPTY:
                dead_temp[cur_x][cur_y] = c+1
            else:
                dead_cnt += grid[cur_x][cur_y]
                dead_temp[cur_x][cur_y] = c+1

                for ddx,ddy in zip(ddxs,ddys):
                    for l in range(1,k+1):
                        nx, ny = cur_x + l * ddx , cur_y + l * ddy
                        if in_range(nx,ny):
                            if grid[nx][ny] == WALL:
                                dead_temp[nx][ny] = c + 1
                                break
                            elif grid[nx][ny] == EMPTY:
                                dead_temp[nx][ny] = c + 1
                                break
                            else :
                                dead_cnt += grid[nx][ny]
                                dead_temp[nx][ny] = c + 1
                        else :
                            break

            if (dead_cnt,-cur_x,-cur_y) > max_cnt :
                max_cnt = (dead_cnt,-cur_x,-cur_y)
                max_dead = [row[:] for row in dead_temp]

    score += max_cnt[0]
    copy_dead(max_dead)



for y in range(m):
    grow()
    duplicate()
    kill_trees()
print(score)