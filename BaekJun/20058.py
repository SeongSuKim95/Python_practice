from selectors import EpollSelector


N,Q = map(int,input().split())

map_size = 2**N

_map = [list(map(int,input().split())) for _ in range(map_size)]

L_list = list(map(int,input().split()))

# 상 하 좌 우
_dirlist = [[-1,0],[1,0],[0,-1],[0,1]]

def rot90(arr,row,col,block_size):
    narr = [[0]*block_size for _ in range(block_size)]
    rarr = [[0]*block_size for _ in range(block_size)]
    for i in range(row,row+block_size):
        for j in range(col,col+block_size):
            narr[i-row][j-col] = arr[i][j]
    # print(narr)
    for i in range(block_size):
        for j in range(block_size):
            rarr[j][block_size-1-i] = narr[i][j]
    # print(rarr)
    for i in range(row,row+block_size):
        for j in range(col,col+block_size):
            arr[i][j] = rarr[i-row][j-col]
    # print(arr)
    return arr

# arr = [[1,1,1,1,],[2,2,2,2],[3,3,1,2],[4,4,3,4]]
# print(rot90(arr,2,2,2))

# 격자 시계 방향으로 회전시키기
for L in L_list:
    # 블록 격자 나누기
    block_size = 2**L
    for block_base in range(0,2**N,block_size):
        
        # Diagonal 성분들의 block들
        base_row,base_col = block_base,block_base

        if 0<= base_row < map_size and 0<= base_col < map_size:
            _map = rot90(_map,base_row,base_col,block_size)
        else:
            break
        # Diagonal 성분의 우상단 방향 block들
        base_row,base_col = block_base, block_base
        while True:
            cur_row = base_row - block_size
            cur_col = base_col + block_size
            # 우상단에 스타트 격자가 존재 할 수 잇으면
            if 0<= cur_row < map_size and 0<= cur_col < map_size:
                # 격자 돌리기
                _map = rot90(_map,cur_row,cur_col,block_size)        
                # 격자 base 바꾸기
                base_row,base_col = cur_row,cur_col
            else:
                break
         
        # Diagonal 성분의 좌하단 방향 block들
        base_row,base_col = block_base,block_base
        while True:
            cur_row = base_row + block_size
            cur_col = base_col - block_size
            # 우상단에 스타트 격자가 존재 할 수 잇으면
            if 0<= cur_row < map_size and 0<= cur_col < map_size:
                # 격자 돌리기
                _map = rot90(_map,cur_row,cur_col,block_size)        
                # 격자 base 바꾸기
                base_row,base_col = cur_row,cur_col
            else:
                break
    cnt = [[0]*map_size for _ in range(map_size)]
    for row in range(map_size):
        for col in range(map_size):
            for dir in _dirlist:
                nrow = row + dir[0]
                ncol = col + dir[1]
                if 0<=nrow<map_size and 0<=ncol<map_size and _map[nrow][ncol]>0:
                    cnt[row][col] +=1
    
    for row in range(map_size):
        for col in range(map_size):
            if _map[row][col] > 0 and cnt[row][col]<3:
                _map[row][col] -=1

    # 인접한 얼음 확인하고 줄이기
    # _nmap = [[-100]* map_size for _ in range(map_size)]
    # for row in range(map_size):
    #     for col in range(map_size):
    #         ice_cnt = 0
    #         for dir in _dirlist:
    #             nrow = row + dir[0]
    #             ncol = col + dir[1]
    #             if 0<= nrow < map_size and 0<= ncol < map_size:
    #                 if _map[nrow][ncol] > 0 :
    #                     ice_cnt +=1
    #         if ice_cnt < 3 and _map[row][col] > 0:
    #             _nmap[row][col] = _map[row][col] - 1
    #         else:
    #             _nmap[row][col] = _map[row][col]
    # _map = _nmap
# print(_map)
print(sum([sum(row) for row in _map]))

visited = [[0]*map_size for _ in range(map_size)]

def dfs(row,col):
    global answer
    ret =  1
    _map[row][col] = 0
    for dir in _dirlist:
        nrow = row + dir[0]
        ncol = col + dir[1]
        if 0<= nrow < map_size and 0<= ncol < map_size and _map[nrow][ncol]:
            ret += dfs(nrow,ncol)
    answer = max(answer,ret)
    return ret

