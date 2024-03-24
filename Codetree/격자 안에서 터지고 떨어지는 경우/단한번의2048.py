grid = [list(map(int,input().split())) for _ in range(4)]
dir = input()


def gravity(): # Down 기준으로 작성

    global grid
    
    nextGrid = [[0]*4 for _ in range(4)]
    for col in range(4):
        tempIndex = 3
        for row in range(3,-1,-1):
            if grid[row][col]:
                nextGrid[tempIndex][col] = grid[row][col]
                tempIndex -= 1
    grid = [row[:] for row in nextGrid]

def rotateCounterClock():
    global grid
    nextGrid = [[0]*4 for _ in range(4)]

    for i in range(4):
        for j in range(4):
            nextGrid[i][j] = grid[j][3-i]
    
    grid = [row[:] for row in nextGrid]

def rotateClock():
    global grid
    nextGrid = [[0]*4 for _ in range(4)]

    for i in range(4):
        for j in range(4):
            nextGrid[i][j] = grid[3-j][i]
    
    grid = [row[:] for row in nextGrid]


def explosion():
    global grid

    nextGrid = [[0]*4 for _ in range(4)]
    for col in range(4):
        curIndex, tempIndex = 3 , 3
        while curIndex >= 0 and tempIndex >= 0:
            if curIndex == 0 :
                nextGrid[tempIndex][col] = grid[curIndex][col] 
                break

            if grid[curIndex][col] == grid[curIndex-1][col]:
                nextGrid[tempIndex][col] = grid[curIndex][col] * 2
                curIndex -= 2

            else:
                nextGrid[tempIndex][col] = grid[curIndex][col] 
                curIndex -= 1
                
            tempIndex -= 1
    
    grid = [row[:] for row in nextGrid]

def printArray():
    global grid
    for row in grid:
        print(*row)
    print()

def solve(dir):

    if dir == "R":
        rotateClock()
        gravity()
        explosion()
        rotateCounterClock()
    elif dir == "D":
        gravity()
        explosion()
    elif dir == "U":
        rotateClock()
        rotateClock()
        gravity()
        explosion()
        rotateCounterClock()
        rotateCounterClock()
    elif dir == "L":
        rotateCounterClock()
        gravity()
        explosion()
        rotateClock()

    printArray()

solve(dir)

