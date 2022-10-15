import copy 


# ball1,ball2,ball3 = 0,0,0

# ball_list = [1,1,1,1,1,1,1,1,1,1,1]
# while True:
#     ball_cnt = 1
#     temp = []
#     # while True:
#     _stack = []
#     for ball in ball_list:
#         if not _stack :
#             _stack.append(ball)
#         else:
#             if ball == _stack[-1]: # 같은 구슬 나올 때
#                 ball_cnt += 1
#             else: # 다른 구슬이 나오면
#                 if ball_cnt >= 4: #만약 4번이상이면
#                     prev_ball = _stack[-1]
#                     if prev_ball == 1:
#                         ball1 += ball_cnt
#                     elif prev_ball == 2:
#                         ball2 += ball_cnt
#                     elif prev_ball == 3:
#                         ball3 += ball_cnt
#                     _stack.append(ball)
#                 else:
#                     for _ in range(ball_cnt):
#                         temp.append(_stack[-1])
#                     _stack.append(ball)
#                 ball_cnt = 1
#     if ball_cnt >=4 :
#         ball_list = []
#         break
#     else:
#         for i in range(ball_cnt):
#             temp.append(_stack[-1])
    
#     if ball_list == temp :
#         ball_list = temp
#         break
#     else:
#         ball_list = temp

# print(ball_list,ball_cnt)
# import sys; input = sys.stdin.readline

# N = int(input())

# _map = [list(map(int,input().split())) for i in range(N)]
# visited= [False] * N
# result = []
# _min = 1e9

# def diff():
#     _start = 0
#     _link = 0
#     for i in range(N-1):
#         for j in range(i+1,N): # 위 대각, 아래 대각 행렬만 보면됨
#             # _map 순회하기
#             if visited[i] and visited[j]:
#                 _start += _map[i][j]
#                 _start += _map[j][i]
#             elif not visited[i] and not visited[j]:
#                 _link += _map[i][j]
#                 _link += _map[j][i]
#     return abs(_start - _link)
    

# def dfs(depth, idx, N):
#     global _min
#     if depth == N//2:
#         diff_result = diff()
#         _min = min(_min,diff_result)
#         if _min == 0 :
#             print(_min)
#             exit(0)
#         return
#     for i in range(idx,N):
#         if not visited[i]:
#             visited[i] = True
#             dfs(depth+1,i+1,N)
#             visited[i] = False

# dfs(0,0,N) # depth, idx, N

# print(_min)

# a = [[8,3,[1,2]],[8,1,[2,3]],[8,4,[1,2]],[2,2,[1,2]],[2,2,[0,2]],[3,2,[1,2]],[2,1,[1,2]],[3,1,[1,2]]]
# a.sort()
# print(a)

# from collections import deque
# from itertools import combinations as c
# import sys

# input = sys.stdin.readline
# INF = 100000 #임의의 큰 수

# '''
# 풀이 방법 : BFS + 조합(combinations)
# 시간 복잡도 : O(n^2)
# 공간 복잡도 : O(n^2)

# 1.  완전탐색을 통해 빈 칸의 개수를 구하고, 모든 바이러스의 위치 정보 저장 
# 2.  어떤 바이러스를 활성 상태로 만들까? -> 조합(combinations)
# 3.  모든 조합 결과에 대해 활성 상태의 바이러스가 퍼지는 시간 계산하기 -> BFS 반복 수행
# 4.  결과 출력

# 옵션 1.  모든 빈 칸에 바이러스를 퍼뜨리면 종료
# 옵션 2.  바이러스를 어떻게 놓아도 모든 빈 칸에 바이러스를 퍼뜨릴 수 없는 경우에는 -1 출력 및 종료
# '''

# def bfs(q, blanks):
# 	visited = [[-1] * n for _ in range(n)] # 방문 목록

# 	time = 0 # 시간 변수를 놓는다
# 	while True:
# 		length = len(q) # 큐의 길이(=1초 동안 새롭게 추가된 바이러스의 수)
		
# 		if blanks == 0 or length == 0:
# 			if blanks == 0: # 옵션 1. 모든 빈 칸에 바이러스를 퍼뜨리면 종료
# 				return time
# 			else: # 옵션 2. 바이러스를 어떻게 놓아도 전체에 퍼뜨릴 수 없는 경우 , blank != 0 인데 length == 0
# 				return INF

