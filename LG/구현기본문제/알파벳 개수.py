string = input()
alpha_cnt = {}
for i in range(ord("a"),ord("z")+1):
    alpha_cnt[i] = 0

for i in string:
    alpha_cnt[ord(i)] += 1

print(*list(alpha_cnt.values()))