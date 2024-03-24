n = int(input())

grid = [list(map(int,input().split())) for _ in range(n)]

def isArray(y,x):

    return 0<=x<n and 0<=y<n

def findPath(cx,cy,k,l):
    dxs,dys = [-1,-1,1,1],[1,-1,-1,1]
    # 0 : 우상, 1 : 좌상, 2: 좌하, 3: 우하
    move_nums = [k,l,k,l]
    cost = 0
    for dx,dy,move_num in zip(dxs,dys,move_nums):
        for _ in range(move_num):
            cx,cy = cx + dx, cy + dy
            if isArray(cx,cy):
                cost += grid[cx][cy]
            else :
                return 0
    return cost

def solve():
    answer = 0
    for i in range(n):
        for j in range(n):
            
            for k in range(1,n):
                for l in range(1,n):
                    answer = max(answer,findPath(i,j,k,l))
    return answer

print(solve())