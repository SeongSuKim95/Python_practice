from collections import deque

# Map 중력 
 
def gravity(map):
    N = len(map)
    for i in range(N-2, -1, -1):  # 밑에서 부터 체크
        for j in range(N):
            # if map[i][j] > -1:  # -1이 아니면 아래로 다운
                r = i
                while True:
                    if 0<=r+1<N and map[r+1][j] == -2:  # 다음행이 인덱스 범위 안이면서 -2이면 아래로 다운
                        map[r+1][j] = map[r][j]
                        map[r][j] = -2
                        r += 1
                    else:
                        break
    return map


# Map 반시계 90도 회전

def rot90cc(map):
    N = len(map)
    nmap = [[0]*N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            nmap[N-1-j][i] = map[i][j]
    return nmap

# 시계 90도 회전
def rot90c(map):
    N = len(map)
    nmap = [[0]*N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            nmap[j][N-1-i] = map[i][j]

    return nmap


def move_fish():
    res = [[[] for _ in range(4)] for _ in range(4)]

    for row in range(4):
        for col in range(4):
            while _temp[row][col]:
                f = _temp[row][col].pop()
                for i in range(f,f-8,-1):
                    i %= 8
                    nrow, ncol = row + fdlist[i][0], col + fdlist[i][1]
                    if 0<= nrow < 4 and 0<= ncol <4 and (nrow,ncol) != shark and _smell[nrow][ncol] == 0:
                        res[nrow][ncol].append(i)
                        break
                else:
                    res[row][col].append(f)
    return res
# for row in _map:
#     print(row)
# for row in rot90cc(_map):
#     print(row)
# for row in rot90c(_map):
#     print(row)

# _map = [[1,1,1,1],
#         [-2,-2,-2,-2],
#         [-2,-2,3,-2],
#         [-2,-2,-2,-2]]
# print(gravity(_map))

# 가장 큰 연결된 그룹 찾기


# 1.
# def dfs(row,col):

#     global answer
#     ret = 1
#     print(row,col)
#     _map[row][col] = 0
#     for dir in _dirlist:
#         nrow = row + dir[0]
#         ncol = col + dir[1]

#         if 0<= nrow < mapsize and 0<= ncol < mapsize and _map[nrow][ncol] > 0 :
#             ret += dfs(nrow,ncol)
#     answer = max(answer,ret)
#     return ret

# for row in range(mapsize):
#     for col in range(mapsize):
#         if _map[row][col] >  0:
#             dfs(row,col)
# print(answer)

# 2.

# def dfs(row,col):

#     global answer
#     visited[row][col] = 1
#     ret = 1
#     for dir in _dirlist:
#         nrow = row + dir[0]
#         ncol = col + dir[1]
#         if 0<= nrow < mapsize and 0 <= ncol < mapsize and not visited[nrow][ncol] and _map[nrow][ncol] != 0:
#             ret += dfs(nrow,ncol)
#     answer = max(answer,ret)
#     return ret


# for row in range(mapsize):
#     for col in range(mapsize):
#         if _map[row][col]> 0 and not visited[row][col]:
#             dfs(row,col)


# BFS
# def bfs(_map):
#     map_size = len(_map)
#     visited = [[False] * map_size for _ in range(map_size)]
    
#     max_area_count = 0 # 영역 크기
#     for row in range(map_size):
#         for col in range(map_size):
#             area_count = 0
#             if visited[row][col] or _map[row][col] == 0:
#                 continue

#             # BFS를 
#             q = deque()
#             q.append((row, col))
#             visited[row][col] = True

#             while q:
#                 cur_row, cur_col = q.popleft()
                
#                 area_count += 1  # 카운트 추가

#                 for dir in _dirlist:
#                     n_row = cur_row + dir[0]
#                     n_col = cur_col + dir[1]
#                     if n_row < 0 or n_col < 0 or n_row >= map_size or n_col >= map_size or visited[n_row][n_col]:
#                         continue
#                     if _map[n_row][n_col] != 0:
#                         visited[n_row][n_col] = True
#                         q.append((n_row, n_col))

#             max_area_count = max(max_area_count, area_count) # 최대 얼음 덩어리 크기 파악
#     print(max_area_count)
# bfs(_map)

# Combination 구현하기

def comb(arr, n):
    result = []
    
    if n > len(arr):
        return result
    if n == 1:
        for i in arr:
            result.append([i])
    elif n > 1:
        for i in range(len(arr) - n + 1):
            for j in comb(arr[i+1:],n-1):
                result.append([arr[i]] + j)
    return result

# Permutation 구현하기

def perm(arr,n):

    result = []
    if n > len(arr):
        return result
    
    if n == 1:
        for i in arr:
            result.append([i])
    
    elif n > 1:
        for i in range(len(arr)):
            ans = [j for j in arr]
            ans.remove(arr[i])
            for p in perm(ans,n-1):
                result.append([arr[i]]+p)
    return result

# arr = [1,2,3]

# print(perm(arr,3))


def comb(arr, n):

    result = []
    if n == 0:
        return result
    elif n == 1:
        for i in arr:
            result.append([i])
    
    elif n > 1:
        for i in range(len(arr)-n+1):
            for j in comb(arr[i+1:],n-1):
                result.append([arr[i]]+j)
    
    return result


# def rotated(a):
#   n = len(a)
#   m = len(a[0])

#   result = [[0]* n for _ in range(m)]

#   for i in range(n):
#     for j in range(m):
#       result[j][n-i-1] = a[i][j]
#   return result


_map = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]

# def rotate90(map,flag):

#     N, M = len(map), len(map[0])

#     if flag == 1: # 90
        
#         nmap = [[0]*N for _ in range(M)]
#         for row in range(N):
#             for col in range(M):
#                 nmap[col][N-1-row] = map[row][col]

#     elif flag == 2: # 180
#         nmap = [[0]*M for _ in range(N)]
#         for row in range(N):
#             for col in range(M):
#                 nmap[N-1-row][M-1-col] = map[row][col]
    
#     elif flag == 3: # 270
#         nmap = [[0]*N for _ in range(M)]
#         for row in range(N):
#             for col in range(M):
#                 nmap[M-1-col][row] = map[row][col]

#     return nmap


# _map =[[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]]


# def rotate90(map,row,col,size):
    
#     # 행: row ~ row+size
#     # 열: col ~ col+size
#     N = size
#     _nmap = [[0]*N for _ in range(N)]
    
#     for r in range(N):
#         for c in range(N):
#             _nmap[r][c] = map[row+r][col+c]
        
#     for r in range(N):
#         for c in range(N):
#             map[row+r][col+c] = _nmap[N-1-c][r]
    
#     return map
    


# for row in rotate90(_map,1,1,2):
#     print(row)



# def comb(arr,n):

#     narr = []
#     N = len(arr)
#     if n <= 0 :
#         pass
#     elif n == 1:
#         for i in arr:
#             narr.append([i])
#     else :

#         for i in range(N-(n-1)):
#             for j in comb(arr[i+1:],n-1):
#                 narr.append([arr[i]]+j)
#     return narr

# print(comb([1,2,3,4],2))

# def comb(arr, n):

#     result = []
#     if n == 0:
#         return result
#     elif n == 1:
#         for i in arr:
#             result.append([i])
    
#     elif n > 1:
#         for i in range(len(arr)-n+1):
#             for j in comb(arr[i+1:],n-1):
#                 result.append([arr[i]]+j)
    
#     return result

# 특정 기준 순서대로 sorting 하는 법 : lambda 식 안에 tuple 형태로 기준 항목을 정렬
# 값에 -를 붙여서 내림차순 정렬을 하자

# test = [[1,2,(0,0)],[3,4,(1,0)],[1,3,(3,4)]]

# test.sort(key = lambda x : (x[0],x[1],x[2][0],x[2][1]))
# print(test)

# 리스트 중복 제거 하기

# test =[1,2,3,4,4]

# new_list = list(dict.fromkeys(test))

# new_list = list(set(test))
# print(new_list) # [1,2,3,4]

# 리스트 연속된 중복 원소 제거

# test = [1,2,3,3,4,4,4,3,3,4,4,5,5]

# stack = []
# new_list = []
# for i in test:
#     if not stack:
#         stack.append(i)
#         new_list.append(i)
#     else:
#         if i == stack[-1]:
#             pass
#         else : 
#             stack.append(i)
#             new_list.append(i)

# print(new_list)

# 행렬 중력 적용하기

a = [[1,1,1],[-2,-1,-2],[-2,-2,-2]]

# def gravity():
#     N = len(a)
#     for i in range(N-2, -1, -1):  # 행 :밑에서 2번째 행부터 체크 (N-2 ~ 0 까지)
#         for j in range(N): # 해당 행의 각 열들을 체크
#             # -1 : 벽, -2 : 빈 공간
#             if a[i][j] > -1:  # -1이 아니면 아래로 다운
#                 cur_r = i # 현재 행
#                 while True:
#                     if 0<=cur_r+1<N and a[cur_r+1][j] == -2:  # 다음행이 배열 범위 안이면서 비어 있으면
#                         a[cur_r+1][j] = a[cur_r][j]
#                         a[cur_r][j] = -2
#                         cur_r += 1 # 가장 밑 부분까지 반복
#                     else:
#                         break

def gravity(map):
    N = len(map)

    """
    N-2 행 (바닥)부터 탐색 시작, 0 까지
    각 열의 원소의 상태 확인, 벽이면 continue 아니면 go
    해당 열의 다음 행 원소가 범위 내에 존재 and 비어 있는 칸인지 확인 
    """
    for i in range(N-2,-1,-1):
        for j in range(N):
            if map[i][j] == -1 :
                continue
            else:
                cur_row = i
                while True:
                    if 0<= cur_row + 1< N and map[cur_row+1][j] == -2:
                        map[cur_row+1][j] = map[cur_row][j]
                        map[cur_row][j] = -2
                        cur_row +=1
                    else :
                        break
    return map
print(gravity(a))


def dfs(x, y, dep, cnt, visit):

    global max_eat, shark, eat

    if dep == 3:
        if max_eat < cnt:
            max_eat = cnt
            shark = (x,y)
            eat = visit[:] # 먹은 물고기들의 좌표
        return
    
    for d in range(4):
        nx = x + dx[d]
        ny = y + dy[d]
        if 0<= nx < 4 and 0<=ny <4 :
            if (nx,ny) not in visit:
                visit.append((nx,ny)) # 맵을 back -tracking할때는 이런식으로 방문한 좌표만 넣어주는 형식을 쓰자.
                dfs(nx,ny,dep+1,cnt + len(temp[nx][ny]),visit) # len(temp[nx][ny]) 물고기 개수를 참조만!
                visit.pop() # back - tracking
            else:
                dfs(nx,ny,dep+1,cnt,visit) #방문한 곳이면 depth 만 늘리기