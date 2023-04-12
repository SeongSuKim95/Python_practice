N = int(input())

points = []

for i in range(N):
    s,e = list(map(int,input().split()))
    points.append((s,1,i))
    points.append((e,-1,i))

points.sort()
start,end = 0,0
segs = set()
answer = 0
for x,v,index in points:
    if v == 1 :
        if not segs:
            start = x
        segs.add(index)
    else : # 끝점
        segs.remove(index)
        if not segs :
            end = x
            answer = max(answer,end - start)
print(answer)