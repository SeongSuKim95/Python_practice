N, M, Q = list(map(int,input().split()))
# 행 열 바람
grid = [list(map(int,input().split())) for _ in range(N)]

winds = [list(map(lambda x : int(x) if x.isdigit() else x,input().split())) for _ in range(Q)]

# 우측 : 1, 좌측 : -1
for idx,(_,dir) in enumerate(winds):
    if dir == "R" : winds[idx][1] = -1
    else : winds[idx][1] = 1

def moveRight(arr):

    rightEnd = arr[-1]
    n = len(arr)
    for i in range(n-1,0,-1):
        arr[i] = arr[i-1]
    arr[0] = rightEnd

    return arr

def moveLeft(arr):

    leftEnd = arr[0]
    n = len(arr)
    for i in range(n-1):
        arr[i] = arr[i+1]
    arr[-1] = leftEnd
    
    return arr 

def moveCurrentRow(rowIdx,dir):
    # print(f"move:{rowIdx},dir : {dir}")
    arr = grid[rowIdx]
    if dir == -1 : arr = moveLeft(arr)
    else : arr = moveRight(arr)
    grid[rowIdx] = arr[:]


def checkDuplicate(arr1,arr2):
    for idx in range(M):
        if arr1[idx] == arr2[idx]:
            return True
    return False

def moveUpperRows(cur_row,cur_dir):
    
    while cur_row > 0 and checkDuplicate(grid[cur_row],grid[cur_row-1]):
        cur_row -= 1
        cur_dir *= -1
        moveCurrentRow(cur_row,cur_dir)
      
def moveLowerRows(cur_row,cur_dir):
    
    while cur_row < N-1 and checkDuplicate(grid[cur_row],grid[cur_row+1]):
        cur_row += 1
        cur_dir *= -1
        moveCurrentRow(cur_row,cur_dir)

def solve():

    for row, dir in winds:
        # 바람 불기
        cur_row, cur_dir = row - 1, dir
        moveCurrentRow(cur_row,cur_dir)
          
        # 위 쪽 행 체크
        moveUpperRows(cur_row,cur_dir)

        # 아래쪽 행 체크
        moveLowerRows(cur_row,cur_dir)

solve()
for row in grid:
    print(*row)