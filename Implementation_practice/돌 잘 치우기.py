from collections import deque

n, k, m = list(map(int,input().split())) 

map_ = [list(map(int,input().split())) for _ in range(n)]

rocks = []

for i in range(n):
    for j in range(n):
        if map_[i][j] :
            rocks.append((i,j))

starts = [tuple(map(lambda x : int(x)-1 ,input().split())) for _ in range(k)]
dxs , dys = [-1,1,0,0],[0,0,-1,1]
max_cnt = 0

def in_range(x,y):
    return 0<= x < n and 0<= y < n

def can_go(x,y):

    return not visited[x][y] and not map_temp[x][y]

# select rocks

selected_idx = []
combis = []
def choose(idx,cnt):

    if cnt == m :
        combis.append(tuple(selected_idx)) # 이거 list 일때 왜 안되지?
        # 여기서 bfs 돌려주면 되는거 였음!!
        return 
    if idx == len(rocks):
        return

    selected_idx.append(idx)
    choose(idx+1,cnt+1)
    selected_idx.pop()

    choose(idx+1,cnt)

choose(0,0)

def bfs():
    q = deque()
    cnt = 0
    for start in starts:
        x,y = start
        q.append((x,y))
        visited[x][y] = True
        cnt += 1       

    while q:
        cur_x,cur_y = q.popleft()
        for dx,dy in zip(dxs,dys):
            nx, ny = cur_x + dx, cur_y + dy
            if in_range(nx,ny) and can_go(nx,ny):
                visited[nx][ny] = True
                q.append((nx,ny))
                cnt += 1
    return cnt



for combi in combis:
    map_temp = [row[:] for row in map_]
    for idx in combi:
        x,y = rocks[idx]
        map_temp[x][y] = 0
    visited = [[False]* n for _ in range(n)]
    cnt = bfs()
    max_cnt = max(max_cnt,cnt)

print(max_cnt)