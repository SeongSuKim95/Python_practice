""" 
어른 상어
"""

# 상 하 좌 우 
_dirlist = [[0,0],[-1,0],[1,0],[0,-1],[0,1]]

N,M,K = map(int,input().split())

_map = [list(map(int,input().split())) for _ in range(N)]

shark_list = [[] for _ in range(M+1)]

# 상어의 좌표 받기
for row in range(N):
    for col in range(N):
        if _map[row][col] != 0 :
            shark_list[_map[row][col]].append([row,col])

sdir_list = list(map(int,input().split()))

for i in range(1,M+1):
    shark_list[i].append(sdir_list[i-1])

# print(shark_list)
shark_prior = {}
for i in range(1,M+1):
    shark_prior[i] = [0]
    for j in range(1,5):
        shark_prior[i].append(list(map(int,input().split())))
"""        
 필요한 것
 
 1.현재 상어들의 상태를 나타내는 list (좌표, 방향)    
 2.상어 냄새 번호와 남은 초수
"""

# 초기 상태 냄새 기록
# 상어 번호와 , 남은 초 수 

smell_map = [[[0,0] for _ in range(N)] for _ in range(N)]
# print(smell_map)

for i in range(1,M+1):
    # row , col
    smell_map[shark_list[i][0][0]][shark_list[i][0][1]][0] = i
    smell_map[shark_list[i][0][0]][shark_list[i][0][1]][1] = K

# 살아 있는 상어의 수
remain_shark = M
# 이동 수
ans = 0
# 현재 상어위치 기록 (냄새 기록을 위한 위치) buffer 역할
current_loc_shark = [[0,0]] * (M+1)

def empty_check(smell_map,shark_idx):

    current_shark_loc = shark_list[shark_idx][0]
    current_shark_dir = shark_list[shark_idx][1]
    cur_prior = shark_prior[shark_idx][current_shark_dir]
    
    # prior direction 순서대로 
    for dir in cur_prior:
        x, y = current_shark_loc[0] + _dirlist[dir][0], current_shark_loc[1] + _dirlist[dir][1]

        if 0<= x < N and 0<= y < N:
            if smell_map[x][y][0] == 0 : # 빈칸이면
                return [x,y,dir] # 이동한 위치, 방향
    return False

def smell_check(smell_map,shark_idx):

    current_shark_loc = shark_list[shark_idx][0]
    current_shark_dir = shark_list[shark_idx][1]
    cur_prior = shark_prior[shark_idx][current_shark_dir]

    for dir in cur_prior:
        x,y = current_shark_loc[0]+_dirlist[dir][0],current_shark_loc[1]+_dirlist[dir][1]
        
        if 0<=x< N and 0<=y<N:
            if smell_map[x][y][0] == shark_idx:
                return [x,y,dir]

def check_shark_dead():
    # 겹치는 상어가 있는지 확인하는 작업
    dead_num = 0
    for i in range(1,M):
        if shark_list[i][0] == -1: # 죽은 상어
            continue
        for j in range(i+1,M+1):

            if shark_list[j][0] == -1: # 죽은 상어
                continue
            if shark_list[i][0] == shark_list[j][0]: #위치가 겹치면 큰 값이 죽음
                shark_list[j][0] = -1
                dead_num += 1
    return dead_num

while remain_shark > 1 and ans < 1001:
    # 상어 움직임
    for i in range(1,M+1): # 각 상어에 대해
        if shark_list[i][0] == -1 : # 죽으면 -1로 표기
            continue

        current_loc = shark_list[i][0]
        current_loc_shark[i] = current_loc # 미리 저장
        
        empty_move = empty_check(smell_map,i)

        # 갈 수 있으면 바뀐 위치와 방향 [x,y,dir], 갈 수 없으면 False

        if empty_move: #갈 수 있으면 상어 위치 update
            new_sx,new_sy,new_dir = empty_move[0],empty_move[1],empty_move[2]
            shark_list[i][0][0], shark_list[i][0][1] = new_sx, new_sy
            shark_list[i][1] = new_dir
        else: # 갈 수 없으면 내 냄새 찾기
            # 비어있는 곳 없을 때 자신의 냄새 있는 곳 탐색
            smell_move = smell_check(smell_map,i)
            new_sx,new_sy,new_dir = smell_move[0],smell_move[1],smell_move[2]
            shark_list[i][0][0], shark_list[i][0][1] = new_sx, new_sy
            shark_list[i][1] = new_dir
        
    # 죽은 상어 있는지 확인
    dead_num = check_shark_dead()
    remain_shark -= dead_num # 남은 상어를 세는것과 1번 상어만 남는 것이 동치이다.

    for row in range(N):
        for col in range(N):
            if smell_map[row][col][0] != 0 : # 냄새 업데이트 1씩 빼줌
                smell_map[row][col][1] -= 1
            
            if smell_map[row][col][1] == 0 : # 냄새가 다 사라지면 할당 상어 없애기
                smell_map[row][col][0] = 0
    

    # 다음 위치에 대한 정보를 list로 넘기고 현재 위치에 대한 냄새를 loop의 끝에서 update한다.
    # 현재 위치 기준으로 냄새 생성
    
    for i in range(1,M+1):
        if shark_list[i][0] != -1 : # 상어가 죽지 않았다면
            x,y = current_loc_shark[i][0],current_loc_shark[i][1]
            smell_map[x][y] = [i,K]
    
    ans += 1

if ans > 1000:
    print(-1)
else:
    print(ans)



