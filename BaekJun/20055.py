

N, K = map(int,input().split())

belt = list(map(int,input().split()))

for i in range(2*N):

    tmp = belt.pop()
    belt = [tmp] + belt
    print(belt[:N])

