N = int(input())

NONE = -1

grid = [
    list(map(int,input().split()))
    for _ in range(N)
]
# direction : 0-> D, 1-> R, 2-> U, 3-> L 


def rotate(): # 한번 돌리기

    # next_grid 초기화
    next_grid = [
        [0 for _ in range(N)]
        for _ in range(N)
        ]
    
    for i in range(N):
        for j in range(N):
            next_grid[i][j] = grid[j][N-1-i]

    for i in range(N):
        for j in range(N):
            grid[i][j] = next_grid[i][j]
    
def drop():
    next_grid = [
        [0 for _ in range(N)]
        for _ in range(N)
        ]
    
    for j in range(N):
        
        keep_num, next_row = NONE, N-1

        for i in range(N-1,-1,-1): # 아래 방향으로 드랍 
            # 비어 있으면 pass
            if not grid[i][j]:
                continue

            if keep_num == NONE :
                keep_num = grid[i][j]
            
            elif keep_num == grid[i][j]:

                next_grid[next_row][j] = keep_num * 2
                keep_num = NONE
                next_row -= 1

            else :
                
                next_grid[next_row][j] = keep_num
                keep_num = grid[i][j]
                next_row -= 1
        
        if keep_num != NONE:
            
            next_grid[next_row][j] = keep_num
    
    for i in range(N):
        for j in range(N):

            grid[i][j] = next_grid[i][j]
    
def print_array(map_):

    for row in map_:
        print(*row)
    print("###")

# print_array(grid)

# drop(0)

# print_array(grid)

def find_max():
    
    return max([max(row) for row in grid])
    

max_num = -1

def gravity(dir):

    for _ in range(dir):
        rotate()
    drop()
    for _ in range(4-dir):
        rotate()

def dfs(cnt):
    global max_num

    if cnt == 5:
        cur_max = find_max()
        max_num = max(cur_max, max_num)
        return
    
    for i in range(4):
        grid_temp = [row[:] for row in grid] 
        
        gravity(i)
        dfs(cnt+1)

        for i in range(N):
            for j in range(N):
                grid[i][j] = grid_temp[i][j]
dfs(0)

print(max_num)