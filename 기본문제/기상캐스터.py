N, M = list(map(int,input().split()))

def print_array(array):
    for row in array:
        print(*row)
    print()
grid = [
    list(input())
    for _ in range(N)
]

answer = [
    [-1 for _ in range(M)]
    for _ in range(N)
]


for i in range(N):
    for j in range(M):
        cur_x,cur_y = i,j
        cnt = 0
        for k in range(j,-1,-1):
            if grid[i][k] == "c":
                answer[i][j] = cnt  
                break
            else :
                cnt += 1

print_array(answer)