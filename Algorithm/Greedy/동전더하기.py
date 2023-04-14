n, k = list(map(int,input().split()))
coins = []

for _ in range(n):
    coins.append(int(input()))

coins.sort(reverse=True)
cnt = 0

for coin in coins :
    while k >= coin :
        k -= coin
        cnt += 1
print(cnt)
