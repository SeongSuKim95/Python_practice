segments = [
    (1, 5), (4, 7), (3, 6), (5, 10), 
    (9, 13), (8, 15), (12, 16)
]
n = 7
k = 11

# 주어진 좌표의 범위가 큰 경우에는
# 각 선분을 두 지점으로 나눠서
# +1, -1로 담은 뒤,
# 정렬해줍니다.
points = []
for x1, x2 in segments:
    points.append((x1, +1)) # 시작점
    points.append((x2, -1)) # 끝점

# 정렬을 진행합니다.
points.sort()

# x = k 전까지
# 각 위치에 적혀있는 숫자들의 합을 구해줍니다.
sum_val = 0
for x, v in points:
    # x가 k 이상이 되면 종료합니다.
    if x >= k:
        break

    # 적혀있는 가중치를 전부 더해줍니다.
    sum_val += v

# x = k에 겹쳐져 있는 선분의 수 = 2
print(sum_val)
