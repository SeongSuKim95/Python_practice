N = int(input())
grid = [list(map(int,input().split())) for _ in range(N)]

curRow,curCol = list(map(lambda x : int(x)-1,input().split()))

def inRange(x,y):
    return 0<=x<N and 0<=y<N

def explosion():
    global grid
    explosionRange = grid[curRow][curCol]
    dxs,dys = [-1,1,0,0],[0,0,-1,1]
    for i in range(explosionRange):
        for dx,dy in zip(dxs,dys):
            nx,ny = curRow+dx*i, curCol+dy*i
            if inRange(nx,ny):
                grid[curRow+dx*i][curCol+dy*i] = 0
    
def gravity():
    global grid
    gridTemp = [[0]*N for _ in range(N)]

    for col in range(N):
        tempIndex = N-1
        for row in range(N-1,-1,-1):
            if grid[row][col] :
                gridTemp[tempIndex][col] = grid[row][col]
                tempIndex -= 1
            else :
                gridTemp[tempIndex][col] = grid[row][col]
    
    grid = [row[:] for row in gridTemp]


def solve():
    global grid
    
    explosion()
    gravity()

    for row in grid:
        print(*row)

solve()