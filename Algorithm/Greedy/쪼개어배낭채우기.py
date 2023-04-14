N,M = list(map(int,input().split()))

jewels = []

for _ in range(N):

    w,v = list(map(int,input().split()))
    jewels.append((v/w,w,v))

jewels.sort(reverse=True)
answer = 0

for pv,w,v in jewels:
    if M - w >= 0:
        answer += v
        M -= w
    else:
        answer += M * pv
        break

print("{:.3f}".format(answer))