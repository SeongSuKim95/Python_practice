from collections import deque

# 상 하 좌 우
dr = [-1,1,0,0]
dc = [0,0,-1,1]
cost_lst = [ K * K + (K-1)*(K-1) for K in range(25)]

def bfs(i,j):
    
    global max_cnt
    
    visited = [[0] * N for _ in range(N)]

    Q = deque([(i,j)])
    
    visited[i][j] = 1
    cnt = 1
    home = maps_[i][j]

    if home * M - cost_lst[1] >= 0 :
        max_cnt = max(max_cnt,home)
    
    while cnt <= N + 1  :

        qlength = len(Q)
        
        for _ in range(qlength):

            r,c = Q.popleft()

            for dir in range(4):
                nr = r + dr[dir]
                nc = c + dc[dir]

                if not(0<=nr<N and 0<=nc<N):
                    continue
                if not visited[nr][nc]:
                    Q.append((nr,nc))
                    visited[nr][nc] = 1

                    if maps_[nr][nc] :
                        home += 1
        if home * M - cost_lst[cnt+1] >= 0 :
            max_cnt = max(max_cnt,home)
        cnt += 1 

T = int(input())
for tc in range(T):

    N , M = map(int, input().split())

    maps_ = [list(map(int,input().split())) for _ in range(N)]
    max_cnt = 0
    for i in range(N):
        for j in range(N):
            bfs(i,j)
    print("#{} {}".format(tc+1,max_cnt))
