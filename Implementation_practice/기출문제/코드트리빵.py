from collections import deque

n,m = list(map(int,input().split()))

def print_array(array):

    for row in array:
        print(*row)
    print()

EMPTY = 0
BASECAMP = 100

grid = [
    list(map(int,input().split()))
    for _ in range(n)
]

for i in range(n):
    for j in range(n):
        if grid[i][j] == 1 :
            grid[i][j] = BASECAMP

store_pos = {i:(0,0) for i in range(1,m+1)}
person_pos = {i:(-1,-1) for i in range(1,m+1)}

pre_visited = [[False for _ in range(n)] for _ in range(n)]
moving = []

for pnum in range(1,m+1):
    x,y = list(map(lambda x : int(x)-1,input().split()))
    grid[x][y] = pnum
    store_pos[pnum] = (x,y)

def in_range(x,y):

    return 0<=x<n and 0<=y<n

def can_go(x,y):

    return not pre_visited[x][y] 

def find_base(x,y):

    dxs,dys = [-1,1,0,0],[0,0,-1,1]
    sx,sy = x,y 
    cur_visited = [row[:] for row in pre_visited]
    
    q = deque()
    cur_visited[sx][sy] = True

    dist = [
        [0 for _ in range(n)]
        for _ in range(n)
    ]

    q.append((sx,sy))
    bases = []
    while q :
        cx,cy = q.popleft()
        for dx,dy in zip(dxs,dys):
            nx, ny = cx + dx, cy + dy
            if in_range(nx,ny) and not cur_visited[nx][ny] :
                cur_visited[nx][ny] = True
                dist[nx][ny] = dist[cx][cy] + 1
                q.append((nx,ny))
                if grid[nx][ny] == BASECAMP and not pre_visited[nx][ny]:
                    bases.append((dist[nx][ny],nx,ny))
    bases.sort()
    cur_dist,base_x,base_y = bases[0]
    # 들어간 거 표시
    pre_visited[base_x][base_y] = True
        
    return base_x,base_y


def move(): # 각자 최단거리로 이동하는데, 상좌우하의 우선순위로 이동
    global moving
    move_dir = [(-1,0),(0,-1),(0,1),(1,0)]
    next_moving = moving[:]
    for cur_p in moving :
        px,py = person_pos[cur_p]
        p_temp = [row[:] for row in pre_visited]
        q = deque()
        p_temp[px][py] = True
        p_dist = [
            [0 for _ in range(n)]
            for _ in range(n)
        ] 
        q.append((px,py,""))

        dest_x,dest_y = store_pos[cur_p]
        routes = None
        while q : 

            cur_x,cur_y,cur_r = q.popleft()
            for idx,d in enumerate(move_dir) :
                dx,dy = d
                nx,ny = cur_x + dx, cur_y + dy
                if in_range(nx,ny) and not p_temp[nx][ny]:
                    p_dist[nx][ny] = p_dist[cur_x][cur_y] + 1
                    p_temp[nx][ny] = True
                    if (nx,ny) == (dest_x,dest_y):
                        routes = cur_r+str(idx)
                        break
                    else:
                        p_temp[nx][ny] = True
                        q.append((nx,ny,cur_r + str(idx)))
        min_route = routes
        # 도착
        if len(min_route) == 1 :
            pre_visited[dest_x][dest_y] = True
            person_pos[cur_p] = (dest_x,dest_y)
            next_moving.remove(cur_p)
        else :
            next_dir = int(min_route[0])
            dx,dy = move_dir[next_dir]
            next_x,next_y = px+dx,py+dy
            person_pos[cur_p] = (next_x,next_y)
        moving = next_moving[:]

def simulate():
    global moving
    t = 0
    while True :
        t += 1
        if t <= m :
            sx,sy = store_pos[t] # t번 사람이 가고 싶은 store
            tx,ty = find_base(sx,sy) # t번 사람이 들어가는 베이스 캠프
            person_pos[t] = (tx,ty)
            move()
            moving.append(t)
        else :
            if moving :
                move()
            else:
                break
    print(t-1)

simulate()
        



