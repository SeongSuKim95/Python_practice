from collections import deque


# 상 하 좌 우
dx = [-1,1,0,0]
dy = [0,0,-1,1]

# Pipe list

pipe_dir = { 
    1 : [0,1,2,3],
    2 : [0,1],
    3 : [2,3],
    4 : [0,3],
    5 : [1,3],
    6 : [1,2],
    7 : [0,2]
}
counter_dir =  {
    0 : 1,
    1 : 0,
    2 : 3,
    3 : 2
}

N,M,R,C,L = map(int,input().split())

map_ = [list(map(int,input().split())) for _ in range(N)]

q = deque()
q.append((R,C))
cnt = 1
visited = [[0] * M for _ in range(N)]
visited[R][C] = 1
# BFS
while q :
    cur_r, cur_c = q.popleft()
    if visited[cur_r][cur_c] == L + 1:
        break    
    for dir in pipe_dir[map_[cur_r][cur_c]]:
        nr, nc = cur_r + dx[dir] , cur_c + dy[dir]
        if 0<= nr < N and 0<= nc < M and not visited[nr][nc] and map_[nr][nc] and (counter_dir[dir] in pipe_dir[map_[nr][nc]]): 
            q.append((nr,nc)) 
            visited[nr][nc] = visited[cur_r][cur_c] + 1
            if visited[nr][nc] == L + 1:
                break
            else : 
                cnt += 1
# for i in visited :
#     print(i) 
print("#{}".format(cnt))



