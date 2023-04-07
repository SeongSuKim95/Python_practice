import sys

N,M,K = list(map(int,input().split()))

lst = list(map(int,input().split()))

seqs = []
visited = [False] * N
min_weight = 1e9

def work(lst):

    cnt = 0 
    cur_box = M
    idx = 0
    total_weight = 0
    while cnt < K :
        
        cur_weight = lst[idx]
        
        temp_box = cur_box - cur_weight
        
        if temp_box < 0 :
            cnt += 1
            cur_box = M
        elif temp_box == 0:
            cnt += 1
            cur_box = M
            idx = (idx + 1 + N) % N
            total_weight += cur_weight
        else :
            total_weight += cur_weight
            idx = (idx + 1 + N) % N
            cur_box = temp_box

    return total_weight
    
def dfs(cnt):
    global min_weight

    if cnt == N :
        min_weight = min(min_weight,work(seqs))
        return

    for i in range(N):
        if not visited[i]:
            visited[i] = True
            seqs.append(lst[i])
            dfs(cnt+1)
            seqs.pop()
            visited[i] = False
dfs(0)
print(min_weight)