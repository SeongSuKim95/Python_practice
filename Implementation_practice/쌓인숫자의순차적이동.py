
N, M = list(map(int,input().split()))

map_ = [list(map(lambda x : [int(x)],input().split())) for _ in range(N)]

targets = list(map(int,input().split()))


dxs,dys = [-1,-1,-1,0,0,1,1,1],[-1,0,1,-1,1,-1,0,1]

def in_range(x,y):

    return 0<=x<N and 0<=y<N


def print_array(array):

    for row in array:
        for elem in row:
            print(elem, end = " ")
        print()
# print_array(map_)

for target in targets :
    for i in range(N):
        for j in range(N):
            for idx,num in enumerate(map_[i][j]):
                if num == target:
                    cur_x,cur_y = i,j
                    cur_idx = idx
    idx = cur_idx
    max_,mx,my = 0, cur_x, cur_y
    for dx,dy in zip(dxs,dys):
        nx,ny = cur_x + dx, cur_y + dy
        if in_range(nx,ny) and map_[nx][ny]:
            for neighbor in map_[nx][ny]:
                if neighbor > max_:
                    max_,mx,my = neighbor,nx,ny         
    map_[mx][my] = map_[cur_x][cur_y][:idx+1] + map_[mx][my] 
    map_[cur_x][cur_y] = map_[cur_x][cur_y][idx+1:]

    # print_array(map_)

for i in range(N):
    for j in range(N):

        if map_[i][j]:

            for elem in map_[i][j]:
                print(elem,end = " ")
            print()
        else :
            print("None")
'''
1. 2차원 배열을 순회하는 것을 함수화하여 원하는 값을 찾을시 즉시 return하게끔 짜기
2. 각 위치의 객체 값들을 list로 관리하기
'''