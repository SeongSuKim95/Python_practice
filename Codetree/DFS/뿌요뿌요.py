N = int(input())

grid = [list(map(int,input().split())) for _ in range(N)]
visited = [[False] * N for _ in range(N)]
dxs,dys = [-1,1,0,0], [0,0,-1,1]
blockCnt = 1
maxblockCnt = 0
numGroups = 0
def inRange(x,y):
    return 0 <= x < N and 0 <= y < N

def canGo(x,y,v):
    return not visited[x][y] and grid[x][y] == v

def dfs(cx,cy,value):
    global blockCnt
    for dx,dy in zip(dxs,dys):
        nx,ny = cx+dx, cy+dy
        if inRange(nx,ny):
            if canGo(nx,ny,value):
                blockCnt += 1
                visited[nx][ny] = True
                dfs(nx,ny,value)
    return

for i in range(N):
    for j in range(N):
        if not visited[i][j]:
            blockCnt = 1
            visited[i][j] = True
            dfs(i,j,grid[i][j])
            maxblockCnt = max(maxblockCnt,blockCnt)
            if blockCnt >= 4 :
                numGroups += 1
print(numGroups, maxblockCnt)
