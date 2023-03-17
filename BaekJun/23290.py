# 상어 이동 -> 상하좌우, 격자 제외
# 물고기 이동 -> 8방향, 갈수 있을 때 까지 45도 반시계 회전, 상어/물고기 냄새/ 격자 제외
# 8 방향 
fish_dirs = [(0,-1),(-1,-1),(-1,0),(-1,1),(0,1),(1,1),(1,0),(1,-1)]

# 상어 방향  상 좌 하 우
shark_dirs = [(-1,0),(0,-1),(1,0),(0,1)]

M, S = list(map(int,input().split()))

fish_info = [list(map(lambda x : int(x)-1,input().split())) for _ in range(M)]
shark_pos = tuple(map(lambda x : int(x)-1,input().split()))
grid = [[[] for _ in range(4)] for _ in range(4)]

smell_grid = [[0 for _ in range(4)] for _ in range(4)]

for fish in fish_info :
    fx, fy, fd  = fish
    grid[fx][fy].append(fd)

def print_array(array):
    
    for row in array:
        print(*row)

def in_range(x,y):
    
    return 0<=x<4 and 0<=y<4

combis = []
combi = []

def choose_dir(cnt):
    if cnt == 3:
        combis.append(combi[:]) # global list 내에 list append 시 deepcopy해서 넣자
        return
    
    for i in range(4):
        combi.append(i)
        choose_dir(cnt+1)
        combi.pop()

def fish_can_go(x,y):
    
    return in_range(x,y) and (x,y) != shark_pos and not smell_grid[x][y]

def fish_move():
    
    new_grid = [[[] for _ in range(4)] for _ in range(4)]
    
    for i in range(4):
        for j in range(4):
            if grid[i][j]:
                for fish_dir in grid[i][j]:
                    cur_fx, cur_fy, can_go = i,j,False # Flag 를 통해 움직일 수 있는지 없는지를 판단
                    for k in range(8): # 3 중 루프에서 iterator 변수 설정 조심
                         cur_dir = (fish_dir - k + 8) % 8
                         nfx, nfy = cur_fx + fish_dirs[cur_dir][0], cur_fy + fish_dirs[cur_dir][1]
                        
                         if fish_can_go(nfx,nfy): # 움직였다면 
                             new_grid[nfx][nfy].append(cur_dir)
                             can_go = True
                             break
                    if not can_go: # 이동할 수 없는 상황이라면 그대로 두고, 그 자리에 그대로 저장
                        new_grid[i][j].append(fish_dir)
    return new_grid

def shark_move():
    
    catched_fish = []
    for dir_lst in combis:
        cur_sx, cur_sy = shark_pos
        fish_num, out_of_range = 0, False
        grid_temp = [row[:] for row in grid]
        for dir in dir_lst: 
            nx, ny = cur_sx + shark_dirs[dir][0], cur_sy + shark_dirs[dir][1]
            if not in_range(nx,ny):
                catched_fish.append(-1)
                out_of_range = True
                break
            if grid_temp[nx][ny] :  
                fish_num += len(grid_temp[nx][ny])
                grid_temp[nx][ny] = []
            cur_sx , cur_sy = nx, ny
        if not out_of_range : 
            catched_fish.append(fish_num)
    return catched_fish

def change_shark_pos(lst):
    global shark_pos
    sx,sy = shark_pos
    for dir in lst :
        sx, sy = sx + shark_dirs[dir][0], sy + shark_dirs[dir][1]
        if grid[sx][sy] : 
            smell_grid[sx][sy] = 3 # 3으로 설정하여야 처음 물고기가 먹힌 상황과, 이전 상황에 대한 시간 경과를 한번에 처리 가능
            grid[sx][sy] = []
    shark_pos = (sx,sy)

def copy_fish(grid_temp):
    
    for i in range(4):
        for j in range(4):
            if grid_temp[i][j]:
                
                for fish in grid_temp[i][j]:
                    grid[i][j].append(fish)
    
def smell_vanish():
    
    for i in range(4):
        for j in range(4):
            if smell_grid[i][j] :
                smell_grid[i][j] -= 1

choose_dir(0)

for _ in range(S):
    grid_temp = [row[:] for row in grid]
    grid = fish_move()
    catched_fish = shark_move()
    shark_way = combis[catched_fish.index(max(catched_fish))]
    change_shark_pos(shark_way)
    smell_vanish()
    copy_fish(grid_temp)

result = 0
for i in range(4):
    for j in range(4):
        if grid[i][j]:
            result += len(grid[i][j])

print(result)  

# 3중 루프 이상에서 i,j,k Iterator를 중복으로 써서 실수
# 방향을 돌리다가 갈수 이동 가능하면 가고, 안되면 제자리에 있는다. (안되면 제자리에 있는 경우 고려 x)
# choose_dir 함수에서 이중 리스트 deepcopy

# 상어의 경로를
# 전체 경우의 수 구하지 않고 매번 판단하도록 다시 짜보기