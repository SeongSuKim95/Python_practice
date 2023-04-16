from collections import deque

N, M = list(map(int,input().split()))

def print_array(array):

    for row in array:
        print(*row)
    print()

grid = [
    list(input())
    for _ in range(N)
]
# print_array(grid)
start,finish = (-1,-1),(-1,-1)
river = []
rain  = []
for i in range(N):
    for j in range(M):
        if grid[i][j] == "W":
            start = (i,j)
        elif grid[i][j] == "*":
            rain.append((i,j))
        elif grid[i][j] == "H":
            finish = (i,j)
        elif grid[i][j] == "X":
            river.append((i,j))

def in_range(x,y):

    return 0<=x<N and 0<=y<M


def bfs():

    dxs,dys = [-1,1,0,0],[0,0,-1,1]
    visited = [
        [False] * M
        for _ in range(N)
    ]
    dist = [
        [0] * M 
        for _ in range(N)
    ]
    for rx,ry in river:
        visited[rx][ry] = True

    # 소나기 확장 시킨 이후,
    q = deque()
    if rain :
        for r in rain :
            visited[r[0]][r[1]] = True
            q.append(r)
    
    hq = deque()
    visited[start[0]][start[1]] = True
    hq.append(start)

    while hq :
        if q :
            cur_level = len(q)
            for _ in range(cur_level):
                cx,cy = q.popleft()
                for dx,dy in zip(dxs,dys):
                    nx,ny = cx+dx,cy+dy
                    if in_range(nx,ny):
                        if not visited[nx][ny] and finish != (nx,ny):
                            visited[nx][ny] = True
                            q.append((nx,ny))
                            
        cur_h = len(hq)
        for _ in range(cur_h):
            hx,hy = hq.popleft()
            for dx,dy in zip(dxs,dys):
                nx,ny = hx+dx, hy+dy
                if in_range(nx,ny):
                    if not visited[nx][ny]:
                        visited[nx][ny] = True
                        dist[nx][ny] = dist[hx][hy] + 1
                        hq.append((nx,ny))


    if not dist[finish[0]][finish[1]]:
        print("FAIL")
    else :
        print(dist[finish[0]][finish[1]])
bfs()
# 문제 조건 제대로 읽기!! 초기 소나기가 여러군데 있을 수 있음!