from collections import deque

n,k,u,d = list(map(int,input().split()))

map_ = [list(map(int,input().split())) for _ in range(n)]

selected_city = []

dxs, dys = [-1,1,0,0,0],[0,0,-1,1,0]
idx_lst = [i for i in range(n*n)]
max_cnt = 0

def in_range(x,y):

    return 0<=x<n and 0<=y<n


def bfs(selected_idx):
    q = deque()
    cnt = 0
    visited = [[False] * n for _ in range(n)]
    for idx in selected_idx:
        q.append((idx//n,idx%n))
        visited[idx//n][idx%n] = True
        cnt += 1

    while q :
        cur_x, cur_y = q.popleft()
        cur_height = map_[cur_x][cur_y]
        for dx,dy in zip(dxs,dys):
            nx, ny = cur_x + dx, cur_y + dy
            if in_range(nx,ny) and u <= abs(cur_height - map_[nx][ny]) <= d and not visited[nx][ny]:
                visited[nx][ny] = True
                q.append((nx,ny))
                cnt += 1
    return cnt

def dfs(idx,cnt):
    global max_cnt
    if cnt == k :
        num_city = bfs(selected_city)
        max_cnt = max(max_cnt,num_city)
        return
    if idx == n*n :
        return
    
    selected_city.append(idx)
    dfs(idx+1,cnt+1)
    selected_city.pop()

    dfs(idx+1,cnt)

dfs(0,0)

print(max_cnt)