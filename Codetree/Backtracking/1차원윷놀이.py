# 변수 선언 및 입력:
n, m, k = tuple(map(int, input().split()))
nums = list(map(int, input().split()))
pieces = [1 for _ in range(k)] # 말들의 현재 위치

ans = 0

def calc():
    score = 0
    for piece in pieces:
        if piece >= m :
            score += 1
    return score

def select(cnt): # 턴 별로 선택
    global ans
    if cnt == n :
        ans = max(ans,calc())
        return 
    
    for i in range(k) : # k개의 말에 대하여
        if pieces[i] >= m :
            continue
        pieces[i] += nums[cnt]
        select(cnt+1)
        pieces[i] -= nums[cnt]


select(0)
print(ans)