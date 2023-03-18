N = int(input())

grid = [
    list(map(int,input().split()))
    for _ in range(N)
]
#
pos_dirs = [(1,-1),(1,1),(-1,1)]

def in_range(x,y):

    return 0<=x<N and 0<=y<N

def get_pos(cur_x,cur_y,lst):
    for (dx,dy), length in zip(pos_dirs,lst):
        nx,ny = cur_x + length * dx , cur_y + length * dy
        if not in_range(nx,ny):
            return False
        else :
            cur_x,cur_y = nx,ny
    return True


def mark_area(cur_x,cur_y,pattern):

    new_grid = [[1 for _ in range(N)] for _ in range(N)]
    dirs = [(1,-1),(1,1),(-1,1),(-1,-1)]
    marks = [2,4,5,3]

    for (mark,length, dir) in zip(marks,pattern,dirs):
        if mark == 2 :
            for i in range(cur_x):
                for j in range(cur_y+1):
                    new_grid[i][j] = mark
            temp_x,temp_y = cur_x,cur_y
            for k in range(length+1):
                cur_x , cur_y = temp_x + k * dir[0], temp_y + k * dir[1]
                for j in range(cur_y):
                    new_grid[cur_x][j] = mark

        elif mark == 4 :
            for i in range(cur_x,N):
                for j in range(cur_y):
                    new_grid[i][j] = mark
            temp_x,temp_y = cur_x,cur_y
            for k in range(length+1):
                cur_x, cur_y = temp_x + k * dir[0], temp_y + k * dir[1]
                for i in range(cur_x+1,N):
                    new_grid[i][cur_y] = mark
        elif mark == 5 :
            for i in range(cur_x+1,N):
                for j in range(cur_y,N):
                    new_grid[i][j] = mark
            temp_x,temp_y = cur_x,cur_y
            for k in range(length + 1):
                cur_x,cur_y = temp_x + k * dir[0], temp_y + k * dir[1]
                for j in range(cur_y+1,N):
                    # print(cur_x,j)
                    new_grid[cur_x][j] = mark
        elif mark == 3 :
            for i in range(cur_x+1):
                for j in range(cur_y+1,N):
                    new_grid[i][j] = mark
            temp_x,temp_y = cur_x,cur_y
            for k in range(length+1):
                cur_x,cur_y = temp_x + k * dir[0], temp_y + k * dir[1]
                for i in range(cur_x):
                    new_grid[i][cur_y] = mark
        
    for i in range(cur_x):
        new_grid[i][cur_y] = 2

    return new_grid

def calc_region(area_grid):
    area = {1:0,2:0,3:0,4:0,5:0}
    
    for i in range(N):
        for j in range(N):
            area[area_grid[i][j]] += grid[i][j]
    
    result = sorted(list(area.values()))

    return result[-1] - result[0]
answer = 1e9
for i in range(N):
    for j in range(N):

        for k in range(1,N-1):
            for l in range(1,N-1):
                pattern = [k,l,k,l]
                if not get_pos(i,j,pattern):
                    break
                else :
                    area_grid = mark_area(i,j,pattern)
                    answer = min(answer,calc_region(area_grid))
print(answer)