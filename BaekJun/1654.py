K,N = list(map(int,input().split()))

lines =[]
min_line = 2**31 - 1
for _ in range(K):
    line = int(input())
    lines.append(line)
    min_line = min(min_line,line)

left,right = 0,min_line

def check(length):
    cnt = 0 
    for line in lines :
        cnt += line // length 
    if cnt < N :
        return False
    else :
        return True
    
while left <= right :
    
    mid = (left+right) // 2
    cur_bool = check(mid)
    
    if cur_bool :
        left = mid + 1
    else :
        right = mid - 1

print(right)