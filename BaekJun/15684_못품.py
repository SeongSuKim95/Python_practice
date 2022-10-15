from copy import deepcopy
# 1.사다리 타고 내려가는거 구현하기
# 기본적으로 주어지는게..
# 1 1 --> a,b  a번 위치에서 b번 사다리 --> b+1번 사다리

# 2.주어진 갯수 만큼 빈 자리에 다리 놓아보기

# 3.각 경우의 수에 따라서 i 번째 줄부터 i 번째 줄로 끝나는지 확인해보기
#  i 번째에 안끝나면 바로 종료 하기 


# N,M,H = map(int,input().split()) # 사다리 개수, 주어진 다리 개수, 높이

# _bridge_list = [list(map(int,input().split())) for _ in range(M)]

N,M,H = 5,5,6
_bridge_list = [[1,1],[3,2],[2,3],[5,1],[5,4]]

_bridge_map = [[0]*(N) for _ in range(H+1)]  # H 높이의 N개 사다리 사이에 있는 다리 개수 (map을 가로 세로 한칸씩 늘린상태)

for H,idx in _bridge_list:
    _bridge_map[H][idx] = 1
# for row in _bridge_map:
#     print(row, sep='\n')
def going_down(_map,i):

    current_x,current_y = i,1
    while current_y != H:

        if _map[current_y][current_x]:
            current_x +=1
            if _map[current_y][current_x+1]:
                continue
            else :
                current_y +=1
        else:
            current_y +=1    

    if current_x == i :
        return True
    else :
        print(i)

        return False

bridge_cnt = 0
answer = 1e9
# 다리 놓아보기
flag = False
def dfs(y,x,_map,cnt):
    global answer
    global flag
    # 사다리 타봐
    if cnt > 3 :
        return
    else:
        # 선판단
        for i in range(1,N+1):
            Success = going_down(_map,i)
            if not Success:
                    return
        if Success:
            flag = True
            answer = min(cnt,answer)
            return    

        for i in range(y,H+1):
            for j in range(x,N+1):
                if _map[i][j] == 1:
                    continue
                else:
                    _map_temp = _map.deepcopy()
                    _map_temp[i][j] = 1
                    dfs(i,j,_map_temp,cnt+1)


dfs(1,1,_bridge_map,bridge_cnt)

if not flag :
    print(-1)
else:
    print(answer)
