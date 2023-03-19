k = int(input())
blocks = [list(map(int,input().split())) for _ in range(k)]

red_grid = [[0 for i in range(6)] for j in range(4)]
yellow_grid = [[0 for i in range(4)] for j in range(6)]
score = 0
def TYPE1(row,col):
    # - 빨간 영역
    # x행에서 0 부터 5 까지 열 순회하여 놓기
    FLAG = False
    for j in range(6): # 좌측에서 부터 스캔
        if red_grid[row][j]:
            red_grid[row][j-1] = 1
            FLAG = True
            break
    if not FLAG : # 아무것도 안놓였다면
        red_grid[row][-1] =  1
    
    # - 노란 영역
    # j열에서 0 부터 5 까지 행 순회하여 놓기
    FLAG = False
    for i in range(6): # 위에서 부터 스캔
        if yellow_grid[i][col]:
            yellow_grid[i-1][col] = 1
            FLAG = True
            break
    if not FLAG :
        yellow_grid[-1][col] = 1
        
def TYPE2(row,col):
    # - 빨간 영역
    # x행에서 0 부터 5 까지 열 순회하여 놓기
    FLAG = False
    for j in range(6): # 좌측에서 부터 스캔
        if red_grid[row][j]:
            red_grid[row][j-1] = 1
            red_grid[row][j-2] = 1
            FLAG = True
            break
    if not FLAG : # 아무것도 안놓였다면
        red_grid[row][-1] = 1
        red_grid[row][-2] = 1

    # - 노란 영역
    # j열에서 0 부터 5 까지 행 순회하여 놓기
    FLAG = False
    for i in range(6): # 위에서 부터 스캔
        if yellow_grid[i][col] or yellow_grid[i][col+1]:
            yellow_grid[i-1][col] = 1
            yellow_grid[i-1][col+1] = 1
            FLAG = True
            break
    if not FLAG :
        yellow_grid[-1][col] = 1
        yellow_grid[-1][col+1] = 1

def TYPE3(row,col):
    # - 빨간 영역
    # x행에서 0 부터 5 까지 열 순회하여 놓기
    FLAG = False
    for j in range(6): # 좌측에서 부터 스캔
        if red_grid[row][j] or red_grid[row+1][j]:
            red_grid[row][j-1] = 1
            red_grid[row+1][j-1] = 1
            FLAG = True
            break
    if not FLAG : # 아무것도 안놓였다면
        red_grid[row][-1] = 1
        red_grid[row+1][-1] = 1

    # - 노란 영역
    # j열에서 0 부터 5 까지 행 순회하여 놓기
    FLAG = False
    for i in range(6): # 위에서 부터 스캔
        if yellow_grid[i][col]:
            yellow_grid[i-1][col] = 1
            yellow_grid[i-2][col] = 1
            FLAG = True
            break
    if not FLAG :
        yellow_grid[-1][col] = 1
        yellow_grid[-2][col] = 1

def red_gravity():
    global score
    temp_grid = [[0 for i in range(6)] for j in range(4)]
    temp_col = 5
    for j in range(5,-1,-1):
        cur_col = []
        for i in range(4):
            cur_col.append(red_grid[i][j])
        if not all([elem == 1 for elem in cur_col]):
            for i in range(4):
                temp_grid[i][temp_col] = cur_col[i]
            temp_col -= 1
        else :
            score += 1
    for i in range(4):
        for j in range(6):
            red_grid[i][j] = temp_grid[i][j]

def yellow_gravity():
    global score
    temp_grid = [[0 for i in range(4)] for j in range(6)]
    temp_row_cnt = 5
    for i in range(5,-1,-1):
        temp_row = yellow_grid[i][:]
        if not all([elem == 1 for elem in temp_row]):
            temp_grid[temp_row_cnt] = temp_row[:]
            temp_row_cnt -= 1
        else:
            score += 1
    for i in range(6):
        for j in range(4):
            yellow_grid[i][j] = temp_grid[i][j]

def print_array(array):
    for row in array:
        print(*row)

def check_red():

    cnt = 0
    # 첫번째 열
    for i in range(4):
        if red_grid[i][0]:
            cnt += 1 
            break
    # 두번째 열
    for i in range(4):
        if red_grid[i][1]:
            cnt += 1
            break

    return cnt

def check_yellow():

    cnt = 0
    # 첫번째 행
    for j in range(4):
        if yellow_grid[0][j]:
            cnt += 1 
            break
    # 두번째 열
    for j in range(4):
        if yellow_grid[1][j]:
            cnt += 1
            break

    return cnt

def shift_right(cnt):

    temp_grid = [[0 for i in range(6)] for j in range(4)]

    for i in range(4):
        for j in range(6-cnt):
            temp_grid[i][j+cnt] = red_grid[i][j]
    
    for i in range(4):
        for j in range(6):
            red_grid[i][j] = temp_grid[i][j] 

def shift_down(cnt):

    temp_grid = [[0 for i in range(4)] for j in range(6)]

    for j in range(4):
        for i in range(6-cnt):
            temp_grid[i+cnt][j] = yellow_grid[i][j] 

    for j in range(4):
        for i in range(6):
            yellow_grid[i][j] = temp_grid[i][j] 

def drop(block):
    t,row,col= block
    # 블록 놓기
    if t == 1 :
        TYPE1(row,col)
    elif t == 2 :
        TYPE2(row,col) 
    elif t == 3 :
        TYPE3(row,col) 

    # 꽉 찬 열 또는 행 확인하고 중력 
    red_gravity()
    yellow_gravity()
    # 5,6번쨰 구간 확인
    red_cnt = check_red()
    if red_cnt :
        shift_right(red_cnt)
    yellow_cnt = check_yellow()
    if yellow_cnt:
        shift_down(yellow_cnt)
    
# red_grid = [
#     [0,0,1,1,0,1],
#     [0,0,1,1,1,1],
#     [0,0,0,1,0,1],
#     [0,0,0,1,1,1],
# ]
# yellow_grid = [
#     [0,0,0,0],
#     [0,0,0,0],
#     [0,0,1,0],
#     [1,1,1,1],
#     [0,1,0,1],
#     [0,1,0,1]
# ]
def calc():
    cnt = 0
    for i in range(4):
        for j in range(6):
            cnt += red_grid[i][j]
    for i in range(6):
        for j in range(4):
            cnt += yellow_grid[i][j]
    return cnt

for block in blocks:
    drop(block)

print(score)
print(calc())