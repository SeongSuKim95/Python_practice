from collections import defaultdict

N = int(input())

names  = defaultdict(lambda : 0)
answer = ""
for _ in range(N):
    first_name = input()[0]
    if names[first_name] >= 5 :
        continue
    else :
        names[first_name] += 1
        if names[first_name] == 5 :
            answer += first_name
if not answer:
    print("PREDAJA")
else :
    print(''.join(sorted(answer)))

ㄴ
li = sorted([input()[0] for _ in range(int(input()))])
s = set(li)
res = []
for c in s:
    if li.count(c) >= 5:
        res.append(c)
print(''.join(sorted(res)) if len(res) > 0 else "PREDAJA")