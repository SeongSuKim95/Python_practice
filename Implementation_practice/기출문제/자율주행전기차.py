from collections import deque

n,m,cur_c = list(map(int,input().split()))

# 0 : 도로, 1 : 벽
grid = [
    list(map(int,input().split()))
    for _ in range(n)
]

person_info = {}

dxs,dys = [-1,1,0,0],[0,0,-1,1]

ax,ay = list(map(lambda x : int(x)-1,input().split()))

def can_go(x,y,visited):

    return in_range(x,y) and not grid[x][y] and visited[x][y] == -1

def in_range(x,y):

    return 0 <= x < n and 0 <= y < n 

def print_array(array):

    for row in array:
        print(*row)

for _ in range(m):
    x_s,y_s,x_e,y_e = list(map(lambda x : int(x)-1,input().split()))
    person_info[(x_s,y_s)] = (x_e,y_e)

def find_person(ax,ay):
    visited = [[-1 for _ in range(n)] for _ in range(n)]
    q  = deque()
    
    visited[ax][ay] = 0
    q.append((ax,ay))

    while q:
        cur_x,cur_y = q.popleft()

        for dx,dy in zip(dxs,dys):
            nx,ny = cur_x + dx, cur_y + dy
            if can_go(nx,ny,visited) :
                visited[nx][ny] = visited[cur_x][cur_y] + 1
                q.append((nx,ny))
    
    person_dist = []

    for start,end in person_info.items():
        xs,ys = start
        if visited[xs][ys] == - 1:
            return -1,xs,ys
        person_dist.append((visited[xs][ys],xs,ys))
        
    return sorted(person_dist)[0]

def go_to_end_point(px,py):
    
    ex,ey = person_info[(px,py)]

    visited = [[-1 for _ in range(n)] for _ in range(n)]
    q  = deque()
    
    visited[px][py] = 0
    q.append((px,py))
    arrived = False
    while q and not arrived:
        cur_x,cur_y = q.popleft()
        for dx,dy in zip(dxs,dys):
            nx,ny = cur_x + dx, cur_y + dy
            if can_go(nx,ny,visited) :
                visited[nx][ny] = visited[cur_x][cur_y] + 1
                q.append((nx,ny))
                if (nx,ny) == (ex,ey):
                    arrived = True
                    used_c = visited[nx][ny]
    if arrived:
        return used_c,ex,ey
    else :
        return visited[ex][ey],ex,ey
FAIL = False

while True :
    
    dist,px,py = find_person(ax,ay)
    
    if dist == -1 or cur_c - dist <= 0 :
        FAIL = True
        break
    remain_c = cur_c - dist
    used_c,ex,ey = go_to_end_point(px,py)
    
    if used_c > remain_c or used_c == -1 :
        FAIL = True
        break
    else : # 사용한 연료만큼 재충전
        cur_c = remain_c + used_c
        ax,ay = ex,ey
        person_info.pop((px,py)) # 데려다 줬으니 제거
        if not person_info:
            break

if not FAIL:
    print(cur_c)
else :
    print(-1)