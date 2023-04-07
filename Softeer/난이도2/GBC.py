import sys

N,M = list(map(int,sys.stdin.readline().split()))

system = [0 for _ in range(101)]
test = [0 for _ in range(101)]

prev_d = 0
for i in range(N):
    d,v = list(map(int,sys.stdin.readline().split()))
    for j in range(prev_d+1,prev_d +d+1):
        system[j] =  v
    prev_d += d

prev_d = 0
for i in range(M):
    d,v = list(map(int,sys.stdin.readline().split()))
    for j in range(prev_d+1,prev_d+d+1):
        test[j] = v
    prev_d += d

max_diff = 0
for v_s,v_t in zip(system,test):
    max_diff = max(max_diff,v_t-v_s)


print(max_diff)
