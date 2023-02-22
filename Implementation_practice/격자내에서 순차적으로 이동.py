N, m = list(map(int,input().split()))

map_ = [list(map(int,input().split())) for _ in range(N)]
 
dxs,dys = [-1,-1,-1,0,0,1,1,1],[-1,0,1,-1,1,-1,0,1]

next_map = [[0] * N for _ in range(N)]
pos = {}

def get_pos():
    
    for i in range(N):
        for j in range(N):
            pos[map_[i][j]] = (i,j)
    
def print_array(array):

    for i in range(N):
        for j in range(N):
            print(array[i][j], end = " ")
        print()

def in_range(x,y):

    return 0<= x < N and 0<= y < N

def change():

    for num in range(1,N*N+1):
        v = pos[num]
        cur_x, cur_y, mx, my, max_ = v[0], v[1], v[0], v[1], 0
        for dx,dy in zip(dxs,dys):
            nx, ny = cur_x + dx , cur_y + dy
            if in_range(nx,ny) and map_[nx][ny] > max_:
                max_ = map_[nx][ny]
                mx, my = nx,ny
        pos[num] = (mx,my)
        pos[max_] = (cur_x,cur_y)
        map_[mx][my] = num
        map_[cur_x][cur_y] = max_


get_pos()
for _ in range(m):
    change()

print_array(map_)