# 		time += 1
# 		for i in range(length): #큐 길이만큼 반복해주는 for문이 이 문제 해결의 핵심** 이번턴에 추가된 애들만 bfs!
# 			x, y = q.popleft()
# 			if visited[x][y] == -1:
# 				visited[x][y] = 1 # 방문 처리

# 			for d in range(4):
# 				nx = x + dx[d]
# 				ny = y + dy[d]

# 				if 0<=nx<n and 0<=ny<n:
# 					if visited[nx][ny] == -1: #아직 방문하지 않은 칸에 대해
# 						if board[nx][ny] == 0: # case 1: 빈 칸을 만난 경우
# 							q.append((nx, ny))
# 							visited[nx][ny] = 1 # 방문 처리
# 							blanks -= 1 # 빈칸 채웠으니까 한칸 빼기
# 						elif board[nx][ny] == 2: # case 2: 비활성된 바이러스를 만난 경우
# 							q.append((nx, ny))
# 							visited[nx][ny] = 1 # 원래 빈칸이 아니었으니 안빼도 됨

# n, m = map(int, input().rstrip('\n').split())
# board = [list(map(int, input().rstrip('\n').split())) for _ in range(n)]

# virus_pos = [] # 바이러스 위치 정보 저장
# blank_cnt = 0 # 빈 칸의 개수

# # 1. 완전탐색을 통해 빈 칸의 개수를 구하고, 모든 바이러스의 위치 정보 저장 : O(N^2)
# for i in range(n):
# 	for j in range(n):
# 		if board[i][j] == 0:
# 			blank_cnt += 1
		
# 		elif board[i][j] == 2:
# 			virus_pos.append((i, j))

# # BFS를 위한 방향벡터 설정
# dx = [-1, 1, 0, 0]
# dy = [0, 0, 1, -1]

# # 2. 어떤 바이러스를 활성 상태로 만들까? -> 조합(combinations) 사용
# virus_combi = c(virus_pos, m)
# res = INF

# for virus_list in virus_combi: #모든 조합 결과에 대하여
# 	q = deque() 
# 	for virus in virus_list:
# 		q.append(virus)

# 	tmp = bfs(q, blank_cnt) #= 수행 # 빈칸 개수를 미리 센다
# 	res = min(res, tmp)

# if res == INF: # 옵션 2. 바이러스를 어떻게 놓아도 전체에 퍼뜨릴 수 없는 경우
# 	print(-1)
# else:
# 	print(res)



# from collections import deque

# N = int(input())
# _map = [list(map(int, input().split())) for _ in range(N)]
# _dirlist = [[-1,0],[0,-1],[0,1],[1,0]] # 상 좌 우 하 로 놓고 코딩해야 문제 조건에 일치

# for row in range(N):
#     for col in range(N):
#         if _map[row][col] == 9:
#             shark_x,shark_y = row,col
#             _map[row][col] = 0 #상어 자리 0으로

# maxsize = 1e9

# def bfs():
#     global shark_x, shark_y, cnt

#     q = deque([(shark_x, shark_y)])
#     visited = [[-1] * N for _ in range(N)]
#     visited[shark_x][shark_y] = 0
#     min_dist = maxsize
#     fish = []

#     while q:
#         x, y = q.popleft()

#         if 0 < _map[x][y] < shark_size: # 상어보다 작은 물고기면!
#             min_dist = min(min_dist, visited[x][y])
#             if visited[x][y] == min_dist:
#                 fish.append((x, y))
#             else:
#                 break
        
#         for dir in _dirlist:
#             nx, ny = x + dir[0], y + dir[1]

#             if not 0 <= nx < N or not 0 <= ny < N:
#                 continue
#             if _map[nx][ny] > shark_size or visited[nx][ny] != -1: #상어 사이즈보다 크거나 방문 했던 곳이면
#                 continue

#             # 상어 사이즈랑 같거나 0 이면
#             q.append((nx, ny))
#             visited[nx][ny] = visited[x][y] + 1 # 표시해나가며 가기(거리 표기)
#     print(visited)
#     if fish:
#         fish.sort()
#         x, y = fish[0]
#         print(fish)
#         shark_x, shark_y, cnt = x, y, cnt + 1
#         _map[shark_x][shark_y] = 0
#         return min_dist
#     else:
#         return -1

# ans = 0
# shark_size, cnt = 2, 0

