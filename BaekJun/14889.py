import sys; input = sys.stdin.readline

N = int(input())

_map = [list(map(int,input().split())) for i in range(N)]

visited = [False] * N
result = []
_min = 1e9

def diff():
    _start = 0
    _link = 0
    for i in range(N-1):
        for j in range(i+1,N):
            #_map 순회하기
            if visited[i] and visited[j] :
                _start += _map[i][j]
                _start += _map[j][i]
            elif not visited[i] and not visited[j]:
                _link += _map[i][j]
                _link += _map[j][i]
    return abs(_start - _link)

def dfs(depth,idx,N):
    global _min
    if depth == N//2:
        # 차이를 구하는 함수
        _min = min(_min, diff())
        # 만약 차이가 0이면 최소값이므로 바로 프로그램 종료
        if _min == 0:  
            print(_min)
            exit(0)
        return
    for i in range(idx,N):
        if not visited[i]:
            visited[i] = True
            dfs(depth+1, i+1, N)
            visited[i] = False

dfs(0,0,N) # depth, idx, N



