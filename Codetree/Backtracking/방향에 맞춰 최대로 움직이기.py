# 변수 선언 및 입력:
n = int(input())
num = [
    list(map(int, input().split()))
    for _ in range(n)
]
move_dir = [
    list(map(int, input().split()))
    for _ in range(n)
]

answer = 0

def inRange(x,y):
    return 0<=x<n and 0<=y<n

def canGo(nx,ny,curNum):
    return num[nx][ny] > curNum

def move(curR,curC,cnt):
    global answer

    answer = max(answer,cnt)

    dxs = [-1, -1, 0, 1, 1, 1, 0, -1]
    dys = [0, 1, 1, 1, 0, -1, -1, -1]
    
    curDir = move_dir[curR][curC] - 1
    curNum = num[curR][curC]
    for i in range(n):
        nx,ny = curR + i * dxs[curDir], curC + i * dys[curDir]
        if inRange(nx,ny) and canGo(nx,ny,curNum):
            move(nx,ny,cnt+1)

r,c = list(map(lambda x : int(x)-1,input().split()))

move(r,c,0)

print(answer)

