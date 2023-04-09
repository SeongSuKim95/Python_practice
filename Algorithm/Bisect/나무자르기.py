
N,M = list(map(int,input().split()))

trees = list(map(int,input().split()))

left, right = 0, max(trees)

def calc_tree(height):
    cnt = 0 
    for tree in trees :
        if tree - height > 0:
            cnt += tree - height 
    return cnt >= M

max_height = 0

while left <= right :
    
    mid = (left + right) // 2
    
    if calc_tree(mid):
        max_height = max(mid,max_height)
        left = mid + 1
    else :
        right = mid - 1        

print(max_height)
     
    
    
