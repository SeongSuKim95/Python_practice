from collections import deque

n, h, m = list(map(int,input().split()))

map_ = [list(map(int,input().split())) for _ in range(n)]

dxs, dys = [-1,1,0,0],[0,0,-1,1]

def in_range(x,y):

    return 0<=x<n and 0<=y<n

def can_go(x,y,visited):

    return not visited[x][y] and map_[x][y] != 1

def bfs():

    q = deque()
    for sx,sy in shelter:
        q.append((sx,sy))
        visited[sx][sy] = 1
   
    while q :
        cur_x,cur_y = q.popleft()
        for dx,dy in zip(dxs,dys):
            nx,ny = cur_x + dx, cur_y + dy
            if in_range(nx,ny) and can_go(nx,ny,visited):
                visited[nx][ny] = visited[cur_x][cur_y] + 1
                q.append((nx,ny))

shelter,people = [], []
visited = [[0] * n for _ in range(n)]
for i in range(n):
    for j in range(n):
        if map_[i][j] == 3 :
            shelter.append((i,j))
        elif map_[i][j] == 2 :
            people.append((i,j))
bfs()
answer = [[0]*n for _ in range(n)]
for i in range(n):
    for j in range(n):
        if map_[i][j] == 2:
            answer[i][j] = visited[i][j] - 1

for row in answer:
    print(*row)