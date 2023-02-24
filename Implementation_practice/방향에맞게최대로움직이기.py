N = int(input())

map_ = [list(map(int,input().split())) for _ in range(N)]

map_dir = [list(map(int,input().split())) for _ in range(N)]

r,c = list(map(lambda x : int(x)-1 , input().split()))

max_cnt = 0

dirs = [(0,0),(-1,0),(-1,1),(0,1),(1,1),(1,0),(1,-1),(0,-1),(-1,-1)]

def in_range(x,y):

    return 0<=x<N and 0<=y<N

def possible(r,c):

    (dx,dy),orig = dirs[map_dir[r][c]], map_[r][c]
    next_ = []
    while in_range(r + dx, c + dy):
        if map_[r+dx][c+dy] > orig :
            next_.append((r+dx,c+dy))
        r, c = r + dx, c+ dy
    return next_

def move(r,c,cnt):
    global max_cnt

    dx,dy = dirs[map_dir[r][c]]
    next_ = possible(r,c)
    if next_:
        for dest in next_:
            nr, nc = dest
            move(nr,nc,cnt + 1)
    else :
        max_cnt = max(max_cnt,cnt)
        

move(r,c,0)

print(max_cnt)