import sys

input = sys.stdin.readline
N, S = list(map(int,input().split()))
lst = list(map(int,input().split()))

answer = N + 1 

p1,p2 = 0,0

temp_lst = [0] + lst
prefix_sum = [0] * (N+1)

for i in range(1,N+1):
    prefix_sum[i] = prefix_sum[i-1] + temp_lst[i]

while p1 < N+1 and p2 < N+1:
    if prefix_sum[p1] - prefix_sum[p2] < S :
        p1 += 1
    else : 
        answer = min(answer,p1-p2)
        p2 += 1
if answer == N + 1:
    print(0)
else:
    print(answer)