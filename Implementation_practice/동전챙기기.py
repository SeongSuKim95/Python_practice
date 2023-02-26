N = int(input())

map_ = [
    input()
    for _ in range(N)
]

min_dist = 1e9

start,end = (-1,-1),(-1,-1)
nums = []
for i in range(N):
    for j in range(N):
        if map_[i][j] == "S":
            start = (i,j)
        if map_[i][j] == "E":
            end = (i,j)
        if map_[i][j].isdigit():
            nums.append((map_[i][j],i,j))

nums = [(i[1],i[2]) for i in sorted(nums,key = lambda x : x[0])] 

selected_nums = []

def dist(start,dist):
    
    return abs(start[0] - dist[0]) + abs(start[1] - dist[1])

def calc_dist(num_lst):

    num_lst = [start] + num_lst + [end]
    dist_sum = 0
    for i in range(len(num_lst)-1):

        dist_sum += dist(num_lst[i],num_lst[i+1])
    
    return dist_sum

def curr_int(idx,cnt):
    global min_dist

    if cnt == 3 :
        
        min_dist = min(min_dist,calc_dist(selected_nums))
        return

    if idx == len(nums):
        return
    
    selected_nums.append(nums[idx])
    curr_int(idx+1,cnt+1)
    selected_nums.pop()

    curr_int(idx+1,cnt)

curr_int(0,0)

if min_dist == 1e9:
    print(-1)
else:
    print(min_dist)