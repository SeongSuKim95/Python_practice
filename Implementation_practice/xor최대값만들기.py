# Back-tracking

n, m = list(map(int,input().split()))

nums = list(map(int,input().split()))

answer = []
max_result = 0

def curr_int(idx,cnt):
    global max_result


    if cnt == m :
        result = 0   
        for elem in answer:
            result ^= elem
        max_result = max(max_result,result)
        return
    
    if idx == n :
        return
    
    answer.append(nums[idx])
    curr_int(idx+1,cnt+1)
    answer.pop()

    curr_int(idx+1,cnt)
    


curr_int(0,0)
print(max_result)
