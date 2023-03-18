N = int(input())

grid = [
    list(map(int,input().split()))
    for _ in range(N)
]

r,c,m1,m2,m3,m4,dir = list(map(int,input().split()))

# dir - 1: 시계, 0 : 반시계

dir_mapper = {
    1:[(-1,1),(-1,-1),(1,-1),(1,1)], #cclk
    0:[(-1,-1),(-1,1),(1,1),(1,-1)], #clk
}

def rotate(dir):

    dirs = dir_mapper[dir]
    if dir == 0 :
        pattern = [m4,m3,m2,m1]
    elif dir == 1 :
        pattern = [m1,m2,m3,m4]
    cur_x,cur_y = r-1,c-1
    temp = grid[cur_x][cur_y]
    for (dx,dy), length in zip(dirs,pattern):
        for _ in range(length):
            nx,ny = cur_x + dx, cur_y + dy
            grid[cur_x][cur_y] = grid[nx][ny] 
            cur_x,cur_y = nx,ny
    if dir == 0:
        grid[r-1-1][c-1+1] = temp
    elif dir == 1 :
        grid[r-1-1][c-1-1] = temp        

rotate(dir)

for row in grid:
    print(*row)