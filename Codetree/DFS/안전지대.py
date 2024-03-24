import sys
sys.setrecursionlimit(2500)
N, M = list(map(int,input().split()))

grid = [list(map(int,input().split())) for _ in range(N)]

dxs,dys = [-1,1,0,0],[0,0,-1,1]
maxHeight = 0
for i in range(N):
    for j in range(M):
        maxHeight = max(maxHeight,grid[i][j])

def canGo(x,y,curHeight):

    return not visited[x][y] and grid[x][y] > curHeight

def inRange(x,y):

    return 0<=x<N and 0<=y<M

def dfs(cx,cy,height):

    for dx,dy in zip(dxs,dys):
        nx,ny = cx+dx,cy+dy
        if inRange(nx,ny):
            if canGo(nx,ny,height):
                visited[nx][ny] = True
                dfs(nx,ny,height)

safeRegions = []

for height in range(1,maxHeight+1):
    visited = [[False] * M for _ in range(N)]
    regionCnt = 0
    for i in range(N):
        for j in range(M):
            if not visited[i][j] and grid[i][j] > height:
                visited[i][j] = True
                dfs(i,j,height)
                regionCnt += 1
    safeRegions.append((height,regionCnt))

safeRegions.sort(key = lambda x : (-x[1],x[0]))
print(*list(safeRegions[0]))