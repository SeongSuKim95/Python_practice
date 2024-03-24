N = int(input())

grid = [list(map(int,input().split())) for _ in range(N)] 

def inRange(x,y):
    return 0<=x<N and 0<=y<N

def explosion(curRow,curCol,grid):
    
    curRange = grid[curRow][curCol]
    dxys= [(-1,0),(1,0),(0,-1),(0,1)]
    for r in range(curRange):
        for dx,dy in dxys:
            if inRange(curRow+r*dx,curCol+r*dy):
                grid[curRow+r*dx][curCol+r*dy] = 0
    return grid

def gravity(grid):
    for col in range(N):
        tmpArr,tmpIdx = [0] * N, N-1
        for row in range(N-1,-1,-1):
            if grid[row][col]:
                tmpArr[tmpIdx] = grid[row][col]
                tmpIdx -= 1
        for row in range(N):
            grid[row][col] = tmpArr[row]
    return grid

def printArray(arr):

    for row in arr:
        print(*row)
    print()

def checkPair(arr):
    cnt = 0
    for row in range(N-1):
        for col in range(N):
            if arr[row][col] and arr[row][col] == arr[row+1][col]:
                cnt += 1
    
    for col in range(N-1):
        for row in range(N):
            if arr[row][col] and arr[row][col] == arr[row][col+1]:
                cnt += 1
    return cnt

answer = 0
for row in range(N):
    for col in range(N):
        gridTemp = [row[:] for row in grid]
        exploded = explosion(row,col,gridTemp)
        gravityed = gravity(exploded)
        answer = max(answer,checkPair(gravityed))
print(answer)

