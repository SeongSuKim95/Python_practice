from itertools import combinations
import sys; input = sys.stdin.readline

N,M = map(int,input().split())

board = [list(map(int,input().split())) for _ in range(N)]
max_board = max(map(max,board)) # 2차원 array의 max값 찾기 

visited = [[False]* M for _ in range(N)]

# 상 하 좌 우
move = [(0,1), (0,-1), (1,0), (-1,0)]

exec_comb = list(combinations(move,3))
# 최대값 변수를 전역 변수로 선언 후 max 함수로 그때 그때 비교
maxvalue = 0 

def dfs(i,j,sum,cnt):

    global maxvalue

    # BackTracking이 추가
    # 탐색 도중 앞으로 더 탐색하여도 현재까지의 최댓값을 넘기지 못한다고 판단할 경우 바로 종료

    if sum + max_board * (4 - cnt) <= maxvalue:
        return

    if cnt == 4 :
        maxvalue = max(maxvalue,sum)
        return # 4개 짜리 블록에 대해 maxvalue 판단 이후 return!
    
    for n in range(4): # move를 바탕으로 근처 블록을 이어나가기

        ni = i + move[n][0]
        nj = j + move[n][1]
        if 0 <= ni < N and 0 <= nj < M and not visited[ni][nj]:
            if cnt == 2:
                visited[ni][nj] = True
                dfs(i,j,sum + board[ni][nj],cnt+1)
                visited[ni][nj] = False
            
            visited[ni][nj] = True
            dfs(ni,nj,sum + board[ni][nj],cnt+1)
            visited[ni][nj] = False

# ㅗ를 따로 처리하기 위해 코드를 짜면 시간초과가 뜨네요...
# def exce(i,j):

#     global maxvalue

#     for comb in exec_comb:
#         temp = board[i][j]
#         for dir in comb:
#             ni = i + dir[0]
#             nj = j + dir[1]
#             if 0 <= ni < N and 0 <= nj < M : 
#                 temp += board[ni][nj]
#             else :
#                 break
#         maxvalue = max(maxvalue,temp)    

for i in range(N):
    for j in range(M):
        # 시작점 방문 표시

        visited[i][j] = True
        dfs(i,j,board[i][j],1) # 현재 위치(i,j)와 board, 블록을 셀 변수(1) 넘겨주기
        visited[i][j] = False

        #  exce(i,j) # ㅗ자모양 블록 계산

print(maxvalue)
        

        