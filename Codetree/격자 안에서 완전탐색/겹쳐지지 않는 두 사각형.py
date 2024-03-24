n,m = list(map(int,input().split()))

grid = [list(map(int,input().split())) for _ in range(n)]

def secondRectangle(visited,first_sum):
    answer = -1e9
    for i in range(n):
        for j in range(m):
            # 첫번째 꼭지점 (i,j)
            for k in range(n):
                for l in range(m):
                    # 두번쨰 꼭지점 (k,l)
                    if i<=k and j<=l :  
                        flag = True
                        for vx in range(i,k+1):
                            for vy in range(j,l+1):
                                if visited[vx][vy] : 
                                    flag = False
                        if flag:
                            second_sum = 0
                            for vx in range(i,k+1):
                                for vy in range(j,l+1):
                                    second_sum += grid[vx][vy]
                            answer = max(answer, first_sum + second_sum)
                        
    return answer
                        
def firstRectangle():
    answer = -1e9
    for i in range(n):
        for j in range(m):
            # 첫번째 꼭지점 (i,j)
            for k in range(n):
                for l in range(m):
                    # 두번째 꼭지점 (k,l):
                    if i <= k and j <= l : 
                        visited = [[0 for _ in range(m)] for _ in range(n)]
                        first_sum = 0
                        for vx in range(i,k+1):
                            for vy in range(j,l+1):
                                visited[vx][vy] = 1
                                first_sum += grid[vx][vy]
                        answer = max(answer,secondRectangle(visited,first_sum))
    return answer
def solve():

    return firstRectangle()


print(solve())
