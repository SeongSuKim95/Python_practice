r,c,k = list(map(int,input().split()))

grid = [list(map(int,input().split())) for _ in range(3)]

def rotate_clk(array):
    n,m = len(array), len(array[0])

    new_array = [[0 for _ in range(n)] for _ in range(m)]
    
    for i in range(n):
        for j in range(m):
            new_array[j][n-1-i] = array[i][j]

    return new_array

def rotate_cclk(array):
    n,m = len(array), len(array[0])

    new_array = [[0 for _ in range(n)] for _ in range(m)]

    for i in range(n):
        for j in range(m):
            new_array[j][i] = array[i][j]
    return new_array

def print_array(array):

    for row in array:
        print(*row)

def step1(grid):
    next_grid = []
    row_cnt = len(grid)
    for row in grid :
        row_dict = {}
        for elem in row :
            if elem != 0 :
                if elem in row_dict.keys():
                    row_dict[elem] += 1
                else :
                    row_dict[elem] = 1
        temp = dict(sorted(row_dict.items(),key = lambda x : (x[1],x[0])))
        lst = []
        for k,v in temp.items():
                lst.append(k)
                lst.append(v)
        next_grid.append(lst)
    
    max_len = 0

    for row in next_grid :
        max_len = max(max_len,len(row))

    for idx,row in enumerate(next_grid) :
        tmp_row = row[:]
        if len(tmp_row) < max_len :
            for _ in range(max_len-len(tmp_row)):
                next_grid[idx].append(0)
    return next_grid

def trim(grid):

    temp = []
    if len(grid) > 100 :
        for i in range(100):
            temp.append(grid[i][:])
    grid = temp
    
    temp = []
    if len(grid[0]) > 100 :
        for i in range(100):
            row = grid[i][:]
            temp.append(row[:100])
    
    return temp
    
time = 0

while True :

    try :
        if grid[r-1][c-1] == k :
            break
        else:
            if time > 100 :
                time = -1
                break
    except :
        pass

    row_cnt, col_cnt = len(grid), len(grid[0])
    if row_cnt >= col_cnt:
        grid = step1(grid)
    else :
        grid = rotate_clk(grid)
        grid = step1(grid)
        grid = rotate_cclk(grid)
    time += 1
    if len(grid) > 100 or len(grid[0]) > 100 :
        grid = trim(grid)

print(time)