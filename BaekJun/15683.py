import sys; input = sys.stdin.readline
import copy

# CCTV 종류별, 바라보는 방향별 감시영역 재귀적 탐색


def dfs(graph,depth):
    global answer
    # 종료 조건! 언제 return 하는가 (또 무엇을 어떻게 리턴할 것인가?)
    if depth == len(cctv_list):
        answer = min(answer, count(graph))
    else:
        # 경우의 수에 따라 바뀌는 것 : 맵! 맵은 deepcopy 
        graph_copy = copy.deepcopy(graph)
        x,y,cctv_type = cctv_list[depth]
        for cctv_dir in cctv_direction[cctv_type]:
            watch(x,y,cctv_dir,graph_copy)
            dfs(graph_copy,depth + 1) # 바뀐 맵을 들고 dfs 수행
            graph_copy = copy.deepcopy(graph)

def watch(x,y,direction,graph):
    for d in direction:
        nx,ny = x,y
        while True :
            nx += direction_list[d][0]
            ny += direction_list[d][1]
            if 0 <= nx < N and 0 <= ny < M :
                if graph[nx][ny] == 6 :
                    break
                elif graph[nx][ny] == 0 :
                    graph[nx][ny] = "#"
            else : 
                break

def count(graph):
    cnt = 0
    for i in range(N):
        for j in range(M):
            if graph[i][j] == 0:
                cnt +=1
    return cnt

if __name__ == '__main__':
    N, M = map(int, input().split())
    graph = [list(map(int, input().split())) for _ in range(N)]

    answer = int(1e9)
    cctv_list = []
    # map에 있는 cctv 위치, 종류 저장
    for i in range(N):
        for j in range(M):
            if 1<= graph[i][j] <= 5 :
                cctv_list.append((i,j,graph[i][j])) # tuple로 저장
    # 탐색 방향 : 상 하 좌 우
    direction_list = [(-1,0),(1,0),(0,-1),(0,1)]

    cctv_direction = [
        [],
        [[0],[1],[2],[3]],
        [[0,1],[2,3]],
        [[0,2],[0,3],[1,2],[1,3]],
        [[0,1,2],[0,1,3],[0,2,3],[1,2,3]],
        [[0,1,2,3]]
    ]

    dfs(graph,0) # 변하는게 무엇인가?--> graph ,무엇에 따라 변하는가? --> depth
    print(answer) 