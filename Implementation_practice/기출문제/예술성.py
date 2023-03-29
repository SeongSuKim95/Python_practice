from collections import deque

n = int(input())

dxs,dys = [-1,1,0,0],[0,0,-1,1]
grid = [
    list(map(int,input().split()))
    for _ in range(n)
]

mark = [
    [0 for _ in range(n)]
    for _ in range(n)
]

visited = [
    [False for _ in range(n)]
    for _ in range(n)
]

def print_array(array):

    for row in array:
        print(*row)
    print()


def in_range(x,y):

    return 0<=x<n and 0<=y<n

def init_visited():

    for i in range(n):
        for j in range(n):
            visited[i][j] = False

def init_mark():

    for i in range(n):
        for j in range(n):
            mark[i][j] = 0

def bfs():


    init_visited()
    init_mark()
    gidx = 0
    g_info = {}
    for x in range(n):
        for y in range(n):
            if not visited[x][y]:
                gidx += 1
                q = deque()
                visited[x][y] = True
                mark[x][y] = gidx
                q.append((x,y))
                gcnt = 1
                while q :
                    cur_x,cur_y = q.popleft()
                    cur_color = grid[cur_x][cur_y]
                    for dx,dy in zip(dxs,dys):
                        nx,ny = cur_x + dx, cur_y +dy
                        if in_range(nx,ny) and not visited[nx][ny] and grid[nx][ny] == cur_color :
                            visited[nx][ny] = True
                            mark[nx][ny] = gidx
                            gcnt += 1
                            q.append((nx,ny))
                g_info[gidx] = (gcnt,cur_color)  
    # print_array(mark)
    return gidx,g_info

def calc_artistic(gidx,g_info):
    score = 0
    adjacent = [
        [0 for _ in range(gidx + 1)]
        for _  in range(gidx + 1)
    ]

    for i in range(n):
        for j in range(n):
            cur_x,cur_y = i,j
            cur_group = mark[i][j]
            for dx,dy in zip(dxs,dys):
                nx, ny = cur_x + dx, cur_y + dy
                if in_range(nx,ny):
                    adj_group = mark[nx][ny]
                    adjacent[cur_group][adj_group] += 1
    # print_array(adjacent)

    for i in range(1,gidx+1):
        for j in range(i+1,gidx+1):
            if adjacent[i][j] :
                cur_gidx,adj_gidx = i,j
                cur_gcnt,cur_gcolor = g_info[cur_gidx] 
                adj_gcnt,adj_gcolor = g_info[adj_gidx]
                score += (cur_gcnt + adj_gcnt) * cur_gcolor * adj_gcolor * adjacent[i][j]
    
    return score

def rotate_part(sx,sy):

    size = n//2

    temp = [[0 for _ in range(size)] for _ in range(size)]
    new_temp = [[0 for _ in range(size)] for _ in range(size)]

    for i in range(size):
        for j in range(size): 
            temp[i][j] = grid[i+sx][j+sy] 
    
    for i in range(size):
        for j in range(size):
            new_temp[j][size-1-i] = temp[i][j]
    
    for i in range(size):
        for j in range(size):
            grid[i+sx][j+sy] = new_temp[i][j]


def rotate():

    # 십자 반시계
    mid_col = []
    for i in range(n):
        mid_col.append(grid[i][n//2])
    mid_row = grid[n//2][:]

    grid[n//2] = mid_col[:]
    for i in range(n):
        grid[i][n//2] = mid_row[::-1][i]
    
    # 4 격자 시계
    size = n//2
    rotate_part(0,0)
    rotate_part(size+1,0)
    rotate_part(0,size+1)
    rotate_part(size+1,size+1)
    # print_array(grid)

answer = 0
for _ in range(4):
    gidx,g_info = bfs()
    answer += calc_artistic(gidx,g_info)
    rotate()
print(answer)