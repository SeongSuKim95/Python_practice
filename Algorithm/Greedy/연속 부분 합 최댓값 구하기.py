n = int(input())

lst = [0] + list(map(int,input().split()))

sum = 0
answer = -1e9
for i in range(1,n+1): # 첫번째 부터 순회하며 합이 음수가 되는 경우, 그 다음부터 다시 시작
    # 지금까지 더한 합이 음수이면!
    if sum < 0 :
        sum = lst[i]
    else:
        sum += lst[i]
    answer = max(answer,sum)
print(answer)
