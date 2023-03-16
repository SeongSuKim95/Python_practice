n,m,t = list(map(int,input().split()))

grid = [list(map(int,input().split())) for _ in range(n)]

wind = []

for i in range(n):
    for j in range(m):
        if grid[i][j] == -1 :
            wind.append((i,j))

next_grid = [row[:] for row in grid]

def can_go(x,y):

    return 0<=x<n and 0<=y<m and grid[x][y] != -1

def dust(): # 확산

    grid_temp = [[0]*m for _ in range(n)]
    dxs,dys = [-1,1,0,0],[0,0,-1,1]

    for i in range(n):
        for j in range(m):
            cur_dust,cur_x,cur_y = grid[i][j],i,j
            next_cur_dust = cur_dust
            if cur_dust != -1 :
                for dx,dy in zip(dxs,dys):
                    nx,ny = cur_x + dx , cur_y + dy
                    if can_go(nx,ny):
                        grid_temp[nx][ny] += cur_dust // 5
                        next_cur_dust -= cur_dust//5 
            grid_temp[cur_x][cur_y] += next_cur_dust
    
    for i in range(n):
        for j in range(m):

            grid[i][j] = grid_temp[i][j]

def print_array(array):

    for row in array:
        print(*row)


def turn_cclk(top):

    r,c = top

    grid_temp = [[0] * m for _ in range(r+1)]
    # copy center
    for i in range(r+1):
        for j in range(m):
            if i != 0 and i!= r and j!= 0 and j!= m-1 :
                grid_temp[i][j] = grid[i][j]
    # bottom
    for j in range(1,m-1):
        grid_temp[r][j+1] = grid[r][j] 
    
    # right

    for i in range(r,0,-1):
        grid_temp[i-1][m-1] = grid[i][m-1]
    
    # top

    for j in range(m-1,0,-1):
        grid_temp[0][j-1] = grid[0][j]

    # left
    for i in range(r-1):
        grid_temp[i+1][0]= grid[i][0]

    grid_temp[r][c] = -1

    for i in range(0,r+1):
        for j in range(m):
            grid[i][j] = grid_temp[i][j]


def turn_clk(down):

    r,c = down

    grid_temp = [[0] * m for _ in range(r,n)]
    # copy center
    for i in range(r,n):
        for j in range(m):
            if i != r and i!= n-1 and j!= 0 and j!= m-1 :
                grid_temp[i-r][j] = grid[i][j]
        
    # top
    for j in range(1,m-1):
        grid_temp[0][j+1] = grid[r][j]
    
    # right
    for i in range(r,n-1):
        grid_temp[i+1-r][m-1] = grid[i][m-1]

    # bottom
    for j in range(m-1,0,-1):
        grid_temp[n-r-1][j-1] = grid[n-1][j] 
    
    # left
    for i in range(n-1,r,-1):
        grid_temp[i-1-r][0]= grid[i][0]

    grid_temp[0][c] = -1

    for i in range(n-r):
        for j in range(m):
            grid[i+r][j] = grid_temp[i][j]

def wind_rotate():

    top, down = wind
    turn_cclk(top)
    turn_clk(down)
    # print_array(grid)
for _ in range(t):
    dust()
    # print_array(grid)
    wind_rotate()
    
answer = 2

for i in range(n):
    for j in range(m):
        answer += grid[i][j]
print(answer)