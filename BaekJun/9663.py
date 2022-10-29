
N = int(input())

def check(row):

    for i in range(row):
        if (board[i] == board[row]) or abs(row-i) == abs(board[row]-board[i]):
            return False
    
    return True

def dfs(row):

    global result
    # 종료 조건
    if row == N :
        result += 1
        return
    else:
        for i in range(N):
            board[row] = i
            if check(row):
                dfs(row+1)
                
board = [0] * N
result = 0

dfs(0)
print(result)