# while True:
#     sec = bfs() # bfs에서 시간을 return
#     if sec == -1: # 물고기를 다 먹었거나 더이상 먹을 수 없는 경우
#         break
#     ans += sec

#     if cnt == shark_size:
#         shark_size += 1
#         cnt = 0

# print(ans)


# 1번 상어는 모두 쫓아낼 수 있음
# N * N 그래프에 M 마리의 상어, k = 냄새 지속시간
# n, m, k = map(int, input().split())
# graph = []
# sharks = [[] for _ in range(m + 1)]

# # 위, 아래, 왼쪽, 오른쪽
# moves = [
#     [],
#     [-1, 0],
#     [1, 0],
#     [0, -1],
#     [0, 1]
# ]

# for i in range(n):
#     row = list(map(int, input().split()))
#     for j in range(n):
#         if row[j] != 0:
#             sharks[row[j]].append([i, j])
    
#     graph.append(row)

# current_d_list = list(map(int, input().split()))

# for i in range(1, m + 1):
#     sharks[i].append(current_d_list[i - 1])

# sharks_preference = {}
# for i in range(1, m + 1):
#     sharks_preference[i] = [0]
#     for j in range(1, 5):
#         sharks_preference[i].append(list(map(int, input().split())))

# """
# sharks[i][0]: i번째 상어의 현재 위치
# sharks[i][1]: i번째 상어가 현재 바라보는 방향
# """

# """
# sharks_preference[i][j]: i번째 상어가 j방향을 보고 있을 때 방향 우선순위 리스트
# """

# # stage
# # 1. 움직인다. (냄새 정보 확인) 
# # 아무 냄새가 없는 칸으로 먼저 이동 / 자신의 냄새가 있는 칸으로 (가능한 칸이 여러개일 경우 우선순위를 따름)
# # 2. 겹치는지 확인한다. (죽는 상어가 있는지 확인)
# # 3. 냄새를 기록 및 업데이트한다.


# graph_smell = [[[0, 0] for _ in range(n)] for _ in range(n)]
# # 첫 냄새 기록
# for i in range(1, m + 1):
#     graph_smell[sharks[i][0][0]][sharks[i][0][1]][0], graph_smell[sharks[i][0][0]][sharks[i][0][1]][1] = i, k


# # 내 냄새가 있는 방향 확인
# def my_smell_check(graph_smell, shark_num):
#     current_shark_loc = sharks[shark_num][0]
#     current_shark_d = sharks[shark_num][1]
#     preferences = sharks_preference[shark_num][current_shark_d]

#     for direction in preferences:
#         x, y = current_shark_loc[0] + moves[direction][0], current_shark_loc[1] + moves[direction][1]

#         if 0 <= x < n and 0 <= y < n:
#             if graph_smell[x][y][0] == shark_num:

#                 return [x, y, direction]

# # 비어있는 공간 확인
# def empty_check(graph_smell, shark_num):
#     current_shark_loc = sharks[shark_num][0]
#     current_shark_d = sharks[shark_num][1]
#     preferences = sharks_preference[shark_num][current_shark_d]

#     for preference in preferences:
#         x, y = current_shark_loc[0] + moves[preference][0], current_shark_loc[1] + moves[preference][1]

#         if 0 <= x < n and 0 <= y < n:
#             if graph_smell[x][y][0] == 0:
#                 return [x, y, preference]
    
#     # 빈 곳이 없으면 False 리턴
#     return False
    
# # 죽는 상어가 있는지 확인
# def check_shark_dead():
#     dead_num = 0
#     for i in range(1, m):
#         if sharks[i][0] == -1:
#             continue

#         for j in range(i + 1, m + 1):
#             if sharks[j][0] == -1:
#                 continue
            
#             i_shark_loc = sharks[i][0]
#             j_shark_loc = sharks[j][0]

#             if i_shark_loc == j_shark_loc:
#                 dead = max(i, j)
#                 sharks[dead][0] = -1
#                 dead_num += 1
    
#     return dead_num

# # 살아있는 상어의 수
# remain_shark = m
# # 이동 횟수
# ans = 0
# # 현재 상어위치 기록 (냄새 기록을 위한 위치)
# current_loc_shark = [[0, 0]] * (m + 1)

# while remain_shark > 1 and ans < 1001:
#     # 상어 움직임
#     for i in range(1, m + 1):
#         # 현재 상어가 죽어있다면 건너뜀
#         if sharks[i][0] == -1:
#             continue

