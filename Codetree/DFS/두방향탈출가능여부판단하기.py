N,M = list(map(int,input().split()))

# 뱀이 없는 경우 1, 뱀이 있는 경우 0

grid = [list(map(int,input().split())) for _ in range(N)]

visited = [[False] * M for _ in range(N)]

dxs = [1,0]
dys = [0,1]

def inRange(x,y):

    return 0<=x<N and 0<=y<M

def canGo(x,y):

    return not visited[x][y] and grid[x][y]

def dfs(cx,cy):

    for dx,dy in zip(dxs,dys):
        nx, ny = cx+dx, cy+dy
        if inRange(nx,ny):
            if canGo(nx,ny):
                visited[nx][ny] = True
                dfs(nx,ny)

dfs(0,0)

if visited[N-1][M-1]:
    print(1)
else:
    print(0)

