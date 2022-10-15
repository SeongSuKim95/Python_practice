
N, M = map(int,input().split())

_map = [list(map(int,input().split())) for _ in range(N)]
_move = [list(map(int,input().split())) for _ in range(M)]

# indexing 편의를 위해 행 열 한칸씩 추가

# 열 추가
for idx,row in enumerate(_map):
    _map[idx] = [0] + _map[idx]

# 행 추가
_nmap = [[0] * (N+1)]
for row in _map:
    _nmap.append(row)
_map = _nmap
# print(_map)
# 구름 방향
# 1부터 8
_cloud_dirlist = {1:(0,-1), 2:(-1,-1), 3:(-1,0), 4:(-1,1), 5:(0,1), 6:(1,1), 7:(1,0),8:(1,-1)}
_diaglist = [(-1,-1),(-1,1),(1,-1),(1,1)]

# 처음 위치
_cloudlist = [[N-1,1],[N-1,2],[N,1],[N,2]]

# 1 ~ N만 쓸거임 
for move in _move:

    _dir,_dist = move
    # print(_cloudlist)
    for idx in range(len(_cloudlist)):
        # 구름 s 칸 이동
        _cloudlist[idx][0] = (_cloudlist[idx][0] + _cloud_dirlist[_dir][0] * _dist) % N
        if not _cloudlist[idx][0] : _cloudlist[idx][0] = N 
        _cloudlist[idx][1] = (_cloudlist[idx][1] + _cloud_dirlist[_dir][1] * _dist) % N
        if not _cloudlist[idx][1] : _cloudlist[idx][1] = N

        # 비 내리기
        _map[_cloudlist[idx][0]][_cloudlist[idx][1]] += 1
    # print(_cloudlist)

    # 대각 방향 확인하고 물 복사    
    for cloud in _cloudlist:
        cnt = 0 
        cloud_row,cloud_col = cloud[0],cloud[1]
        for diag in _diaglist :
            try:
                if _map[cloud_row + diag[0]][cloud_col + diag[1]]:  
                    cnt +=1
            except:
                pass
        _map[cloud_row][cloud_col] += cnt
    # print(_map)
    
    # 구름 소멸 후 구름이 다시 생성
    _temp = [[1]*(N+1) for _ in range(N+1)]

    for cloud_y,cloud_x in _cloudlist:
        _temp[cloud_y][cloud_x] = 0
    
    _cloudlist = []
    for row in range(N+1):
        for col in range(N+1):
            if _map[row][col] >=2 and _temp[row][col]:
                _cloudlist.append([row,col])
                _map[row][col] -= 2
                
print(sum([sum(row) for row in _map]))