#         current_loc = sharks[i][0]
#         current_loc_shark[i] = current_loc
#         empty_move = empty_check(graph_smell, i)

#         # 비어있는 곳부터 탐색
#         if empty_move:
#             # 비어있는 곳 중 이동할 곳이 있다면 해당 위치로 이동 후 sharks 리스트 업데이트
#             new_loc_x, new_loc_y, new_d = empty_move[0], empty_move[1], empty_move[2]
#             sharks[i][0][0], sharks[i][0][1] = new_loc_x, new_loc_y
#             sharks[i][1] = new_d
        
#         else:
#             # 비어있는 곳 없을 때 자신의 냄새 있는 곳 탐색, 이동 후 sharks 리스트 업데이트
#             smell_move = my_smell_check(graph_smell, i)
#             new_loc_x, new_loc_y, new_d = smell_move[0], smell_move[1], smell_move[2]
#             sharks[i][0][0], sharks[i][0][1] = new_loc_x, new_loc_y
#             sharks[i][1] = new_d

#     # 죽은 상어 있는지 확인 후 업데이트
#     dead_num = check_shark_dead()
#     remain_shark -= dead_num

#     # 기존 존재하던 냄새 업데이트 (1 빼줌)
#     for i in range(n):
#         for j in range(n):
#             if graph_smell[i][j][0] != 0:
#                 graph_smell[i][j][1] -= 1
            
#             if graph_smell[i][j][1] == 0:
#                 graph_smell[i][j][0] = 0

#     # 살아있는 상어에 대하여 새로운 냄새 생성
#     for i in range(1, m + 1):
#         if sharks[i][0] != -1:
#             x, y = current_loc_shark[i][0], current_loc_shark[i][1]
#             graph_smell[x][y] = [i, k]
    
#     ans += 1

# if ans > 1000:
#     print(-1)
# else:
#     print(ans)

# import copy

# def move_fish():
#     """
#     물고기 이동
#     1. 상어가 있는 칸, 물고기 냄새 칸, 벗어나는 칸 x 
#     2. 45도 반시계 회전 후 이동. 이동 못하는 경우 그대로 
#     :return:
#     """
#     res = [[[] for _ in range(4)] for _ in range(4)]
#     for x in range(4):
#         for y in range(4):
#             while temp[x][y]:
#                 d = temp[x][y].pop()
#                 for i in range(d, d - 8, -1):
#                     i %= 8
#                     nx, ny = x + f_dx[i], y + f_dy[i]
#                     if (nx, ny) != shark and 0 <= nx < 4 and 0 <= ny < 4 and not smell[nx][ny]:
#                         res[nx][ny].append(i)
#                         break
#                 else:
#                     res[x][y].append(d)
#     return res

# def dfs(x, y, dep, cnt, visit):
#     """
#     상어 3칸 이동
#     1. 제외되는 물고기 수가 많고 > 이동방법 사전순(백트래킹하면 자동으로 됨) 
#     2. 이동한 곳을 저장 > 물고기 냄새가 됨  
#     """
#     global max_eat, shark, eat
#     if dep == 3:   # 3번 이동한 경우 그만 
#         if max_eat < cnt:
#             max_eat = cnt
#             shark = (x, y)
#             eat = visit[:]
#         return
#     for d in range(4):
#         nx = x + dx[d]
#         ny = y + dy[d]
#         if 0 <= nx < 4 and 0 <= ny < 4:
#             if (nx, ny) not in visit:  # 처음 방문, cnt에 죽은 물고기 수 추가  
#                 visit.append((nx, ny))
#                 dfs(nx, ny, dep + 1, cnt + len(temp[nx][ny]), visit)
#                 visit.pop()
#             else:  # 방문한 경우
#                 dfs(nx, ny, dep + 1, cnt, visit)

# #       ←, ↖,   ↑,  ↗, →, ↘, ↓, ↙
# f_dx = [0, -1, -1, -1, 0, 1, 1, 1]
# f_dy = [-1, -1, 0, 1, 1, 1, 0, -1]
# dx = [-1, 0, 1, 0]
# dy = [0, -1, 0, 1]

# m, s = map(int, input().split())
# fish = [list(map(int, input().split())) for _ in range(m)]
# graph = [[[] for _ in range(4)] for _ in range(4)]

