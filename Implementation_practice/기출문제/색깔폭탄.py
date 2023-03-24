from collections import deque

# n,m = list(map(int,input().split()))

ROCK = -1
RED = 0
EMPTY = -2
# 1 ~ m
# 빨강 포함일 경우 색 딱 두개만, 같은 색상끼리만

# 중력

# 90도 회전

# 중력

# grid = [
#     list(map(int,input().split()))
#     for _ in range(n)
# ]

n,m = 6,2
grid = [
    [0,-1,2,2,1,1],
    [0,0,2,2,1,1],
    [-1,1,1,1,1,1],
    [0,0,0,0,2,2],
    [1,2,-1,1,-1,1],
    [2,1,-1,0,2,0]
    
]

score = 0


def in_range(x,y):

    return 0<=x<n and 0<=y<n

def group_bomb():

    visited = [[False for _ in range(n)] for _ in range(n)]
    dxs,dys = [-1,1,0,0],[0,0,-1,1]
    groups = []
    red_cnts = []
    bomb_cnts = []
    print("####################")
    for i in range(n):
        for j in range(n):
            if grid[i][j] != ROCK and not visited[i][j] and grid[i][j] != RED and grid[i][j] != EMPTY:

                q = deque()
                cur_color = grid[i][j]
                cur_group = []
                
                visited[i][j] = True
                q.append((i,j)) # 색, x, y
                cur_group.append((cur_color,i,j))
                red_cnt = 0
                red_group = []
                while q:
                    cur_x,cur_y = q.popleft()
                    for dx,dy in zip(dxs,dys):
                        nx,ny = cur_x + dx, cur_y + dy
                        if in_range(nx,ny) and grid[nx][ny] != ROCK and not visited[nx][ny] and grid[i][j] != EMPTY:
                            if grid[nx][ny] == cur_color:
                                visited[nx][ny] = True
                                q.append((nx,ny))
                                cur_group.append((cur_color,nx,ny))
                            elif grid[nx][ny] == RED:
                                visited[nx][ny] = True
                                q.append((nx,ny))
                                cur_group.append((RED,nx,ny))
                                red_cnt += 1
                                red_group.append((nx,ny))
                groups.append(cur_group[:])  
                red_cnts.append(red_cnt)
                bomb_cnts.append(-len(cur_group[:]))              
                for rx,ry in red_group:
                    visited[rx][ry] = False
    return list(zip(bomb_cnts,red_cnts,groups))

def check_group(group_infos,max_bomb,min_red):

    max_bomb_idx, min_red_idx = [],[]
    
    for idx,(bomb_cnt,red_cnt,group) in enumerate(group_infos):
        if bomb_cnt == max_bomb:
            max_bomb_idx.append(idx)
    
    if len(max_bomb_idx) == 1 :

        return True, max_bomb_idx[0]

    else :
        for cur_idx in max_bomb_idx :
            _,red_cnt,_ = group_infos[cur_idx]
            if red_cnt == min_red :
                min_red_idx.append(cur_idx)

        if len(min_red_idx) == 1 :

            return True, min_red_idx[0]

        else :


            return False, min_red_idx
            

def get_explosion_lst():

    group_infos = group_bomb()
    # print(group_infos)
    # zip(red_cnts,groups)
    if not group_infos:
        return [(0,0)] 

    min_group = sorted(group_infos)[0]
    
    max_bomb_cnt, min_red_cnt = min_group[0],min_group[1]

    Flag, check_idx = check_group(group_infos,max_bomb_cnt,min_red_cnt)

    if Flag:
        return group_infos[check_idx][2]
    
    else :
        new_groups = []
        for idx in check_idx:    
            _,_,group = group_infos[idx]
            group_temp = []
            for color,x,y in group:
                if color :
                    group_temp.append((-x,y))
            bx, by = sorted(group_temp)[0]
            new_groups.append((bx,by,idx))

        _,_,final_idx = sorted(new_groups)[0]

        bomb_lst = group_infos[final_idx][2]

        return bomb_lst

def print_array(array):

    for row in array:
        print(*row)

def explosion(lst):
    global score
    for _,x,y in lst :
        grid[x][y] = EMPTY
    score += len(lst)**2

def rotate():

    new_grid = [[-2 for _ in range(n)] for _ in range(n)]
    for i in range(n):
        for j in range(n):
            new_grid[n-1-j][i] = grid[i][j]

    for i in range(n):
        for j in range(n):
            grid[i][j] = new_grid[i][j]

def gravity():

    for j in range(n):
        cur_col = []
        for i in range(n):
            cur_col.append(grid[i][j])
        
        temp_cnt = n-1
        new_col = [EMPTY for _ in range(n)]
        for k in range(n-1,-1,-1):
            if cur_col[k] == EMPTY:
                continue
            elif cur_col[k] == ROCK:
                temp_cnt = k-1
                new_col[k] = ROCK
            else :
                new_col[temp_cnt] = cur_col[k]
                temp_cnt -= 1
        for k in range(n):
            grid[k][j] = new_col[k] 

while True :
    lst = get_explosion_lst()
    if len(lst) == 1 :
        break
    explosion(lst)

    gravity()
    rotate()
    gravity()


print(score)