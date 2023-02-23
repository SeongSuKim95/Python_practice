# N, M, t, k = list(map(int,input().split()))

# balls_tmp = (list(input().split()) for _ in range(M))

N, M ,t, k = 4, 3, 1, 2

balls_tmp = [[1,4,"D",1],[2,1,"R",3],[3,4,"U",1]]

map_ = [[[] for _ in range(N)] for _ in range(N)]

# grid = [
#     [[] for _ in range(N)]
#      for _ in range(N)
# ]

next_map_ = [[[] for _ in range(N)] for _ in range(N)]

balls = []
# 방향 전환 고려
# 상 좌 우 하
dirs = [(-1,0),(0,-1),(0,1),(1,0)]
dir_dec = {"U":0,"L":1,"R":2,"D":3}

def print_array(array):

    for row in array:
        for elem in row :
            print(elem, end = " ")
        print()

for idx,(x,y,dir,v) in enumerate(balls_tmp):
    map_[int(x)-1][int(y)-1] = [[int(v),idx+1,dir_dec[dir]]]

def in_range(x,y):

    return 0<= x < N and 0<= y < N

def move():

    for i in range(N):
        for j in range(N):
            if map_[i][j]:
                # print(i,j)
                for ball in map_[i][j]:
                    # print(ball)
                    cur_x,cur_y,cur_v,cur_num,cur_dir = i,j,ball[0],ball[1],ball[2]
                    for _ in range(cur_v):
                        nx, ny = cur_x + dirs[cur_dir][0], cur_y + dirs[cur_dir][1]
                        if in_range(nx,ny):
                            cur_x,cur_y = nx,ny
                        else :
                            cur_dir = 3 - cur_dir
                            cur_x, cur_y = cur_x + dirs[cur_dir][0], cur_y + dirs[cur_dir][1]
                    # print(cur_v,cur_num,cur_dir)
                    # print(next_map_[cur_x][cur_y])
                    next_map_[cur_x][cur_y].append([cur_v,cur_num,cur_dir])
                    # if next_map_[cur_x][cur_y] : 
                    #     next_map_[cur_x][cur_y] += [[cur_v,cur_num,cur_dir]]
                    # else :
                    #     next_map_[cur_x][cur_y] = [[cur_v,cur_num,cur_dir]]
def sorting():

    for i in range(N):
        for j in range(N):
            # print("D",next_map_[i][j][:k])
            if len(next_map_[i][j]) > k :
                next_map_[i][j] = sorted(next_map_[i][j], key = lambda x : (x[0],x[1]),reverse = True)
                temp = []
                for l in range(k):
                    temp.append(next_map_[i][j][l])
                next_map_[i][j] = temp
                # print(next_map_[i][j])
def copy():
    for i in range(N):
        for j in range(N):
            map_[i][j] = next_map_[i][j][:]
    for i in range(N):
        for j in range(N):
            next_map_[i][j] = []
for _ in range(t):
    # print_array(map_)
    move()
    # print("######")
    # print_array(next_map_)
    sorting()
    copy()
    # print("#####")
    # print_array(map_)

cnt = 0

for i in range(N):
    for j in range(N):
        if map_[i][j] :
            cnt += len(map_[i][j])
print(cnt)

    

'''
[[],[],[]] 과 [[]*3] 은 다르다!
'''