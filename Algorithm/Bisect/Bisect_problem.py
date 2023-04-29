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


def lower_bound(target):
    left = 0                             # 첫 번째 원소의 위치로 설정합니다.
    right = n - 1                        # 마지막 원소의 위치로 설정합니다.
    min_idx = n                         # 최소이므로, 답이 될 수 있는 값보다 더 큰 값으로 설정합니다.

    while left <= right:                 # [left, right]가 유효한 구간이면 계속 수행합니다.
        mid = (left + right) // 2        # 가운데 위치를 선택합니다.
        if arr[mid] >= target:           # 만약에 선택한 원소가 target보다 같거나 크다면 
            min_idx = min(min_idx, mid)  # 같거나 큰 값들의 위치 중 최솟값을 계속 갱신해줍니다.
            right = mid - 1              # 왼쪽에 조건을 만족하는 숫자가 더 있을 가능성 때문에 right를 바꿔줍니다.
        else:
            left = mid + 1               # 작은 경우라면 left를 바꿔줍니다.
    
    return min_idx                       # 조건을 만족하는 최소 index 값을 반환합니다.

def upper_bound(target):
    left = 0                             # 첫 번째 원소의 위치로 설정합니다.
    right = n - 1                        # 마지막 원소의 위치로 설정합니다.
    min_idx = n                          # 최소이므로, 답이 될 수 있는 값보다 더 큰 값으로 설정합니다.

    while left <= right:                 # [left, right]가 유효한 구간이면 계속 수행합니다.
        mid = (left + right) // 2        # 가운데 위치를 선택합니다.
        if arr[mid] > target:            # 만약에 선택한 원소가 target보다 크다면 
            min_idx = min(min_idx, mid)  # 큰 값들의 위치 중 최솟값을 계속 갱신해줍니다.
            right = mid - 1              # 왼쪽에 조건을 만족하는 숫자가 더 있을 가능성 때문에 right를 바꿔줍니다.
        else:
            left = mid + 1               # 같거나 작은 경우라면 left를 바꿔줍니다.
    
    return min_idx                       # 조건을 만족하는 최소 index 값을 반환합니다.

def custom_bound(target):
    left = 0                             # 첫 번째 원소의 위치로 설정합니다.
    right = n - 1                        # 마지막 원소의 위치로 설정합니다.
    max_idx = -1                         # 최대이므로, 답이 될 수 있는 값보다 더 작은 값으로 설정합니다.

    while left <= right:                 # [left, right]가 유효한 구간이면 계속 수행합니다.
        mid = (left + right) // 2        # 가운데 위치를 선택합니다.
        if arr[mid] <= target:           # 만약에 선택한 원소가 target보다 같거나 작다면 
            max_idx = max(max_idx, mid)  # 같거나 작은 값들의 위치 중 최댓값을 계속 갱신해줍니다.
            left = mid + 1               # 오른쪽에 조건을 만족하는 숫자가 더 있을 가능성 때문에 left를 바꿔줍니다.
        else:
            right = mid - 1              # 값이 더 큰 경우라면 right를 바꿔줍니다.
    
    return max_idx                       # 조건을 만족하는 최대 index 값을 반환합니다.

def upper_bound(target):
    
    left,right = 0, len(arr)-1
    min_idx = n
    while left <= right :
        mid = (left+right)//2
        
        if arr[mid] > target :
            min_mid = min(min_mid,mid)
            right = mid - 1
        else :
            left = mid + 1