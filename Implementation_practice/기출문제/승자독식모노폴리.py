# 독점 계약 땅 표기 (땅 주인 번호, 남은 턴 수)
# 현재 플레이어 표기 (땅 주인 번호, 방향)
n,m,k = list(map(int,input().split()))
EMPTY = (0,0)
grid = [
    list(map(int,input().split()))
    for _ in range(n)
]
grid_player = [[(0,0) for _ in range(n)] for _ in range(n)]
grid_land = [[(0,0) for _ in range(n)] for _ in range(n)]

initial_dir = [0] + list(map(lambda x : int(x)-1,input().split()))
# 위 아래 왼 오
dirs = [(-1,0),(1,0),(0,-1),(0,1)]
remain_players = [i for i in range(1,m+1)]
for i in range(n):
    for j in range(n):
        if grid[i][j]:
            player_num = grid[i][j]
            grid_player[i][j] = (player_num,initial_dir[player_num])
            grid_land[i][j] = (player_num,k)

priority = \
[[
    [0,0,0,0],
    [0,0,0,0],
    [0,0,0,0],
    [0,0,0,0]
]]\
+\
[
    [
        list(map(lambda x : int(x)-1,input().split())) for _ in range(4)
    ]
    for _ in range(m)
]

def print_array(array):
    for row in array:
        print(*row)

def in_range(x,y):

    return 0<=x<n and 0<=y<n

def is_empty(x,y):

    return in_range(x,y) and grid_land[x][y] == EMPTY

def is_myland(pnum, x,y):

    return in_range(x,y) and grid_land[x][y][0] == pnum

def move_player(cx,cy,cp,cd):

    dir_priority = priority[cp][cd]
    moved = False
    # 빈땅있는지 확인
    for dir in dir_priority:
        nx,ny = cx + dirs[dir][0], cy + dirs[dir][1]
        if is_empty(nx,ny):
            next_grid_player[nx][ny].append((cp,dir))
            moved = True
            break
    # 내땅있는지 확인
    if not moved :
        for dir in dir_priority:
            nx,ny = cx + dirs[dir][0], cy + dirs[dir][1]
            if is_myland(cp,nx,ny):
                next_grid_player[nx][ny].append((cp,dir))
                break

def remove_players(lst):

    for pnum,_ in lst:
        remain_players.remove(pnum)

def merge_player():

    for i in range(n):
        for j in range(n):
            if next_grid_player[i][j]:
                cur_grid_players = sorted(next_grid_player[i][j][:])
                remove_players(cur_grid_players[1:])
                next_grid_player[i][j] = [cur_grid_players[0]]

def mark_land():
    # grid 초기화
    for i in range(n):
        for j in range(n):
            grid_player[i][j] = EMPTY

    for i in range(n):
        for j in range(n):
            if next_grid_player[i][j]:
                cp,cd = next_grid_player[i][j][0]
                grid_player[i][j] = (cp,cd)
                grid_land[i][j] = (cp,k+1)
    # 시간 경과
    for i in range(n):
        for j in range(n):
            if grid_land[i][j] != EMPTY:
                cp, remain_time = grid_land[i][j]
                grid_land[i][j] = (cp,remain_time-1)
                if remain_time -1 == 0 :
                    grid_land[i][j] = EMPTY

turn = 0
while True :
    turn += 1
    # 모든 player의 다음 위치를 저장할 grid
    next_grid_player = [[[] for _ in range(n)] for _ in range(n)]
    # 매 player마다
    for p_num in range(1,m+1):

        for i in range(n):
            for j in range(n):
                cur_x,cur_y = i,j
                cur_player,cur_dir = grid_player[i][j]
                if p_num == cur_player:
                    move_player(cur_x,cur_y,cur_player,cur_dir)
    
    merge_player()
    mark_land()
    if remain_players == [1]:
        print(turn)
        break
    if turn > 1000 :
        print(-1)
        break