# for x, y, d in fish:
#     graph[x - 1][y - 1].append(d - 1)

# shark = tuple(map(lambda x: int(x) - 1, input().split()))
# smell = [[0] * 4 for _ in range(4)]

# for _ in range(s):
#     eat = list()
#     max_eat = -1
#     # 1. 모든 물고기 복제
#     temp = copy.deepcopy(graph)
#     # 2. 물고기 이동
#     temp = move_fish()
#     # 3. 상어이동 - 백트래킹
#     dfs(shark[0], shark[1],0, 0, list())
#     for x, y in eat:
#         if temp[x][y]:
#             temp[x][y] = []
#             smell[x][y] = 3   # 3번 돌아야 없어짐
#     # 4. 냄새 사라짐 
#     for i in range(4):
#         for j in range(4):
#             if smell[i][j]:
#                 smell[i][j] -= 1
#     # 5. 복제 마법
#     for i in range(4):
#         for j in range(4):
#             graph[i][j] += temp[i][j]

# # 물고기 수 구하기 
# answer = 0
# for i in range(4):
#     for j in range(4):
#         answer += len(graph[i][j])

# print(answer)

"""
상어초등학교
"""


dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]


n = int(input())
arr = [[0]*n for _ in range(n)]
## 한 번에 정보를 받음
students = [list(map(int, input().split())) for _ in range(n**2)]

## 학생 수 만큼 for문을 돌며 자리에 앉혀 줌.
for order in range(n**2):
    student = students[order]
    ## 여기다가 가능한 자리를 다 담아서 정렬 후 앉힘
    tmp = []
    for i in range(n):
        for j in range(n):
            if arr[i][j] == 0:
                like = 0
                blank = 0
                for k in range(4):
                    nr, nc = i + dr[k], j + dc[k]
                    if 0 <= nr < n and 0 <= nc < n:
                        if arr[nr][nc] in student[1:]:
                            like += 1
                        if arr[nr][nc] == 0:
                            blank += 1
                tmp.append([like, blank, i, j])
    ### !!!! like, blank는 클 수록, 행과 열의 수는 작을수록 답이니 lambda 뒤의 조건을 잘 줘야함!!!
    tmp.sort(key= lambda x:(-x[0], -x[1], x[2], x[3]))
    ### 정렬 후 젤 앞에 있는 리스트의 행과 열의 번호에 학생 앉히기 
    arr[tmp[0][2]][tmp[0][3]] = student[0]

result = 0
## 점수를 매길 때는 학생 순서대로 점수 주기 위해 정렬함 
students.sort()

for i in range(n):
    for j in range(n):
        ans = 0
        for k in range(4):
            nr, nc = i + dr[k], j + dc[k]
            if 0 <= nr < n and 0 <= nc < n:
                if arr[nr][nc] in students[arr[i][j]-1]:
                    ans += 1
        if ans != 0:
            result += 10 ** (ans-1)
print(result)

"""
상어 중학교
"""

from collections import deque

# 인접 블록 찾기 -> 블록 크기, 무지개크기, 블록좌표 리턴
def bfs(x, y, color):
    q = deque()
    q.append([x, y])
    dx = [-1, 0, 1, 0]
    dy = [0, 1, 0, -1]

    block_cnt, rainbow_cnt = 1, 0  # 블록개수, 무지개블록 개수
    blocks, rainbows = [[x,y]], []  # 블록좌표 넣을 리스트, 무지개좌표 넣을 리스트

    while q:
        x, y = q.popleft()
        for d in range(4):
            nx = x + dx[d]
            ny = y + dy[d]
            
            # 범위 안이면서 방문 안한 일반 블록인 경우
            if 0 <= nx < N and 0 <= ny < N and not visited[nx][ny] and a[nx][ny] == color:
                visited[nx][ny] = 1
                q.append([nx, ny])
                block_cnt += 1
                blocks.append([nx, ny])
                
            # 범위 안이면서 방문 안한 무지개 블록인 경우
            elif 0 <= nx < N and 0 <= ny < N and not visited[nx][ny] and a[nx][ny] == 0:
                visited[nx][ny] = 1
                q.append([nx, ny])
                block_cnt += 1
                rainbow_cnt += 1
                rainbows.append([nx, ny])

    # 무지개블록은 방문 다시 해제
    for x,y in rainbows:
        visited[x][y] = 0

    return [block_cnt, rainbow_cnt, blocks+rainbows]


