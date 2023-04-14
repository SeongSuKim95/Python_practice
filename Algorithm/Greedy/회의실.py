N = int(input())

rooms = []

for _ in range(N):
    rooms.append(tuple(map(int,input().split())))

rooms.sort(key = lambda x : x[1])

e = -1
cnt = 0
for cs,ce in rooms :
    if cs >= e :
        e = ce
        cnt += 1
print(cnt)
    