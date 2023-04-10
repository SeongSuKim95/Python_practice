import sys

MAX = 1000000
N, K = list(map(int,sys.stdin.readline().split()))

line = [0 for i in range(MAX)]

length_sum = 0 
max_length = 0
for _ in range(N):
    s, e = list(map(int,sys.stdin.readline().split()))
    length_sum += e - s
    max_length = max(max_length,e)
    for i in range(s,e):
        line[i] += 1
p1,p2 = 0,0
new_line = [0] + line[:max_length]
prefix_sum = [0 for _ in range(len(new_line))]

for i in range(1,len(prefix_sum)):
    prefix_sum[i] = prefix_sum[i-1] + new_line[i]

answer = (max_length+1, max_length+1)

while p1 < max_length and p2 < max_length :
    cur = prefix_sum[p1] - prefix_sum[p2]
    if cur < K :
        p1 += 1
    elif cur == K :
        answer = min(answer,(p2,p1))
        p1 += 1
    elif cur > K :
        p2 += 1
if answer != (max_length+1,max_length+1):
    print(answer[0],answer[1])
else :
    print(0,0)