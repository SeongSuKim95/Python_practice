N, m, t = list(map(int,input().split()))

map_ = [list(map(int,input().split())) for _ in range(N)]

balls = []

for _ in range(m):

    balls.append(tuple(map(lambda x : int(x)-1,input().split())))


cur_ball = [[0] * N for _ in range(N)]
next_ball = [[0] * N for _ in range(N)]
dxs,dys = [-1,1,0,0],[0,0,-1,1]


for ball in balls:

    cur_ball[ball[0]][ball[1]] = 1

def in_range(x,y):

    return 0<= x < N and 0<= y < N

def remove():

    for i in range(N):
        for j in range(N):
            if next_ball[i][j] >= 2 :
                next_ball[i][j] = 0

def duplicate():

    for i in range(N):
        for j in range(N):
            cur_ball[i][j] = next_ball[i][j]

    for i in range(N):
        for j in range(N):
            next_ball[i][j] = 0

def add(balls):
    balls = []
    for i in range(N):
        for j in range(N):
            if cur_ball[i][j] :
                balls.append((i,j))
    return balls
def move():

    for ball in balls:
        cur_x,cur_y,max_,mx,my = ball[0], ball[1],0,ball[0],ball[1]
        for dx,dy in zip(dxs,dys):
            nx, ny = cur_x + dx , cur_y + dy
            if in_range(nx,ny) and map_[nx][ny] > max_:
                max_,mx,my = map_[nx][ny],nx,ny
        next_ball[mx][my] += 1

def print_array(array):

    for i in range(N):
        for j in range(N):
            print(array[i][j], end = " ")
        print()
for _ in range(t):
    move()
    remove()
    duplicate()
    balls = add(balls)

print(len(balls))

'''
격자 내에서 여러 객체의 이동을 동시에 진행해야 하는 경우
1. 현재 map, next map 두개를 생성 ( 현재 map에 객체들의 현재 상태 기록, next map은 초기화)
2. 현재 map에서 알고리즘을 거쳐 next map 생성
3. next map을 현재 map에 복사
4. next map 초기화
'''