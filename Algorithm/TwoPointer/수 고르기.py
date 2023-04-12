import sys
input = sys.stdin.readline
N,M = list(map(int,input().split()))
lst = []
for _ in range(N):
    lst.append(int(input()))
lst.sort()

p1,p2 = 0,0
answer = 2e9
while p1 < N and p2 < N:
    
    if lst[p1] - lst[p2] < M :
        p1 += 1
    else :
        answer = min(answer,lst[p1]-lst[p2])
        p2 += 1

print(answer)