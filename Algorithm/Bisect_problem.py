from bisect import bisect_left, bisect_right
from re import L

N,M = map(int,input().split())

array = list(map(int,input().split()))

# sorted = sorted(len,reversed=True)

# 탐색 범위가 넓을땐 이진탐색을 떠올리고 중간점부터 시작!

start = 0
end = max(array)

result = 0

while(start<=end):
    total = 0
    mid = (start+mid)//2
    for x in array:
        if x > mid :
            total += x -mid

    if total < M:
        end = mid -1
    
    else :
        result = mid 
        start = mid + 1

print(result)


def bisect(sorted,start,end,M):

    mid = (start + end)//2
    sum = 0 
    for x in sorted :
        sum += (x - mid)
        if sum >= M:
            end = mid + 1
            bisect(sorted,start,end,M)
        
    return 0    
