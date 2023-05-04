def solution(stones, k):
    # N 보다 작거나 같은 수가 연달아 K개 등장
    # NlogN
    
    left, right = 1, 2e9
    
    while left <= right :
        
        mid = (left + right) // 2
        cnt = 0
        for stone in stones : 
            if stone <= mid :
                cnt += 1
            else :
                cnt = 0
            if cnt >= k :
                break
        if cnt >= k:
            right = mid - 1 # 건널 수 없음
        else :
            left = mid + 1
    answer = left
    
    return answer