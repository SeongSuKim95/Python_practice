N, M, Q = list(map(int,input().split()))

grid = [list(map(int,input().split())) for _ in range(N)]

# 바람 Q회
winds = [list(map(lambda x : int(x)-1,input().split())) for _ in range(Q)]# 좌상단, 우하단

dxs,dys = [-1,1,0,0], [0,0,-1,1]

def rotate(r1,c1,r2,c2):
    global grid
    gridTemp = [row[:] for row in grid]

    # (r1,c1)  (r1,c2)
    # 
    # (r2,c1)  (r2,c2)
    
    # grid --> gridTemp로 복사
    # 상 : c2-1 ~ c1 감소, r1
    # 우 : r2-1 ~ r1 감소, c2
    # 하 : c1+1 ~ c2 증가, r2
    # 좌 : r1+1 ~ r2 증가, c1

    for i in range(c2-1,c1-1,-1): # r1
        gridTemp[r1][i+1] = grid[r1][i]
    
    for i in range(r2-1,r1-1,-1): # c2
        gridTemp[i+1][c2] = grid[i][c2] 
    
    for i in range(c1+1,c2+1): #r2
        gridTemp[r2][i-1] = grid[r2][i]

    for i in range(r1+1,r2+1): #c1
        gridTemp[i-1][c1] = grid[i][c1] 
                   
    grid = [row[:] for row in gridTemp]

def isValid(x,y):

    return 0 <= x < N and 0 <= y < M 

def getMeanInSquare(r1,c1,r2,c2):

    global grid
    gridTemp = [row[:] for row in grid]

    for curRow in range(r1,r2+1):
        for curCol in range(c1,c2+1):
            
            sumVal,sumCnt = grid[curRow][curCol],1
            
            for dx,dy in zip(dxs,dys):
                newRow, newCol = curRow + dx, curCol + dy
                if isValid(newRow,newCol):
                    sumVal += grid[newRow][newCol]
                    sumCnt += 1
            
            gridTemp[curRow][curCol] = int(sumVal / sumCnt)
    
    grid = [row[:] for row in gridTemp]

def solve():
    global winds
    for r1,c1,r2,c2 in winds:
        rotate(r1,c1,r2,c2)
        getMeanInSquare(r1,c1,r2,c2)


solve()

for row in grid:
    print(*row)