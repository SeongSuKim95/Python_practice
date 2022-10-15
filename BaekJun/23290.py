

import copy

def move_fish():
    res = [[[] for _ in range(4)] for _ in range(4)]

    for row in range(4):
        for col in range(4):
            while temp[row][col]:
                cur_d = temp[row][col].pop()
                for i in range(cur_d,cur_d-8,-1): # 반시계 방향
                    i %= 8
                    nrow, ncol = row + f_dx[i], col + f_dy[i]
                    if 0<= nrow < 4 and 0<= ncol <4 and (nrow,ncol) != shark and not smell[nrow][ncol]:
                        res[nrow][ncol].append(i)
                        break
                else:
                    res[row][col].append(cur_d)
    return res

def dfs(x, y, dep, cnt, visit):

    global max_eat, shark, eat

    if dep == 3:
        if max_eat < cnt:
            max_eat = cnt
            shark = (x,y)
            eat = visit[:]
        return
    
    for d in range(4):
        nx = x + dx[d]
        ny = y + dy[d]
        if 0<= nx < 4 and 0<=ny <4 :
            if (nx,ny) not in visit:
                visit.append((nx,ny))
                dfs(nx,ny,dep+1,cnt + len(temp[nx][ny]),visit)
                visit.pop() # back - tracking
            else:
                dfs(nx,ny,dep+1,cnt,visit)
f_dx = [0,-1,-1,-1,0,1,1,1]
f_dy = [-1,-1,0,1,1,1,0,-1]
dx = [-1,0,1,0]
dy = [0,-1,0,1]

M,S = map(int,input().split())
fish =  [list(map(int,input().split())) for _ in range(M)]
_map = [[[] for _ in range(4)] for _ in range(4)] # fish 맵과 smell 맵을 따로 
# fish 맵의 element를 빈리스트로 쓰기

for x,y,d in fish:
    _map[x-1][y-1].append(d-1)

shark = tuple(map(lambda x: int(x)-1, input().split())) # 상어 좌표
smell = [[0] * 4 for _ in range(4)]

for _ in range(S):
    eat = []
    test = list()
    max_eat = -1
    # 1. 모든 물고기 복제하기
    temp = copy.deepcopy(_map)
    # 2. 물고기 이동
    temp = move_fish()
    # 3. 상어 이동
    dfs(shark[0],shark[1],0,0,list())

    for x,y in eat: # 지나온 좌표들
        if temp[x][y] :
            temp[x][y] = [] # 물고기 제거
            smell[x][y] = 3 # 3번 돌아야 없어짐
    # 4. 냄새 사라짐 (아까 생성된 냄새를 2로 만들어줌과 동시에, 기존의 냄새 map에서 1씩 빼기)

    for i in range(4):
        for j in range(4):
            if smell[i][j] :
                smell[i][j] -= 1
    
    # 5 . 복제된 물고기
    for i in range(4):
        for j in range(4):
            _map[i][j] += temp[i][j] # 바뀐 물고기를 더한다

answer = 0
for i in range(4):
    for j in range(4):
        answer += len(_map[i][j])


print(answer)