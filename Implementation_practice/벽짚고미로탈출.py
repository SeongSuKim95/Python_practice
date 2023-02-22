N = int(input())

x, y = list(map(int,input().split()))

map_ = [list(input()) for _ in range(N)]

def print_array(map_):

    for row in map_:
        for elem in row:
            print(elem, end = " ")
        print()

def in_range(x,y):

    return 0<= x < N and 0<= y < N

def chdir_cclk(dir):
    
    return (dir - 1 + 4) % 4

def chdir_clk(dir):
    
    return (dir + 1) % 4

def wall_check(x,y):

    if map_[x][y] == "#" : 
        return True

    else :
        return False

# Clockwise 우 하 좌 상
dxs, dys, = [0,1,0,-1], [1,0,-1,0]

cur_dir,cur_x,cur_y = 0,x-1,y-1
time = 0
Flag = False

orig_dir, orig_x, orig_y = cur_dir, cur_x, cur_y 
while in_range(cur_x,cur_y):

    nx, ny = cur_x + dxs[cur_dir], cur_y + dys[cur_dir]
    if in_range(nx,ny): # 격자 안
        if map_[nx][ny] == "#":
            cur_dir = chdir_cclk(cur_dir)
        elif map_[nx][ny] == ".":
            cur_x , cur_y = nx, ny
            time += 1
            ndir = chdir_clk(cur_dir)
            wall_x, wall_y = cur_x + dxs[ndir] , cur_y + dys[ndir]
            if wall_check(wall_x,wall_y):
                pass
            else :
                cur_dir,cur_x,cur_y = ndir,wall_x,wall_y
                time += 1

    else :
        time += 1
        break

    if cur_x == orig_x and cur_y == orig_y and cur_dir == orig_dir :
        Flag = True
        break

if not Flag:
    print(time)
else :
    print(-1)

            






