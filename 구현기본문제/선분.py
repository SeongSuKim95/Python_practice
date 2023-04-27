N = int(input())

lines = []

for _ in range(N):
    lines.append(tuple(map(int,input().split())))
    
lines.sort()
starts, ends = [],[]
for s,e in lines :
    starts.append(s)
    ends.append(e)

cnt = 1
sp = ep = 0
cs,ce = starts[sp],ends[ep]

for s,e in zip(starts,ends):
    if cs<= s and s <= ce : # 이전 선분과 겹칠 경우
        sp += 1
        cs = s
    else :
        sp += 1
        ep += 1
        cs,ce = s,e
        cnt += 1

print(cnt)