# 포인트 : 순차적으로 일어나는 연산인지, 각 원소에 대해 독립적으로 동시에 일어나는 연산인지를 파악해야함.
# 독립적으로 일어나는 경우 array의 copy본을 하나 만든 후, 여기서 연산 후에 넣어줘야 한다.
# smart하게 짜보자.

a = [
    [1,2,3,4,5],
    [6,7,8,9,10],
    [11,12,13,14,15],
    [16,17,18,19,20]
]

start_row, end_row, start_col, end_col = 0, 3, 0, 4
dy,dx = [-1,1,0,0,0],[0,0,-1,1,0]

temp = [row[:] for row in a]

def in_range(x,y):

    return 0<= x < 4 and 0<= y < 5

def average(x, y):
    # 자기 자신의 위치를 포함하여 평균을 내야 하므로
    # dx, dy 방향을 5개로 설정하면 한 번에 처리가 가능합니다.
    dxs, dys = [0, 1, -1, 0, 0], [0, 0, 0, 1, -1]
    
    active_numbers = [temp[x+dx][y+dy] for dx,dy in zip(dxs,dys) if in_range(x+dx,y+dy)]
    
    return sum(active_numbers) // len(active_numbers)

for i in range(start_row,end_row+1):
    for j in range(start_col,end_col+1):

        a[i][j] = average(i,j)

print(a)