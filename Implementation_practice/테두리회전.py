
a = [
    [1,2,3,4,5],
    [6,7,8,9,10],
    [11,12,13,14,15],
    [16,17,18,19,20]
]


def rotate_clock(start_row, start_col, end_row, end_col):
    start_row, start_col, end_row, end_col = start_row - 1, start_col - 1, end_row - 1 , end_col -1 
    temp = a[start_row][start_col]
    # 왼쪽 열
    for row in range(start_row,end_row):
        a[row][start_col] = a[row+1][start_col]
    
    # 아래 행
    for col in range(start_col,end_col):
        a[end_row][col] = a[end_row][col+1]

    # 오른쪽 열
    for row in range(end_row,start_row,-1):
        a[row][end_col] = a[row-1][end_col]

    # 위쪽 행
    for col in range(end_col,start_col,-1):
        a[start_row][col] = a[start_row][col-1]
    
    a[start_row][start_col+1] = temp
    
    for i in range(4):
        for j in range(5):                                                                                                                                                                                                                                                                                                                                                                                                                                                                        
            print(a[i][j],end = " ")
        print()

def rotate_cclock(start_row, start_col, end_row, end_col):
    start_row, start_col, end_row, end_col = start_row - 1, start_col - 1, end_row - 1 , end_col -1 
    temp = a[start_row][start_col]
    
    # 위쪽 행
    for col in range(start_col,end_col):
        a[start_row][col] = a[start_row][col+1]
    
    # 오른쪽 열
    for row in range(start_row,end_row):
        a[row][end_col] = a[row+1][end_col]
    
    # 아래쪽 행
    for col in range(end_col,start_col,-1):
        a[end_row][col] = a[end_row][col-1]
    
    # 왼쪽 열

    for row in range(end_row,start_row,-1):
        a[row][start_col] = a[row-1][start_col]
    
    a[start_row+1][start_col] = temp

    for i in range(4):
        for j in range(5):
            print(a[i][j], end = " ")
        print()
    
rotate_cclock(1,1,3,4)

# 1. 행렬 테두리의 좌측 상단을 소실점으로 잡는다.
# 2. 돌리는 방향에 따라 먼저 shift할 열 or 행을 정한다.
# 3. 차례대로 한칸씩 옮겨주면서 돌린다. 이 떄 for 문의 range를 도착점 기준으로 정하는게 편하다.
# 4. 소실점의 도착지점에 1에서 저장한 값을 넣어준다.