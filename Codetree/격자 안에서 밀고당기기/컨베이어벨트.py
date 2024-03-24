n,t = list(map(int,input().split()))

upperList = list(map(int,input().split()))
lowerList = list(map(int,input().split()))

def moveOneSecond(upper,lower):
    lowerTemp,upperTemp = lower[-1],upper[-1]
    
    for i in range(n-1,0,-1):
        upper[i] = upper[i-1]
    
    for i in range(n-1,0,-1):
        lower[i] = lower[i-1]
    
    upper[0],lower[0] = lowerTemp, upperTemp
    return upper, lower

def solve(upperList,lowerList):
    for _ in range(t):
        upperList, lowerList = moveOneSecond(upperList,lowerList)
    print(*upperList)
    print(*lowerList)

solve(upperList,lowerList)