n, m = list(map(int,input().split()))

dxs,dys = [1,0],[0,1]

map_ = [list(map(int,input().split())) for _ in range(n)]

end = (n-1,m-1)
visited = [[False] * m for _ in range(n)]
answer = 0

def in_range(x,y):
    
    return 0<= x < n and 0<= y < m and map_[x][y] and not visited[x][y]


def dfs(x,y):
    global answer

    if (x,y) == end :
        answer = 1
        return

    for dx,dy in zip(dxs,dys):
        nx,ny = x + dx, y + dy
        if in_range(nx,ny):
            visited[nx][ny] = True
            dfs(nx,ny)

visited[0][0] = True
dfs(0,0)
print(answer)