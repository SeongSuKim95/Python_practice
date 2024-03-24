n,m = list(map(int,input().split()))

grid = [list(map(int,input().split())) for _ in range(n)]

def getSummation(x1,y1,x2,y2):
    for i in range(x1,x2+1):
        for j in range(y1,y2+1):
            if grid[i][j] <= 0 :
                return -1
    return abs(x2 - x1 + 1) * abs(y2 - y1 + 1)

def solve():

    answer = -1
    for i in range(n):
        for j in range(m):

            for k in range(n):
                for l in range(m):
                    if i <= k and j <= l : 
                        answer = max(answer,getSummation(i,j,k,l))
    return int(answer)

print(solve())

