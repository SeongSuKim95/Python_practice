

N,M = map(int,input().split())

_map = [list(map(int,input().split())) for _ in range(N)]

# map에 아무것도 없는 경우.. 바로 끝내기 
if _map == [[0]*N for _ in range(N)]:
    print(0)
    exit()
magic = [list(map(int,input().split())) for _ in range(M)]

# 마법 방향 상 하 좌 우
magic_dirlist = {1: [-1,0], 2: [1,0], 3:[0,-1], 4:[0,1]}

# 탐색 방향 좌 하 우 상
_dirlist = {1: [0,-1], 2: [1,0], 3:[0,1], 4:[-1,0]}

cur_x, cur_y = int(N//2), int(N//2)

init_dir = 1 # 항상 시작점에서 왼쪽 방향 부터 

M = int((N**2/2 - 3) / 4) + 1

# 탐색 좌표 리스트 하나 생성

coord_list = []
dir_seq = []
cnt = 0
ball1,ball2,ball3 = 0,0,0
while len(dir_seq) <= N*N:
    dir_seq += [1]*(2*cnt+1) + [2]*(2*cnt+1) + [3]*(2*cnt+2) + [4]*(2*cnt+2)
    cnt +=1

for i in range(N*N):
    try:
        coord_list.append((cur_x,cur_y))
        cur_x += _dirlist[dir_seq[i]][0]
        cur_y += _dirlist[dir_seq[i]][1]
    except:
        break
for magic_dir, dist in magic:
    # 각 마법에 대해서
    attack_x,attack_y = int(N//2),int(N//2)
    for i in range(dist):
        attack_y += magic_dirlist[magic_dir][0]
        attack_x += magic_dirlist[magic_dir][1]
        try:
            _map[attack_y][attack_x] = 0 
        except:
            pass

    # 구슬 땡기기
    ball_list = []
    _nmap = [[0]*N for _ in range(N)]
    for coord_x,coord_y in coord_list:
        try:
            cur_ball = _map[coord_x][coord_y]
            if cur_ball != 0 :
                ball_list += [cur_ball]
        except:
            pass
    # original = ball_list[:]
    
    # 연속된 4개 이상의 같은 구슬 제거하기
    while True:
        ball_cnt = 1
        temp = []
        # while True:
        _stack = []
        for ball in ball_list:
            if not _stack :
                _stack.append(ball)
            else:
                if ball == _stack[-1]: # 같은 구슬 나올 때
                    ball_cnt += 1
                else: # 다른 구슬이 나오면
                    if ball_cnt >= 4: #만약 4번이상이면
                        prev_ball = _stack[-1]
                        if prev_ball == 1:
                            ball1 += ball_cnt
                        elif prev_ball == 2:
                            ball2 += ball_cnt
                        elif prev_ball == 3:
                            ball3 += ball_cnt
                        _stack.append(ball)
                    else:
                        for _ in range(ball_cnt):
                            temp.append(_stack[-1])
                        _stack.append(ball)
                    ball_cnt = 1
        
        if ball_cnt >=4:
            prev_ball = _stack[-1]
            if prev_ball == 1:
                ball1 += ball_cnt
            elif prev_ball == 2:
                ball2 += ball_cnt
            elif prev_ball == 3:
                ball3 += ball_cnt
            ball_list = []
            break
        else:
            for i in range(ball_cnt):
                temp.append(_stack[-1])
        
        if ball_list == temp :
            ball_list = temp
            break
        else:
            ball_list = temp
            
    # 새로 할당
    if not ball_list :
        break
    else:
        _stack = []
        ball_cnt = 1
        new_ball_list = []
        for ball in ball_list:
            if not _stack:
                _stack.append(ball)
            else:
                if _stack[-1] == ball :
                    ball_cnt +=1
                else:
                    new_ball_list.append(ball_cnt)
                    new_ball_list.append(_stack[-1])
                    _stack.append(ball)
                    ball_cnt = 1

        new_ball_list.append(ball_cnt)
        new_ball_list.append(_stack[-1])

        # 새롭게 맵 할당 (상어 있는 곳 고려)
        new_ball_list = [0] + new_ball_list
        for idx,ball in enumerate(new_ball_list):
            try:
                _nmap[coord_list[idx][0]][coord_list[idx][1]] = ball
            except:
                pass
        _map =_nmap
   

print(ball1 + 2*ball2 + 3*ball3)