answer = 0 

for row in range(map_size):
    for col in range(map_size):
        if  _map[row][col] > 0:
            dfs(row,col)
print(answer)
# 가장 큰 덩어리 찾기 

# visited = [[0]*map_size for _ in range(map_size)]
# _max = -1e9

# def dfs(row,col,visited,cnt):
#     global _max
#     visited[row][col] = 1
#     _max = max(_max, cnt)
#     for dir in _dirlist:
#         nrow = row + dir[0]
#         ncol = col + dir[1]
#         if 0<= nrow < map_size and 0<= ncol < map_size:
#             pass
#         else:
#             continue
#         if not visited[nrow][ncol] and _map[nrow][ncol]:
#             dfs(nrow,ncol,visited,cnt+1)

# for row in range(map_size):
#     for col in range(map_size):
#         cnt = 0
#         if not visited[row][col] and _map[row][col]:
#             dfs(row,col,visited,cnt+1)


# Solution

# from collections import deque

# dy = (0, 1, 0, -1)
# dx = (1, 0, -1, 0)

# def rotate_and_melting(board, len_board, L):
#     """
#     Level에 맞게 회전 후 얼음을 녹임
#     :param board: 보드
#     :param len_board: 보드 길이
#     :param L: level
#     :return:
#     """
#     new_board = [[0] * len_board for _ in range(len_board)] # 회전한 Board 저장 용

#     # rotate
#     r_size = 2 ** L # 격자 사이즈
#     for y in range(0, len_board, r_size): # 격자 시작 좌표 y축
#         for x in range(0, len_board, r_size): # 격자 시작 좌표 x축
#             for i in range(r_size): # 열 인덱스
#                 for j in range(r_size): # 행 인덱스
#                     new_board[y + j][x + r_size - i - 1] = board[y + i][x + j]

#     board = new_board
#     melting_list = [] # 녹을 얼음 좌표
#     for y in range(len_board):
#         for x in range(len_board):
#             ice_count = 0
#             for d in range(len(dy)):
#                 ny = y + dy[d]
#                 nx = x + dx[d]

#                 if nx < 0 or ny < 0 or nx >= len_board or ny >= len_board:
#                     continue
#                 elif board[ny][nx] > 0:
#                     ice_count += 1

#             if ice_count < 3 and board[y][x] != 0:
#                 melting_list.append((y, x))

#     # 저장된 얼음들을 녹임
#     for y, x in melting_list:
#         board[y][x] -= 1

#     return board

# def check_ice_bfs(board, len_board):
#     """
#     얼음 상태 확인
#     :param board: 보드
#     :param len_board: 보드 가로 길이
#     :return:
#     """
#     used = [[False] * len_board for _ in range(len_board)]
#     ice_sum = 0
#     max_area_count = 0
#     for y in range(len_board):
#         for x in range(len_board):
#             area_count = 0
#             if used[y][x] or board[y][x] == 0:
#                 continue
#             # BFS를 이용하여 얼음 덩어리 조사
#             q = deque()
#             q.append((y, x))
#             used[y][x] = True

#             while q:
#                 sy, sx = q.popleft()
#                 ice_sum += board[sy][sx] # 얼음 합 추가
#                 area_count += 1  # 얼음 카운트 추가

#                 for d in range(4):
#                     ny = sy + dy[d]
#                     nx = sx + dx[d]
#                     if nx < 0 or ny < 0 or nx >= len_board or ny >= len_board or used[ny][nx]:
#                         continue
#                     if board[ny][nx] != 0:
#                         used[ny][nx] = True
#                         q.append((ny, nx))

#             max_area_count = max(max_area_count, area_count) # 최대 얼음 덩어리 크기 파악

#     print(ice_sum)
#     print(max_area_count)


# def solve():
#     N, Q = map(int, input().split(' '))
#     len_board = 2 ** N
#     board = [list(map(int, input().split(' '))) for _ in range(len_board)]
#     L_list = list(map(int, input().split(' ')))

#     for L in L_list:
#         board = rotate_and_melting(board, len_board, L)

#     check_ice_bfs(board, len_board)

# solve()

