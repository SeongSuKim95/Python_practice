A,B,C = list(map(int,input().split()))

trucks = [0 for _ in range(101)]
price = {1 : A, 2 : B, 3: C}
for _ in range(3):
    s,e = list(map(int,input().split()))
    for i in range(s,e):
        trucks[i] += 1
answer = 0
for i in range(100):
    if trucks[i]:
        answer += trucks[i] * price[trucks[i]]

print(answer)
