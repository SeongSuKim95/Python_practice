N = int(input())

map_ = [list(map(int,input().split())) for _ in range(N)]

# 방향
# 남동, 남서, 북서, 북동 
dxy = [(1, 1), (1, -1), (-1, -1), (-1, 1)]

def dfs(y,x,path,way):
    global i,j,cnt
    
    if y == i and x == j and way == 3:
        cnt = max(cnt,len(path))
        return 
    else :
        if 0 <= x < N and 0<= y < N and (map_[y][x] not in path) :
            new_path = path + [map_[y][x]]
            ny, nx = y + dxy[way][0] , x + dxy[way][1]
            dfs(ny,nx,new_path,way)

            if way < 3: 
                ny,nx = y+dxy[way+1][0] , x + dxy[way+1][1]
                dfs(ny,nx,new_path,way+1)

cnt = -1

for i in range(N):
    for j in range(N):
        dfs(i,j,[],0)
print(cnt)

