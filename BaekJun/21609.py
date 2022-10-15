
from collections import deque
# 행, 일반 블록 번호
N, M = map(int,input().split())

_map = [list(map(int,input().split())) for _ in range(N)]
_dirlist = [[-1,0],[1,0],[0,-1],[0,1]]

def rot90():
    
    _nmap = [[0]*N for _ in range(N)]
    for row in range(N):
        for col in range(N):
            _nmap[N-1-col][row] = _map[row][col]
    
    return _nmap

def gravity():

    for i in range(N-2,-1,-1):
        for j in range(N):

            if _map[i][j] == -1 :
                continue
            else:
                cur_row = i
                while True:
                    if 0<= cur_row+1 < N and _map[cur_row+1][j] == -2:
                        _map[cur_row+1][j] = _map[cur_row][j]
                        _map[cur_row][j] = -2
                        cur_row += 1
                    else:
                        break

def bfs(row,col,color):

    visited[row][col] = 1
    q = deque([(row,col)])
    bcnt, rbcnt = 1,0
    b_coord, rb_coord = [[row,col]],[]
    while q :
        x,y = q.popleft()
        for dir in _dirlist:
            nx, ny = x + dir[0], y + dir[1]
            if nx <0 or nx>= N or ny <0 or ny >= N or visited[nx][ny] :
                continue
            if _map[nx][ny] == color: #일반 블록
                q.append((nx,ny))
                bcnt += 1
                visited[nx][ny] = 1
                b_coord.append([nx,ny])
            elif _map[nx][ny] == 0 : #무지개 블록
                q.append((nx,ny))
                visited[nx][ny] = 1
                rbcnt += 1
                rb_coord.append([nx,ny])

    b_coord.sort() # 기준 블록이 맨 앞으로 오도록 정렬
    return [bcnt+rbcnt,rbcnt,b_coord,rb_coord]
            

def remove():

    blocks = block_infos[0][2] + block_infos[0][3]
    for block in blocks:
        _map[block[0]][block[1]] = -2

score = 0

while True:
    visited = [[0]*N for _ in range(N)]
    block_infos =[]
    for row in range(N):
        for col in range(N):
            block_info = []
            if _map[row][col] > 0 and not visited[row][col]:  # 만약 일반 블록이고, 방문하지 않은 블록이면
                block_info = bfs(row,col,_map[row][col]) 
                if block_info[0]>=2:
                    block_infos.append(block_info)
                for rblock in block_info[3]: # 무지개 블록 방문 처리 풀기
                    visited[rblock[0]][rblock[1]] = 0 
            else:
                pass
    if not block_infos:
        break
    
    block_infos.sort(key = lambda x : (x[0],x[1],x[2][0][0],x[2][0][1]),reverse=True)
    score += block_infos[0][0] ** 2
    remove()
    gravity()
    _map = rot90()
    gravity()

print(score)