# 블록 제거 함수
def remove(block):
    for x,y in block:
        a[x][y] = -2


# 중력 함수
def gravity(a):
    for i in range(N-2, -1, -1):  # 밑에서 부터 체크
        for j in range(N):
            if a[i][j] > -1:  # -1이 아니면 아래로 다운
                r = i
                while True:
                    if 0<=r+1<N and a[r+1][j] == -2:  # 다음행이 인덱스 범위 안이면서 -2이면 아래로 다운
                        a[r+1][j] = a[r][j]
                        a[r][j] = -2
                        r += 1
                    else:
                        break


# 반시계 회전 함수
def rot90(a):
    new_a = [[0]*N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            new_a[N-1-j][i] = a[i][j]
    return new_a



# 0. 메인코드
N, M = map(int, input().split())
a = [list(map(int, input().split())) for _ in range(N)]

score = 0  # 점수

# 1. 오토플레이-> while {2. 크기 가장 큰 블록 찾기 3. 블록제거+점수더하기 4. 중력 5. 90회전 6. 중력}
while True:
    # 2. 크기 가장 큰 블록 찾기
    visited = [[0] * N for _ in range(N)]  # 방문체크
    blocks = []  # 가능한 블록 그룹들 넣을 리스트
    for i in range(N):
        for j in range(N):
            if a[i][j] > 0 and not visited[i][j]:  # 일반블록이면서 방문 안했으면
                visited[i][j] = 1  # 방문
                block_info = bfs(i, j, a[i][j])  # 인접한 블록 찾기
                # block_info = [블록크기, 무지개블록 개수, 블록좌표]
                if block_info[0] >= 2:
                    blocks.append(block_info)
    blocks.sort(reverse=True)

    # 3. 블록제거+점수더하기
    if not blocks:
        break
    remove(blocks[0][2])
    score += blocks[0][0]**2

    # 4. 중력
    gravity(a)

    # 5. 90회전
    a = rot90(a)

    # 6. 중력
    gravity(a)

print(score)


""" 
어른 상어
"""

# 상 하 좌 우 
_dirlist = [[0,0],[-1,0],[1,0],[0,-1],[0,1]]

N,M,K = map(int,input().split())

_map = [list(map(int,input().split())) for _ in range(N)]

shark_list = [[] for _ in range(M+1)]

# 상어의 좌표 받기
for row in range(N):
    for col in range(N):
        if _map[row][col] != 0 :
            shark_list[_map[row][col]].append([row,col])

sdir_list = list(map(int,input().split()))

for i in range(1,M+1):
    shark_list[i].append(sdir_list[i-1])

# print(shark_list)
shark_prior = {}
for i in range(1,M+1):
    shark_prior[i] = [0]
    for j in range(1,5):
        shark_prior[i].append(list(map(int,input().split())))
"""        
 필요한 것
 
 1.현재 상어들의 상태를 나타내는 list (좌표, 방향)    
 2.상어 냄새 번호와 남은 초수
"""

# 초기 상태 냄새 기록
# 상어 번호와 , 남은 초 수 

smell_map = [[[0,0] for _ in range(N)] for _ in range(N)]
# print(smell_map)

for i in range(1,M+1):
    # row , col
    smell_map[shark_list[i][0][0]][shark_list[i][0][1]][0] = i
    smell_map[shark_list[i][0][0]][shark_list[i][0][1]][1] = K

# 살아 있는 상어의 수
remain_shark = M
# 이동 수
ans = 0
# 현재 상어위치 기록 (냄새 기록을 위한 위치) buffer 역할
current_loc_shark = [[0,0]] * (M+1)

def empty_check(smell_map,shark_idx):

    current_shark_loc = shark_list[shark_idx][0]
    current_shark_dir = shark_list[shark_idx][1]
    cur_prior = shark_prior[shark_idx][current_shark_dir]
    
    # prior direction 순서대로 
    for dir in cur_prior:
        x, y = current_shark_loc[0] + _dirlist[dir][0], current_shark_loc[1] + _dirlist[dir][1]

        if 0<= x < N and 0<= y < N:
            if smell_map[x][y][0] == 0 : # 빈칸이면
                return [x,y,dir] # 이동한 위치, 방향
    return False

def smell_check(smell_map,shark_idx):

    current_shark_loc = shark_list[shark_idx][0]
    current_shark_dir = shark_list[shark_idx][1]
    cur_prior = shark_prior[shark_idx][current_shark_dir]

    for dir in cur_prior:
        x,y = current_shark_loc[0]+_dirlist[dir][0],current_shark_loc[1]+_dirlist[dir][1]
        
        if 0<=x< N and 0<=y<N:
            if smell_map[x][y][0] == shark_idx:
                return [x,y,dir]

def check_shark_dead():
    # 겹치는 상어가 있는지 확인하는 작업
    dead_num = 0
    for i in range(1,M):
        if shark_list[i][0] == -1: # 죽은 상어
            continue
        for j in range(i+1,M+1):

            if shark_list[j][0] == -1: # 죽은 상어
                continue
            if shark_list[i][0] == shark_list[j][0]: #위치가 겹치면 큰 값이 죽음
                shark_list[j][0] = -1
                dead_num += 1
    return dead_num

while remain_shark > 1 and ans < 1001:
    # 상어 움직임
    for i in range(1,M+1): # 각 상어에 대해
        if shark_list[i][0] == -1 : # 죽으면 -1로 표기
            continue

        current_loc = shark_list[i][0]
        current_loc_shark[i] = current_loc # 미리 저장
        
        empty_move = empty_check(smell_map,i)

        # 갈 수 있으면 바뀐 위치와 방향 [x,y,dir], 갈 수 없으면 False

        if empty_move: #갈 수 있으면 상어 위치 update
            new_sx,new_sy,new_dir = empty_move[0],empty_move[1],empty_move[2]
            shark_list[i][0][0], shark_list[i][0][1] = new_sx, new_sy
            shark_list[i][1] = new_dir
        else: # 갈 수 없으면 내 냄새 찾기
            # 비어있는 곳 없을 때 자신의 냄새 있는 곳 탐색
            smell_move = smell_check(smell_map,i)
            new_sx,new_sy,new_dir = smell_move[0],smell_move[1],smell_move[2]
            shark_list[i][0][0], shark_list[i][0][1] = new_sx, new_sy
            shark_list[i][1] = new_dir
        
    # 죽은 상어 있는지 확인
    dead_num = check_shark_dead()
    remain_shark -= dead_num # 남은 상어를 세는것과 1번 상어만 남는 것이 동치이다.

    for row in range(N):
        for col in range(N):
            if smell_map[row][col][0] != 0 : # 냄새 업데이트 1씩 빼줌
                smell_map[row][col][1] -= 1
            
            if smell_map[row][col][1] == 0 : # 냄새가 다 사라지면 할당 상어 없애기
                smell_map[row][col][0] = 0
    

    # 다음 위치에 대한 정보를 list로 넘기고 현재 위치에 대한 냄새를 loop의 끝에서 update한다.
    # 현재 위치 기준으로 냄새 생성
    
    for i in range(1,M+1):
        if shark_list[i][0] != -1 : # 상어가 죽지 않았다면
            x,y = current_loc_shark[i][0],current_loc_shark[i][1]
            smell_map[x][y] = [i,K]
    
    ans += 1

if ans > 1000:
    print(-1)
else:
    print(ans)



"""
마법사 상어와 복제
"""

import copy

def move_fish():
    res = [[[] for _ in range(4)] for _ in range(4)]

    for row in range(4):
        for col in range(4):
            while temp[row][col]: # row,col에 있는 모든 물고기에 대해
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

f_dx = [0,-1,-1,-1,0,1,1,1]
f_dy = [-1,-1,0,1,1,1,0,-1]
dx = [-1,0,1,0]
dy = [0,-1,0,1]

M,S = map(int,input().split())
fish = [list(map(int,input().split())) for _ in range(M)]
_map = [[[] for _ in range(4)] for _ in range(4)] # fish 맵과 smell 맵을 따로 
# fish 맵의 element를 빈리스트로 쓰기

for x,y,d in fish:
    _map[x-1][y-1].append(d-1)

shark = tuple(map(lambda x: int(x)-1, input().split())) # 상어 좌표
smell = [[0] * 4 for _ in range(4)]

for _ in range(S):
    eat = []
    max_eat = -1
    # 1. 모든 물고기 복제하기
    temp = copy.deepcopy(_map)
    # 2. 물고기 이동
    temp = move_fish()
    # 3. 상어 이동
    dfs(shark[0],shark[1],0,0,list()) # depth, count, visit

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

