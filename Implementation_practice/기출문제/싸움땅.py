n,m,k = list(map(int,input().split()))

def print_array(array):

    for row in array:
        print(*row)

gun_grid = [
    list(map(lambda x : [int(x)] if int(x) else [], input().split()))
    for _ in range(n)
]

# 상 우 하 좌
dirs = [(-1,0),(0,1),(1,0),(0,-1)]

player_grid = [
    [[] for _ in range(n)]
    for _ in range(n)
]

player_pos = {i:(0,0) for i in range(1,m+1)}
player_score = {i: 0 for i in range(1,m+1)}

for p_num in range(1,m+1):
    x,y,d,s = list(map(int,input().split()))
    player_grid[x-1][y-1].append((p_num,s,0,d))
    player_pos[p_num] = (x-1,y-1)

def in_range(x,y):

    return 0<=x<n and 0<=y<n


def move_player(pnum):

    px,py = player_pos[pnum]
    pnum,ps,pg,pd  = player_grid[px][py][0]
    
    dx,dy = dirs[pd]

    nx,ny = px + dx, py + dy
    
    if in_range(nx,ny):

        player_grid[px][py].remove((pnum,ps,pg,pd))
        player_grid[nx][ny].append((pnum,ps,pg,pd))
        pass
    else :
        player_grid[px][py].remove((pnum,ps,pg,pd))
        pd = (pd + 2 + 4) % 4
        dx,dy = dirs[pd]
        nx,ny = px + dx, py + dy
        player_grid[nx][ny].append((pnum,ps,pg,pd))
    
    player_pos[pnum] = (nx,ny)

    return nx,ny 

def not_player(x,y):

    return len(player_grid[x][y]) != 2

def gun_exist(x,y):

    return gun_grid[x][y] != []

def get_gun(x,y,idx): # gun을 집는 행위만!
    
    pnum,ps,pg,pd = player_grid[x][y][idx]
    gun_list = gun_grid[x][y]
    # player가 무기가 있으면
    if gun_list :
        if pg :
            gun_temp = gun_list[:] + [pg]
        else :
            gun_temp = gun_list[:]
        max_gun = max(gun_temp)
        gun_temp.remove(max_gun)

        gun_grid[x][y] = gun_temp[:]
        player_grid[x][y][idx] = (pnum,ps,max_gun,pd)
    
def can_go(x,y):

    return player_grid[x][y] == []

def throw_gun(x,y,idx): # gun을 버리는 행위만!
    # idx 0 --> old
    # idx 1 --> new
    cnum,cs,cg,cd = player_grid[x][y][idx]
    if cg:
        gun_grid[x][y].append(cg)
        cg = 0
    else:
        pass
    player_grid[x][y][idx] = (cnum,cs,cg,cd)

def loser_move(x,y,idx):

    cnum,cs,cg,cd = player_grid[x][y][idx]
    td = cd
    for i in range(4):
        cd = (td + i + 4) % 4
        dx,dy = dirs[cd]
        nx,ny = x + dx, y + dy
        if in_range(nx,ny) and can_go(nx,ny):
            player_grid[nx][ny].append((cnum,cs,cg,cd))
            player_grid[x][y].remove((cnum,cs,cg,td))
            player_pos[cnum] = (nx,ny)
            break

    get_gun(nx,ny,0) # 한명 밖에 없는 상황

def fight_player(x,y):

    old_player, new_player = player_grid[x][y] # old 0, new 1

    onum,os,og,od = old_player
    nnum,ns,ng,nd = new_player
    old_stat, new_stat = (os + og, os), (ns + ng, ns)

    if old_stat > new_stat :
    
        player_score[onum] += old_stat[0] - new_stat[0]
        throw_gun(x,y,1)
        loser_move(x,y,1)
        get_gun(x,y,0) # 한명 밖에 없는 상황
    
    elif new_stat > old_stat:
        
        player_score[nnum] += new_stat[0] - old_stat[0]
        throw_gun(x,y,0)
        loser_move(x,y,0)
        get_gun(x,y,0) # 한명 밖에 없는 상황


def simulate():

    for turn in range(k):
        for cur_player in range(1,m+1):
            nx,ny = move_player(cur_player)
            if not_player(nx,ny):
                get_gun(nx,ny,0)
                    
            else : # 사람 있으면
                fight_player(nx,ny)

simulate()
print(*list(player_score.values()))