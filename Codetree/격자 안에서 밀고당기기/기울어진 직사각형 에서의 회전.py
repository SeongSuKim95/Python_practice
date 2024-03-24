N = int(input())
grid = [list(map(int,input().split())) for _ in range(N)]

r,c,m1,m2,m3,m4,dir = list(map(int,input().split()))
r,c = r-1,c-1

def rotateCounterClockwise(): # dir 0 : 반시계
    global grid
    gridTemp = [row[:] for row in grid]
    # 4,3,2,1
    dxs,dys = [1,1,-1,-1],[1,-1,-1,1]
    length = [m2,m1,m2,m1]
    
    curRow, curCol = r,c
    for dx,dy,m in zip(dxs,dys,length):
        for _ in range(m):
            gridTemp[curRow][curCol] = grid[curRow-dx][curCol-dy]
            curRow -= dx
            curCol -= dy
    grid = [row[:] for row in gridTemp]

def rotateClockwise(): # dir 1 : 시계
    global grid
    gridTemp = [row[:] for row in grid]
    # 4,3,2,1
    dxs,dys = [1,1,-1,-1],[-1,1,1,-1]
    length = [m1,m2,m1,m2]
    
    curRow, curCol = r,c
    for dx,dy,m in zip(dxs,dys,length):
        for _ in range(m):
            gridTemp[curRow][curCol] = grid[curRow-dx][curCol-dy]
            curRow -= dx
            curCol -= dy
    grid = [row[:] for row in gridTemp]

def solve():
    global grid
    if dir == 0 :
        rotateCounterClockwise()
    else :
        rotateClockwise()

solve()
for row in grid:
    print(*row)
