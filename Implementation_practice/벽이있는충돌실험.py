def print_array(array):

    for row in array:
        for elem in row :
            print(elem,end = " ")
        print()

t = int(input())

dirs = {
    "U": (-1,0),
    "D": (1,0),
    "L": (0,-1),
    "R": (0,1)
}
def in_range(x,y):

    return 0<= x < N and 0<= y < N

def move():
    balls_next = {}
    for (x,y),dir in balls.items():
        dir_temp = dir
        cur_x,cur_y,dir = x,y,dirs[dir]
        nx,ny = cur_x + dir[0], cur_y + dir[1]
        if in_range(nx,ny):
            next_map[nx][ny] += 1
            balls_next[(nx,ny)]= dir_temp
        else :
            next_map[cur_x][cur_y] += 1
            if dir_temp == "U":
                balls_next[(cur_x,cur_y)] = "D"
            elif dir_temp == "D":
                balls_next[(cur_x,cur_y)] = "U"
            elif dir_temp == "L":
                balls_next[(cur_x,cur_y)] = "R"
            elif dir_temp == "R":
                balls_next[(cur_x,cur_y)] = "L"
    return balls_next

def remove(balls_next):

    for i in range(N):
        for j in range(N):
            if next_map[i][j] >= 2 :
                next_map[i][j] = 0
                balls_next.pop((i,j))
    
    for i in range(N):
        for j in range(N):
            next_map[i][j] = 0

    return balls_next

for _ in range(t):
    N, M = list(map(int,input().split()))

    balls = {}
    for _ in range(M):
        x,y,dir = list(map(lambda x : int(x) - 1 if x.isdigit() else x,input().split()))
        balls[(x,y)] = dir
    next_map = [[0] * N for _ in range(N)]
    balls_history = [balls]
    
    for _ in range(2*N):
        # print("start",cnt,balls)
        balls = move()
        balls = remove(balls)
        # print("Removed",cnt,balls)
        if balls in balls_history:
            break
        else :
            balls_history.append(balls)
            
    print(len(balls))