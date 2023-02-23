'''
K개중 하나를 N번 선택하기
'''

N = int(input())

map_ = [list(map(int,input().split())) for _ in range(N)]

bomb_ = []

for i in range(N):
    for j in range(N):
        if map_[i][j] == 1:
            bomb_.append((i,j))

num_bombs = len(bomb_)
answer = []

dxs_4,dys_4 = [-1,1,0,0,0],[0,0,-1,1,0]
dxs_8,dys_8 = [-1,-1,1,1,0],[-1,1,-1,1,0]
max_count = -1

def in_range(x,y):
    
    return 0<=x<N and 0<=y<N

def explosion():
    map_tmp = [[0 for _ in range(N)] for _ in range(N)]

    for bomb,(x,y) in zip(answer,bomb_):
        if bomb == 1 :
            
            for row in range(-2,3):
                nx = x + row 
                if in_range(nx,y):
                    map_tmp[x+row][y] = 1
        
        elif bomb == 2:

            for dx,dy in zip(dxs_4,dys_4):
                nx, ny = x + dx, y + dy
                if in_range(nx,ny):
                    map_tmp[nx][ny] = 1

        elif bomb == 3:
            
            for dx,dy in zip(dxs_8,dys_8):
                nx, ny = x + dx, y + dy
                if in_range(nx,ny):
                    map_tmp[nx][ny] = 1
    cnt = 0
    for i in range(N):
        for j in range(N):
            cnt += map_tmp[i][j]
    return cnt            

def select_bomb(num):
    global max_count
    if num_bombs == num :
        cnt = explosion()
        # print(answer)
        max_count = max(cnt,max_count)
        return
    for i in range(1,4):
        answer.append(i)
        select_bomb(num+1)
        answer.pop()

select_bomb(0)
print(max_count)