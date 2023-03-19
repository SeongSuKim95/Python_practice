n,m,q = list(map(int,input().split()))

grid = [
    list(map(int,input().split()))
    for _ in range(n)
]

# turn 정보 : x, d, k
turns = [
    list(map(int,input().split())) 
    for _ in range(q)
]

NONE = -1
# 구현해야하는것

# 1. 원판 돌리기
# 2. 인접 수 지우기
# 3. 정규화 치환하기
# 4. 지운 수 있는지 확인하기

# NONE = -1

# n : 원판 개수, m : 원판 내 숫자 개수 , q  : 회전 횟수

# x의 배수인 경우의 원판만 회전
# 1. 원판 돌리기
# 시계방향 : 마지막 원소 빼서 맨 앞으로
# 5 2 3 4  --> 4 5 2 3
# 반시계방향 : 첫번째 원소 빼서 맨 뒤로
# 5 2 3 4  --> 2 3 4 5

# 2. 인접 수 지우기
# 열 인접 : 첫번째 열을 맨 뒤에 추가후 i 번째가 i+1번째랑 같은지 확인 
# 5 2 3 5 5
# 5 2 1 1 5
# 5 7 4 4 5
# 2 6 3 6 2
# 행 인접 : i 번째가 i+1번째랑 같은지 확인

def print_array(array):
    for row in array:
        print(*row)

def shift_right(lst): # 무결

    temp = lst[:]
    end = temp[-1]

    return [end] + temp[:-1]

def shift_left(lst): # 무결
    
    temp = lst[:]
    start = temp[0]

    return temp[1:] + [start]

def check_empty():

    for i in range(n):
        for j in range(m):
            if grid[i][j] != NONE :
                return False
    return True

def turn_table(turn): # 맞음

    x,d,k = turn
    for table_num in range(1,n+1):
        if not table_num % x : # 배수만 원판 돌리기 
            if d == 0 : # 시계
                for _ in range(k):
                    temp = grid[table_num-1][:]
                    temp = shift_right(temp)
                    grid[table_num-1] = temp[:]
            elif d == 1 : # 반 시계
                for _ in range(k):
                    temp = grid[table_num-1][:]
                    temp = shift_left(temp)
                    grid[table_num-1] = temp[:]

def delete(check):

    for i in range(n):
        for j in range(m):
            if check[i][j] :
                grid[i][j] = NONE


def check_adjacent():

    check = [
        [False for i in range(m)]
        for j in range(n)
    ]
    
    Flag = False
    
    # 행 인접 
    for i in range(n-1):
        for j in range(m):
            if grid[i][j] == grid[i+1][j] and grid[i][j]!= NONE:
                check[i][j] = True
                check[i+1][j] = True
                Flag = True

    # 열 인접

    for i in range(n):
        for j in range(m):
            # 마지막 열
            if j == m-1 :
                if grid[i][j] == grid[i][0] and grid[i][j]!= NONE:
                    check[i][j] = True
                    check[i][0] = True
                    Flag = True
            else:
                if grid[i][j] == grid[i][j+1] and grid[i][j]!= NONE: # 지우고 난 이후 중복 처리!
                    check[i][j] = True
                    check[i][j+1] = True
                    Flag = True
    if Flag :
        delete(check)
    # print_array(check)
    return Flag

def normalize():

    grid_sum = 0
    cnt = 0
    for i in range(n):
        for j in range(m):    
            if grid[i][j] is not NONE :
                grid_sum += grid[i][j]
                cnt += 1
    if not cnt : # 원판에 수가 없으면
        return
    
    mean = grid_sum // cnt
    for i in range(n):
        for j in range(m):
            cur_num = grid[i][j]
            if cur_num is not NONE:
                if cur_num > mean :
                    grid[i][j] = cur_num - 1
                elif cur_num < mean : 
                    grid[i][j] = cur_num + 1
def calc_sum():
    result = 0
    # print_array(grid)
    for i in range(n):
        for j in range(m):
            if grid[i][j] is not NONE :
                result += grid[i][j]
    return result

# check_adjacent()
for turn in turns :
    turn_table(turn)
    if check_empty():
        break
    flag = check_adjacent() # 지워지는 수 있으면 True
    if not flag : # 지워지는 수 없으면
        normalize()

print(calc_sum())