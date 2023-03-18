grid = [
    [1,2,3,4,5,6,7],
    [8,9,1,2,3,4,5],
    [6,7,8,9,1,2,3],
    [4,5,6,7,8,9,1]
]


start_row, start_col = 0,0

pattern = [6,3,6,3]
dirs = [(0,1),(1,0),(0,-1),(-1,0)]

temp = grid[start_row][start_col]

cur_x,cur_y = start_row,start_col
for (dx,dy),length in zip(dirs,pattern):
    for _ in range(length):
        nx,ny = cur_x + dx, cur_y + dy
        grid[cur_x][cur_y] = grid[nx][ny]
        cur_x,cur_y = nx,ny

grid[start_row+1][start_col] = temp

for row in grid:
    print(*row)