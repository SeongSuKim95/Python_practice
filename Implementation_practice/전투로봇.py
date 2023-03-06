from collections import deque

N = int(input())

grid = [list(map(int,input().split())) for _ in range(N)]

monster_pos = []
robot_x,robot_y = 0,0
for i in range(N):
    for j in range(N):
        if grid[i][j] == 9:
            robot_x,robot_y,robot_level = i,j,2
            grid[i][j] = 0
        elif 1<= grid[i][j] <=6 :
            monster_pos.append((i,j))


visited = [[-1]* N for _ in range(N)]
total_time = 0

target_exp = 2
current_exp = 0
Flag = True

def in_range(x,y):

    return 0<= x < N and 0<= y < N 

def can_go(x,y):

    return visited[x][y] == -1 and (grid[x][y] <= robot_level)

def initialize():

    for i in range(N):
        for j in range(N):
            visited[i][j] = -1


def bfs():
    global robot_x, robot_y, current_exp, target_exp, robot_level, total_time, Flag
    dxs , dys = [-1,0,0,1], [0,-1,1,0]
    
    initialize()
    
    visited[robot_x][robot_y] = 0
    q = deque()
    q.append((robot_x,robot_y))
    
    if monster_pos :
        monster_x,monster_y = sorted(monster_pos,key = lambda x : grid[x[0]][x[1]])[0]
        if grid[monster_x][monster_y] >= robot_level:
            Flag = False
            return
    else :
        Flag = False
        return
    
    min_dist = 1e9
    catched_monsters = []
    flag = True
    while q and flag:

        cur_x, cur_y = q.popleft()
        for dx,dy in zip(dxs,dys):
            nx ,ny = cur_x + dx, cur_y + dy
            if in_range(nx,ny) and can_go(nx,ny):
                
                visited[nx][ny] = visited[cur_x][cur_y] + 1
                q.append((nx,ny))
                # 타겟 마주치면
                if (nx,ny) in monster_pos and grid[nx][ny] < robot_level:
                    if min_dist >= visited[nx][ny]:
                        catched_monsters.append((nx,ny))
                        min_dist = visited[nx][ny]
                    else :
                        flag = False
                        break
    if catched_monsters:
        catched_monsters.sort(key = lambda x : (x[0],x[1]))
        nx, ny = catched_monsters[0]
        grid[nx][ny] = 0
        monster_pos.remove((nx,ny))
        current_exp += 1
        robot_x,robot_y = nx,ny
        total_time += visited[nx][ny]

        if target_exp == current_exp :
            target_exp += 1
            robot_level += 1
            current_exp = 0
    else :
        Flag = False
    
    return


while Flag:
    bfs()
print(total_time)