import sys

from collections import defaultdict

N,M = list(map(int,input().split()))

weights = [0] + list(map(int,input().split()))

friends = {i:[] for i in range(1,N+1)}

for _ in range(M):
    f1,f2 = tuple(map(int,input().split()))
    friends[f1].append(weights[f2])
    friends[f2].append(weights[f1])

cnt = 0

for k,v in friends.items():
    if not v:
        cnt += 1
    else :
        if weights[k] > max(v):
            cnt += 1

print(cnt)

import sys

n, m = map(int, sys.stdin.readline().split())
w = list(map(int, sys.stdin.readline().split()))
g = [list(map(int, sys.stdin.readline().split())) for x in range(m)]

# [0] 리스트를 n+1개 만큼 만든다.
# 순서를 구분하기 위해 0번째의 수에 0을 넣어 제외한다.
cnt = [1 for _ in range(n+1)]
cnt[0]=0

# 그룹 수 만큼 반복한다.
# A,B가 들 수 있는 무게를 g 리스트에서 가져와 w에 넣어 비교한다.
# 비교할때 더 무거운 무게를 들 수 없다면 0을 부여한다.
for i in range(m):
    if w[g[i][0]-1] > w[g[i][1]-1]:
            cnt[g[i][1]] = 0

    elif w[g[i][0]-1] < w[g[i][1]-1]:
            cnt[g[i][0]] = 0

	# 똑같은 무게를 들 수 있다면 둘다 0을 부여
    else:
        cnt[g[i][0]] = 0
        cnt[g[i][1]] = 0


# cnt 리스트에 1의 개수를 출력한다.
print(cnt.count(1))