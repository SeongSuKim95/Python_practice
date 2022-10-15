N,M = map(int,input().split())

_map = [list(map(int,input().split())) for _ in range(N)]

_chicken = []

for i in range(N):
    for j in range(N):
        if _map[i][j] == 2 :
            _chicken.append((i,j))


# 각 집에서 가장 가까운 치킨 집 거리 구하기
def _chicken_dist(x,y,chicken_list):

    chicken_dist = 1e9
    for chicken in chicken_list:
        chicken_dist = min(chicken_dist,abs(chicken[0] - x)+abs(chicken[1] -y))

    return chicken_dist


num_chicken = len(_chicken)
visited = [True] * num_chicken
dist_sum = 1e9

# 치킨 집 M개만 남겨 놓고 도시 치킨 거리 구하기

def dfs(idx,depth,visited,M):
    global dist_sum
    # 종료 조건
    # print(idx,depth,visited)
    if depth == num_chicken - M: #3
        chicken_list = []
        for idx,i in enumerate(visited):
            if i :
                chicken_list.append(_chicken[idx])
        temp_sum = 0
        for i in range(N):
            for j in range(N):
                if _map[i][j] == 1:
                    temp_sum += _chicken_dist(i,j,chicken_list)
        dist_sum = min(dist_sum,temp_sum)
    else :
        for i in range(idx,num_chicken): 
            visited[i] = False
            dfs(i+1,depth+1,visited,M)
            visited[i] = True

dfs(0,0,visited,M) # idx, depth, M

print(dist_sum)
