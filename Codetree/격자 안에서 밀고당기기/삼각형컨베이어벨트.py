n, t = list(map(int,input().split()))

firstList = list(map(int,input().split()))
secondList = list(map(int,input().split()))
thirdList = list(map(int,input().split()))

def moveRight1Second(first,second,third):

    firstTemp,secondTemp,thirdTemp = first[-1],second[-1],third[-1]
    
    for i in range(n-1,0,-1):
        # 우측 당기기
        first[i],second[i],third[i] = first[i-1],second[i-1],third[i-1]
    # 좌측 채우기
    first[0],second[0],third[0] = thirdTemp,firstTemp,secondTemp

    return first,second,third

for _ in range(t):
    firstList,secondList,thirdList = moveRight1Second(firstList,secondList,thirdList)

print(*firstList)
print(*secondList)
print(*thirdList)