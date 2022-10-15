

N,M,K = map(int,input().split())

fires = [list(map(int,input().split())) for _ in range(M)]

_map = [[[] for _ in range(N+1)] for _ in range(N+1)]

_dirlist = [[-1,0],[-1,1],[0,1],[1,1],[1,0],[1,-1],[0,-1],[-1,-1]]

for row,col,m,s,d in fires:
    _map[row][col].append((m,s,d))

def move(): 
    # print(f"{_}th iter: move")
    # 빈 맵 만들기
    _nmap = [[[] for _ in range(N+1)] for _ in range(N+1)]
    
    for row in range(1,N+1):
        for col in range(1,N+1):
            if _map[row][col]:
                for ball in _map[row][col]:
                    m,s,d = ball
                    dx, dy = _dirlist[d][0], _dirlist[d][1]      
                    nrow, ncol = (row + s*dx) % N, (col + s*dy) % N
                    if nrow == 0:
                        nrow = N
                    elif nrow == N:
                        nrow = 1
                    if ncol == 0 :
                        ncol = N
                    elif ncol == N:
                        ncol = 1
                    _nmap[nrow][ncol].append((m,s,d))
                    # print(nrow,ncol)
    # print(f"After {_}th iter: move")
    # print(_nmap)
    return _nmap

def merge():
    # print(f"{_}th iter: merge")

    _nmap = [[[] for _ in range(N+1)] for _ in range(N+1)]

    for row in range(1,N+1):
        for col in range(1,N+1):
            if len(_map[row][col]) >= 2:
                m_sum,s_sum = 0,0 # 질량,속력 합
                d_list = [0] * len(_map[row][col])
                for idx, ball in enumerate(_map[row][col]):
                    m,s,d = ball
                    m_sum += m
                    s_sum += s
                    if d % 2 == 0:
                        d_list[idx] = 1
                    else:
                        d_list[idx] = -1
                nm, ns = int(m_sum/5), int(s_sum/len(_map[row][col]))
                if int(m_sum / 5) == 0 : # 나눈 질량이 0이면
                    continue
                if sum(d_list) == len(_map[row][col]) or sum(d_list) == -len(_map[row][col]):
                    d_list = [0,2,4,6]
                else:
                    d_list = [1,3,5,7]
                for nd in d_list:
                    _nmap[row][col].append((nm,ns,nd))
            else: # 2개 이하면?
                _nmap[row][col] = _map[row][col]
 
    # print(f"After {_}th iter: merge")
    # print(_nmap)
    return _nmap
# Loop

for _ in range(K):
    _map = move()
    _map = merge()

ans = 0
for row in range(1,N+1):
    for col in range(1,N+1):
        if _map[row][col]:
            for ball in _map[row][col]:
                ans += ball[0]
print(ans)