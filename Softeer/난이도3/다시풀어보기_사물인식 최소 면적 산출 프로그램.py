import sys
n, k = map(int, input().split())
color = [[] for i in range(k + 1)]
result = 1e9

for i in range(n):
    a, b, c = map(int, sys.stdin.readline().split())
    color[c].append([a, b])

def dfs(lx, ly, hx, hy, cnt, current):
    global result
    if cnt == k + 1:
        if result > current:
            result = current
        return

    for point in color[cnt]: # color 군끼리 이중 list로 묶은 후 넣어놓고 idx를 키워가며 순회
        x1, x2, y1, y2 = lx, hx, ly, hy # 현재가지에서의 최소, 최대 x,y 지점
        if point[0] < lx:
            x1 = point[0] 
        elif point[0] > hx:
            x2 = point[0]
        if point[1] < ly:
            y1 = point[1]
        elif point[1] > hy:
            y2 = point[1]

        temp = abs(x2 - x1) * abs(y2 - y1)
        if temp < result:
            dfs(x1, y1, x2, y2, cnt + 1, temp)


for p in color[1]:
    dfs(p[0], p[1], p[0], p[1], 2, 0)

print(result)