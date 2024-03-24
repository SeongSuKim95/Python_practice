n,m = list(map(int,input().split()))

grid = [list(map(int,input().split())) for _ in range(n)]

def isValid(x,y):

    return 0<=x<n and 0<=y<n

def isInRange(cur_x,cur_y,dist_x,dist_y,th):
       return abs(dist_x - cur_x) + abs(dist_y - cur_y) <= th 

def checkGold(x,y):

    return grid[x][y] == 1

def findCost(cur_x,cur_y,cur_range):
    gold_cnt = 0
    cost = cur_range ** 2 + (cur_range + 1) ** 2
    # 매번 N X N 완탐
    for dist_x in range(n):
        for dist_y in range(n):
            if isInRange(cur_x,cur_y,dist_x,dist_y,cur_range) and checkGold(dist_x,dist_y):
                gold_cnt += 1
    return (gold_cnt * m - cost, gold_cnt)

def solve():
    answer = 0 # 초기화 값 0 
    for i in range(n):
        for j in range(n):
            for cur_range in range(2*(n-1)+1):
                cost, gold_cnt = findCost(i,j,cur_range)
                if cost >= 0 :
                    # print(i,j,cur_range,gold_cnt)
                    answer = max(answer, gold_cnt)
    
    return answer

print(solve())
