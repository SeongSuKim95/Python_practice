N = int(input())

grid = [list(map(int,input().split())) for _ in range(N)]

visited = [[False] * N for _ in range(N)]

dxs,dys = [-1,1,0,0],[0,0,-1,1]
peopleNum = 1
peopleList = []
def inRange(x,y):

    return 0<=x<N and 0<=y<N

def canGo(x,y):

    return not visited[x][y] and grid[x][y]

def printArr(arr):

    for row in arr:
        print(*row)
    print()

def dfs(cx,cy):
    global peopleNum
    for dx,dy in zip(dxs,dys):
        nx,ny = cx + dx, cy + dy
        if inRange(nx,ny):
            if canGo(nx,ny):
                visited[nx][ny] = True
                peopleNum += 1
                dfs(nx,ny)

for i in range(N):
    for j in range(N):
        if not visited[i][j] and grid[i][j]:
            peopleNum = 1
            visited[i][j] = True
            dfs(i,j)
            peopleList.append(peopleNum)

print(len(peopleList))
for elem in sorted(peopleList):
    print(elem)