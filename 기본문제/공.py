K = int(input())

cups = [i for i in range(4)]

for _ in range(K):
    a,b = list(map(int,input().split()))
    cups[a],cups[b] = cups[b],cups[a]

print(cups.index(1))

