# BFS를 노드 단위로 구분하는 것이 아니라 depth 단위로 구분
from collections import deque

def print_array(array):

    for row in array:
        print(row)
    print("#################################")

N = 11
test_map = [[0] * N for _ in range(N)]

visited = [[0] * N for _ in range(N)]

condition = 5

init_r, init_c = 5,5

# 상 하 좌 우 
dr = [-1,1,0,0]
dc = [0,0,-1,1]
visited[init_r][init_c] = 1

Q = deque([(init_r,init_c)])
cnt = 1

print_array(visited)

while cnt <= condition:
    
    qlen = len(Q)

    for _ in range(qlen):

        r,c = Q.popleft()
        for dir in range(4):
            
            nr = r + dr[dir]
            nc = c + dc[dir]

            if not( 0<=nr< N and 0<=nc<N ):
                continue
            if not visited[nr][nc]:
                Q.append((nr,nc))
                visited[nr][nc] = 1
                
    cnt += 1
    print(cnt)
    print_array(visited)









    






