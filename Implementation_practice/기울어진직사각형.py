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
