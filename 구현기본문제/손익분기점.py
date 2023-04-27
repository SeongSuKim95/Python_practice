A,B,C = list(map(int,input().split()))


def simulate():
    if B >= C:
        print(-1)
        return
    
    print(A // (C - B) + 1)

simulate()
