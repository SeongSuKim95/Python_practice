# 변수 선언 및 입력:

n = int(input())
grid = [
    list(map(int, input().split()))
    for _ in range(n)
]


def in_range(x, y):
    return 0 <= x and x < n and 0 <= y and y < n


def get_score(x, y, k, l):
    dxs, dys = [-1, -1, 1, 1], [1, -1, -1, 1]
    move_nums = [k, l, k, l]
    
    sum_of_nums = 0

    # 기울어진 직사각형의 경계를 쭉 따라가봅니다.
    for dx, dy, move_num in zip(dxs, dys, move_nums):
        for _ in range(move_num):
            x, y = x + dx, y + dy
                
            # 기울어진 직사각형이 경계를 벗어나는 경우라면
            # 불가능하다는 의미로 답이 갱신되지 않도록
            # 0을 반환합니다.
            if not in_range(x, y):
                return 0
            
            sum_of_nums += grid[x][y]
    
    return sum_of_nums


ans = 0

# (i, j)를 시작으로 1, 2, 3, 4 방향
# 순서대로 길이 [k, l, k, l] 만큼 이동하면 그려지는
# 기울어진 직사각형을 잡아보는
# 완전탐색을 진행해봅니다.
for i in range(n):
    for j in range(n):
        for k in range(1, n):
            for l in range(1, n):
                ans = max(ans, get_score(i, j, k, l))

print(ans)

####### 내 풀이 ######
'''
- 기본적인 발상은 같았는데, 완탐에서 굳이 예외처리를 안해도 되는 부분에 대해 신경쓰고 있었다.
- 어차피 맵을 벗어나면 경로 탐색을 중지하므로, 좌우 범위를 확인한 후에 완탐할 필요가 없다.
'''

N = int(input())

map_ = [list(map(int,input().split())) for _ in range(N)]


dirs = [(1,-1),(1,1),(-1,1),(-1,-1)]

def sum_route(iters,coords):

    cur_i,cur_j = coords
    sum_cnt = 0
    for i in range(4):
        for k in range(iters[i]):
            cur_i, cur_j = cur_i + dirs[i][0], cur_j + dirs[i][1]
            
            if not(0<= cur_i < N and 0<= cur_j < N) :
                continue
            sum_cnt += map_[cur_i][cur_j]

    return sum_cnt

max_sum = 0
for i in range(N):
    for j in range(N):

        left_reach,right_reach = min(j,N-1-i), min(N-1-j,N-1-i)
        combi = []
        for k in range(1,left_reach + 1):
            for l in range(1, right_reach +1):

                n_i = i +  k * dirs[0][0] + l * dirs[1][0]
                n_j = j +  k * dirs[0][1] + l * dirs[1][1]

                if not(0<= n_i < N and 0<= n_j < N):
                    continue
                combi.append((k,l))

        for combis in combi:
            k,l = combis
            iters = [k,l,k,l]
            sum_cnt = sum_route(iters,(i,j))                
            max_sum = max(max_sum,sum_cnt)
                
print(max_sum)
