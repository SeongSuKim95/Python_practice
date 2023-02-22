N, M, K = list(map(int,input().split()))

apples = [list(map(lambda x : int(x)-1 ,input().split())) for _ in range(M)]

infos = [list(input().split()) for _ in range(K)]

dirs = {
    "U" : (-1,0),
    "D" : (1,0),
    "R" : (0,1),
    "L" : (0,-1)
}

map_ = [[0] * N for _ in range(N)]
map_[0][0] = 1
cur_x,cur_y = 0,0
snake,length = [(cur_x,cur_y)],1
time = 0
def print_array(map_):

    for row in map_:
        for elem in row:
            print(elem,end = " ")
        print()

for apple in apples:
    x,y = apple
    map_[x][y] = 2

def in_range(x,y):

    return 0<=x<N and 0<=y<N
    
flag = False
for info in infos:
    if flag :
        break
    dir, dist = info
    dx,dy = dirs[dir]
    for _ in range(int(dist)):
        time += 1
        nx,ny = cur_x + dx, cur_y + dy

        if not in_range(nx,ny):
            flag = True
            break

        if map_[nx][ny] == 2:
            length += 1
        
        if len(snake) == length :
            tail_x,tail_y = snake[0]
            map_[tail_x][tail_y] = 0
            snake = snake[1:]

        cur_x,cur_y = nx,ny

        if map_[cur_x][cur_y] == 1:
            flag = True
            break
        else : 
            map_[cur_x][cur_y] = 1
            snake.append((cur_x,cur_y))

        # print(snake,time)
        # print_array(map_)

print(time)