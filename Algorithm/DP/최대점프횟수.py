n = int(input())

jumps = list(map(int,input().split()))

dp = [-1e9 for _ in range(n)]
# dp[i] = 점프하여 도착한 마리막 위치를 i라 했을 때, 가능한 최대 점프 횟수
dp[0] = 0
for i in range(1,n):
    for j in range(i):
        if dp[j] == -1e9:
            continue
        if j+ jumps[j] >= i :
            dp[i] = max(dp[j]+1,dp[i])

print(max(dp))

# 동일한 상태 정의 : 선택한 부분 수열에서 마지막 원소의 위치, 선택한 부분 수열의 길이
# 마지막 원소의 위치를 고정하고 부분 수열의 길이를 최대로 하는 점화식 세우기
# 최댓값 구하는 문제이므로 dp테이블 INT_MIN으로 초기화