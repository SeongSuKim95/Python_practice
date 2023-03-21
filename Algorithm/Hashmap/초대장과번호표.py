from collections import deque

# 변수 선언 및 입력:
n, g = tuple(map(int, input().split()))

invited = [False] * n
# 각 그룹마다 초대장을 받지 못한 사람들을 관리해줍니다.
groups = [set() for _ in range(g)]
# 각 사람이 어떤 그룹에 속하는지를 관리해줍니다.
people_groups = [[] for _ in range(n)]

q = deque()
ans = 0

for i in range(g):
    nums = list(map(int, input().split()))[1:]
    for num in nums:
        num -= 1
        groups[i].add(num)
        people_groups[num].append(i)

q.append(0)
invited[0] = True
while q:
    x = q.popleft()
    ans += 1

    # x가 들어있는 그룹에서 x를 지웁니다.
    # hashset에는 그룹에서 초대받지 않은 인원만을 남깁니다.
    for g_num in people_groups[x]:
        # 해당 그룹에서 x를 지웁니다.
        groups[g_num].remove(x)
        # 초대받지 않은 인원이 한명밖에 없다면 초대합니다.
        if len(groups[g_num]) == 1:
            p_num = list(groups[g_num])[0]
            if not invited[p_num]:
                invited[p_num] = True
                q.append(p_num)

# 초대장을 받는 인원을 출력합니다.
print(ans)


## 내코드 

N, G = list(map(int,input().split()))

sets = []

for _ in range(G):
    sets.append(set(list(map(int,input().split()))[1:]))
answer = set([1])
curp = [1]
while True :
    newp = set()
    for p in curp :
        for cur_set in sets :    
            if p in cur_set:
                cur_set.remove(p)
            if len(cur_set) == 1 :
                newp |= cur_set
                cur_set = set()                    
    if not newp:
        break
    else:
        answer |= newp
        curp = newp
print(len(answer))