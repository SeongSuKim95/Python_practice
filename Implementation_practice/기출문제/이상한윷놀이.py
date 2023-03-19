
n, k = list(map(int,input().split()))

# 0 : 흰색, 1 : 빨강, 2: 파랑
grid = [list(map(int,input().split())) for _ in range(n)]

# 우 좌 상 하
dirs = [(0,1),(0,-1),(-1,0),(1,0)]

dir_mapper = {
    0 : 1,
    1 : 0,
    2 : 3,
    3 : 2
}

horse = [tuple(map(lambda x : int(x)-1, input().split())) for _ in range(k)]

# 턴 한번 동안 1번 부터 k번 말까지 차례대로 이동

# 흰색칸으로 이동하는 경우
# 말이 없는 경우 : 이동
# 말이 있는 경우 : 기존 말 위에 올려두기

# 빨간색칸으로 이동하는 경우
# 말이 없는 경우 : 이동하기 "전", 이동해야하는 말의 순서를 뒤집은 후에 이동
# 말이 있는 경우 : 순서 뒤집기 + 기존 말 위에 올려두기

# 파란색칸으로 이동하는 경우, 격자 범위 벗어나는 경우

# 방향을 반대로 전환한 뒤 이동 (말이 쌓여있는 경우 해당 말 만 방향 전환)
# 전환 후에도 파란색이 있으면 제자리에!

# 종료 조건
# 말이 4개 이상 겹쳐지는 경우 즉시 종료, 턴의 번호 출력

def in_range(x,y):

    return 0<=x<n and 0<=y<n


def print_array(array):

    for row in array:
        print(*row)

horse_grid = [[[] for _ in range(n)] for _ in range(n)]

for idx,(x,y,dir) in enumerate(horse):
    horse_grid[x][y].append([idx+1,dir]) 
# print_array(horse_grid)

def move_white(idx,cur_num,cur_x,cur_y,nx,ny):

    horse_group = horse_grid[cur_x][cur_y][idx:][:] # 위에 있는말 모두
    
    horse_grid[nx][ny] = horse_grid[nx][ny] + horse_group # 이동

    horse_grid[cur_x][cur_y] = horse_grid[cur_x][cur_y][:idx] 

def move_red(idx,cur_num,cur_x,cur_y,nx,ny):

    horse_group = horse_grid[cur_x][cur_y][idx:][:] # 위에 있는말 모두

    reversed_group = horse_group[::-1] # 뒤집기

    horse_grid[nx][ny] = horse_grid[nx][ny] + reversed_group # 이동

    horse_grid[cur_x][cur_y] = horse_grid[cur_x][cur_y][:idx] # 현재칸 갱신

def move_blue(idx,cur_num,cur_x,cur_y,nx,ny,cur_dir):

    new_dir = dir_mapper[cur_dir]
    horse_grid[cur_x][cur_y][idx] = [cur_num,new_dir]

    nx2,ny2 = cur_x + dirs[new_dir][0], cur_y + dirs[new_dir][1]
    
    if in_range(nx2,ny2) and (grid[nx2][ny2] in [0,1]):
        if grid[nx2][ny2] == 0 :
            move_white(idx,cur_num,cur_x,cur_y,nx2,ny2)
        elif grid[nx2][ny2] == 1:
            move_red(idx,cur_num,cur_x,cur_y,nx2,ny2)

def check_num():
    for i in range(n):
        for j in range(n):
            if len(horse_grid[i][j])>=4 :
                return False
    return True

def simulate():
    turn_cnt = 0 
    while True :
        turn_cnt += 1
        visited = [False for _ in range(k+1)]
        for horse_num in range(1,k+1):
            for i in range(n):
                for j in range(n):

                    if horse_grid[i][j]:
                        for idx,horse_info in enumerate(horse_grid[i][j]):
                            cur_num,cur_dir = horse_info 
                            cur_x,cur_y = i,j   
                            if cur_num == horse_num and not visited[cur_num]: 
                                visited[cur_num] = True
                                nx,ny = cur_x + dirs[cur_dir][0], cur_y + dirs[cur_dir][1]
                                if in_range(nx,ny) and (grid[nx][ny] in [0,1]): # 흰색 or 빨강
                                    if grid[nx][ny] == 0 :
                                        move_white(idx,cur_num,cur_x,cur_y,nx,ny)
                                    elif grid[nx][ny] == 1 :
                                        move_red(idx,cur_num,cur_x,cur_y,nx,ny)
                                else : # out of range or 파랑
                                        move_blue(idx,cur_num,cur_x,cur_y,nx,ny,cur_dir)
                                if not check_num():
                                    return turn_cnt
        if turn_cnt > 1000 :
            return -1

print(simulate())

