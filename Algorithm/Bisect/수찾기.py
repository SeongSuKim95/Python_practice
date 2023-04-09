N = int(input())

nums = sorted(list(map(int,input().split())))

M = int(input())
targets = list(map(int,input().split()))

def bisect(target,start,end):
    mid = 0
    while start <= end:
        
        mid = (start + end) // 2
        
        if target == nums[mid] :
            return 1
        elif target > nums[mid] :
            start = mid + 1
        elif target < nums[mid] :
            end = mid - 1
    return 0

for target in targets:
     print(bisect(target,0,N-1))
     