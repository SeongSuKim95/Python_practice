from collections import deque


N = int(input())
_map = [list(map(int,input().split())) for _ in range(N)]
# 상 좌 우 하
_dirlist = [[-1,0],[0,-1],[0,1],[1,0]]

# N = 4
# _map = [[4,3,2,1],[0,0,0,0],[0,0,9,0],[1,2,3,4]]
for row in range(N):
    for col in range(N):
        if _map[row][col] == 9:
            shark_x, shark_y = row, col
            _map[row][col] = 0
maxsize = 1e9
time,cnt,shark_size = 0, 0, 2
fish = []

def bfs(cur_x,cur_y):
    # visited map에다가 거리 표시 할거임!
    visited = [[-1]*N for _ in range(N)]
    q = deque([(cur_x,cur_y)]) # 처음 넣을 때 list 안의 튜플로 넣어줘야함!
    visited[cur_x][cur_y] = 0
    fish = []
    min_dist = maxsize
    while q:
        cur_x, cur_y = q.popleft()
        # print((cur_x,cur_y))
        if 0 < _map[cur_x][cur_y] < shark_size :
            min_dist = min(min_dist,visited[cur_x][cur_y])
            # print(min_dist)
            if visited[cur_x][cur_y] == min_dist:
                fish.append((cur_x,cur_y)) # 여기도.. min_dist만 있는것...
            else:
                # 아닌 경우 더 찾지 않는다!
                # BFS라서 이렇게 짜야함! 더 먼 거리에 있어도 최소 경우 니까..
                break
        for dir in _dirlist :
            nx = cur_x + dir[0]
            ny = cur_y + dir[1]

            if nx<0 or nx>=N or ny<0 or ny>=N: # 범위 넘어가는 경우
                continue 
            if visited[nx][ny] != -1 or _map[nx][ny] > shark_size:  #방문 했거나 상어 크기보다 큰경우
                continue
            
            q.append((nx,ny))
            visited[nx][ny] = visited[cur_x][cur_y] + 1
    if fish:
        fish.sort()
        fish_x,fish_y = fish[0]
        _map[fish_x][fish_y] = 0
        return fish_x,fish_y,min_dist
    else:
        return -1,-1,-1

while True:

    # 물고기 정보 list 초기화
    # 현재 상어 위치
    fish_x,fish_y,cur_time = bfs(shark_x,shark_y)
    
    if cur_time == -1 : # 물고기를 다 먹었거나 먹을 수 있는 물고기가 없는 경우
        break
    else:
        cnt +=1
        if cnt == shark_size :
            shark_size +=1
            cnt = 0
        time += cur_time
    
    shark_x,shark_y = fish_x,fish_y
print(time)
# N = int(input())

# # 상 하 좌 우 

# _dirlist =[[-1,0],[1,0],[0,-1],[0,1]]

# _map = [list(map(int,input().split())) for _ in range(N)]

# fish_count = 0
# fish_coord = []
# shark_size = 2
# time = 0

# for row in range(N):
#     for col in range(N):
#         if _map[row][col] not in [0,9]:
#             fish_count +=1
#             fish_coord.append((row,col))
#         elif _map[row][col] == 9:
#             shark_coord = (row,col)

# def dfs(row,col,visited,depth,shark_size):
#     # print(depth,row,col)
    
#     if 0 < _map[row][col] < shark_size:
#         fish_info.append([depth,row,col])
    
#     for dir in _dirlist:
#         nrow = row + dir[0]
#         ncol = col + dir[1]

#         if nrow<0 or nrow>=N or ncol<0 or ncol>=N:
#             continue
        
#         else:
#             if not visited[nrow][ncol] and 0<=_map[nrow][ncol]<=6:
#                 if _map[nrow][ncol] <= shark_size : #상어 보다 작거나 같으면
#                     visited[nrow][ncol] = 1
#                     dfs(nrow,ncol,visited,depth+1,shark_size)
#                     visited[nrow][ncol] = 0
            
# row,col = shark_coord
# answer = 0
# exp = 0
# visited = [[0]*N for _ in range(N)]
# cnt = 0
# while True:

#     if fish_count == 0:
#         break
#     fish_info = [] # 
#     depth = 0 # 시간
#     min_depth = 1e9
#     visited[row][col] = 1
    
#     dfs(row,col,visited,depth,shark_size)

#     visited[row][col] = 0

#     if not fish_info: 
#         break
    
#     else:
#         _map[row][col] = 0 # 상어 자리 빼주기
        
#         time, row, col = sorted(fish_info)[0]
#         exp += 1
#         if exp == shark_size:
#             shark_size += 1
#             exp = 0
#         _map[row][col] = 0 # 먹은 자리 빼주기

#         answer += time
#         fish_count -= 1
# print(answer)


# 0 0 0 0 1 1
# 0 0 6 0 2 3
# 0 0 5 0 2 3
# 0 0 0 0 6 3
# 0 0 0 0 0 6
# 0 0 0 0 0 0



