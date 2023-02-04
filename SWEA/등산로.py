N,K = map(int,input().split())

map_ = [list(map(int,input().split())) for _ in range(N)]

dx = [0,0,-1,1]
dy = [-1,1,0,0]
answer = -1e9

def dfs(y,x,depth,map):
    global answer
    cnt = 0 
    for i in range(4):
        ny , nx = y + dy[i], x + dx[i]
        if 0 <= ny < N and 0 <= nx < N and map[ny][nx] < map[y][x]:
            dfs(ny,nx,depth+1,map) 
        else :
            cnt += 1
    if cnt == 4 :
        # print(depth)
        answer = max(answer,depth) 
            
    
def find_max(map):
    max_ = -1e9

    for i in range(N):
        for j in range(N):
            max_ = max(map[i][j],max_)

    max_point = []
    for i in range(N):
        for j in range(N):
            if map[i][j] == max_:
                max_point.append((i,j))
    
    return max_point


for i in range(N):
    for j in range(N):
        for k in range(K+1):
            map_temp = [map_[l][:] for l in range(N)]
            map_temp[i][j] -= k
        
            # Max 값 찾기
            max_points = find_max(map_temp)

            # DFS
            for max_point in max_points:
                max_y,max_x = max_point
                dfs(max_y,max_x,1,map_temp)

