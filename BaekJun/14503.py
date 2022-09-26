import sys; input = sys.stdin.readline

N,M = map(int,input().split())
r,c,cur_dir = map(int,input().split())

board = [list(map(int,input().split())) for _ in range(N)]

# 북, 서, 남, 동
dir_list = {0:[-1,0],1:[0,-1],2:[1,0],3:[0,1]}

board[r][c] = 2
cnt = 1
while True:
    
    left_dir = cur_dir + 1
    
    if left_dir > 3 : left_dir = 0

    nr = r + dir_list[left_dir][0]
    nc = c + dir_list[left_dir][1]

    if board[nr][nc] == 0:
        board[nr][nc] = 2
        cur_dir = left_dir
        cnt += 1
        r,c = nr,nc
    else:
        f_cnt = 0
        # 네 방향 확인
        for idx, direction in dir_list.items():
            nr = r + direction[0]
            nc = c + direction[1]
            if board[nr][nc] == 1 or board[nr][nc] == 2:
                f_cnt +=1
        if f_cnt == 4:
            nr = r - dir_list[cur_dir][0]
            nc = c - dir_list[cur_dir][1]
            if board[nr][nc] == 2:
                r,c = nr,nc
                f_cnt = 0
            else:
                break
print(cnt)