N,M,K = list(map(int,input().split()))

map_ = [list(map(int,input().split())) for _ in range(N)]
def gravity(map_,col):
    temp = [0] * N   
    
    temp_cnt = N-1
    for row in range(N-1,-1,-1):
        if map_[row][col] != 0 :
            temp[temp_cnt] = map_[row][col]
            temp_cnt -= 1
    for row in range(N):
        map_[row][col] = temp[row]
    return map_

def explosion(map_,col):
    Flag = False
    while not Flag :
        Flag = True
        for idx in range(N):
            if map_[idx][col] == 0:
                continue
            start,end = idx,idx
            for next_idx in range(idx+1,N):
                if map_[idx][col] == map_[next_idx][col]:
                    end = next_idx 
                else :
                    break
            if end - start >= M-1 : 
                Flag = False
                for i in range(start,end+1):
                    map_[i][col] = 0
        map_ = gravity(map_,col)
    return map_

def rotate(map_):

    temp = [[0]* N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            if map_[i][j] != 0 :
                temp[j][N-1-i] = map_[i][j]
    for col in range(N):
        map_ = gravity(temp,col)

    return map_

def print_array(map_):

    for row in map_:
        for elem in row :
            print(elem, end=" ")
        print()
    print("##")

for _ in range(K):
    for col in range(N):
        map_ = explosion(map_,col)
    map_ = rotate(map_)

for col in range(N):
    map_ = explosion(map_,col)

cnt = 0
for i in range(N):
    for j in range(N):
        if map_[i][j] != 0 :
            cnt += 1

print(cnt)

## 시간 단축을 위해 column 단위로 폭발과 중력처리를 해줘야한다.