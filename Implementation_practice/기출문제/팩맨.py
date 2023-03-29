def print_array(array):

    for row in array:
        print(*row)
    print()
m,t = list(map(int,input().split()))

px, py = list(map(lambda x : int(x)-1,input().split()))

cur_grid = [
    [[] for _ in range(4)]
    for _ in range(4)
]

egg_grid = [
    [[] for _ in range(4)]
    for _ in range(4)
]

dead_grid = [
    [0 for _ in range(4)]
    for _ in range(4)
]


# monster initialize

for _ in range(m):
    mr,mc,md = list(map(lambda x : int(x)-1,input().split()))
    cur_grid[mr][mc].append(md)

# packman route

routes = []
for i in range(4):
    for j in range(4):
        for k in range(4):
            routes.append((i,j,k))

def duplicate():

    for i in range(4):
        for j in range(4):
            egg_grid[i][j] = []

    for i in range(4):
        for j in range(4):
            egg_grid[i][j] = cur_grid[i][j][:]

def in_range(x,y):

    return 0<=x<4 and 0<=y<4


def can_go(x,y):

    return not dead_grid[x][y] and (x,y) != (px,py)

def move_monster():
    # 45도 반시계 --> + 1
    m_dirs = [(-1,0),(-1,-1),(0,-1),(1,-1),(1,0),(1,1),(0,1),(-1,1)] 
    
    next_grid = [
        [[] for _ in range(4)]
        for _ in range(4)
    ]

    for i in range(4):
        for j in range(4):
            if cur_grid[i][j]:
                monsters,cur_x,cur_y = cur_grid[i][j],i,j
                for d in monsters:
                    turn_cnt = 0
                    for k in range(8):
                        cur_d = (d + k + 8) % 8
                        dx,dy = m_dirs[cur_d] 
                        nx,ny = cur_x + dx, cur_y + dy
                        if in_range(nx,ny) and can_go(nx,ny):
                            next_grid[nx][ny].append(cur_d)
                            break
                        else :
                            turn_cnt += 1
                    if turn_cnt == 8 :
                        next_grid[cur_x][cur_y].append(d)
    for i in range(4):
        for j in range(4):
            cur_grid[i][j] = next_grid[i][j][:]

def move_packman():              
    global px,py
    
    
    # 상 좌 하 우
    p_dirs = [(-1,0),(0,-1),(1,0),(0,1)]
    
    possible_route = []
    # print(px,py)
    for idx,route in enumerate(routes):
        cur_px,cur_py = px,py
        cur_cnt = 0
        flag = False
        
        temp_grid = [
            [[] for _ in range(4)]
            for _ in range(4)
        ]

        for i in range(4):
            for j in range(4):
                temp_grid[i][j] = cur_grid[i][j][:]

        for cur_dir in route:
            dx , dy = p_dirs[cur_dir]
            cur_px,cur_py = cur_px + dx, cur_py + dy
            if in_range(cur_px,cur_py):
                cur_cnt += len(temp_grid[cur_px][cur_py])
                temp_grid[cur_px][cur_py] = []
            else :
                flag = True
                break
        if not flag:       
            possible_route.append((cur_cnt,-idx,route))

    possible_route.sort(reverse = True)
    # print(possible_route)
    _,_,route = possible_route[0]
    # print(route)
    for d in route:
        dx,dy = p_dirs[d]
        px,py = px + dx , py + dy
        if cur_grid[px][py] :
            cur_grid[px][py] = []
            dead_grid[px][py] = 3
        
def dead_clear():

    for i in range(4):
        for j in range(4):
            if dead_grid[i][j]:
                dead_grid[i][j] -= 1

def new_monster():

    for i in range(4):
        for j in range(4):
            if egg_grid[i][j]:
                for egg in egg_grid[i][j]:
                    cur_grid[i][j].append(egg)

def count_monster():
    ans = 0
    for i in range(4):
        for j in range(4):
            if cur_grid[i][j]:
                ans += len(cur_grid[i][j])
    return ans

def simulate():

    duplicate()
    move_monster()
    move_packman()
    dead_clear()
    new_monster()

for i in range(t):

    simulate()

print(count_monster())