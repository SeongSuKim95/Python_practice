N , R , C = list(map(int,input().split()))

map_ = [list(map(int,input().split())) for _ in range(N)]

dxs = [-1,1,0,0]
dys = [0,0,-1,1]

def in_range(x,y):

    return 0<= x < N and 0<= y < N

def check(x,y):
    max_, max_x, max_y = map_[x][y], x,y
    for dx,dy in zip(dxs,dys):
        nx,ny = x + dx, y + dy
        if not in_range(nx,ny):
            continue
        if map_[nx][ny] > map_[x][y]:
            max_,max_x,max_y = map_[nx][ny],nx,ny
            break

    return max_, max_x, max_y
R,C = R-1,C-1
lst = [map_[R][C]]
while check(R,C)[0] != map_[R][C]:
    max_,R,C = check(R,C)
    lst.append(max_)

for i in lst:
    print(i,end = " ")