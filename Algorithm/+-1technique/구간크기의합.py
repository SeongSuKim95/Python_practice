N = int(input())
points = []

for _ in range(N):
    s,e = list(map(int,input().split()))
    points.append((s,1))
    points.append((e,-1))

points.sort()
pv,px = 0,0
cv = 0
ans = 0
for cx,v in points:
    pv = cv
    cv = pv + v
    if pv == 0: # 새로 시작
        px = cx
    elif pv > 0 and cv == 0 :
        ans += cx - px
    
print(ans)


## 

# 변수 선언 및 입력:
n = int(input())
segments = [
    tuple(map(int, input().split()))
    for _ in range(n)
]

# 각 선분을 두 지점으로 나눠 담은 뒤,
# 정렬해줍니다.
# 이때 (x좌표, +1-1값, 선분 번호)
# 형태로 넣어줍니다.
# +1은 시작점
# -1은 끝점을 뜻합니다.
points = []
for i, (x1, x2) in enumerate(segments):
    points.append((x1, +1, i)) # 시작점
    points.append((x2, -1, i)) # 끝점

# 정렬을 진행합니다.
points.sort()

# 각 점을 순서대로 순회합니다.
# 등장하고 아직 사라지지 않은
# 선분을 hashset으로 관리합니다.
segs = set()

ans = 0       # 구간 크기의 합을 저장합니다.
start_x = -1  # 현재 합쳐진 구간의 시작 x값을 기록해줍니다.
for x, v, index in points:
    # 시작점인 경우입니다.
    if v == +1:
        # 남아있는 선분이 없다면
        # 합쳐진 구간의 시작이므로
        # start_x값을 갱신해줍니다.
        if not segs:
            start_x = x    
        
        # 해당 선분 번호를 hashset에 넣어줍니다.
        segs.add(index)

    # 끝점인 경우입니다.
    else:
        # 해당 선분을 제거합니다.
        segs.remove(index)

        # 남아있는 선분이 없다면
        # 합쳐진 구간의 끝이므로
        # 답을 갱신해줍니다.
        if not segs:
            end_x = x
            ans += end_x - start_x

print(ans)