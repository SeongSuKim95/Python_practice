N,M = list(map(int,input().split()))

arr = [0] * N 

for i in range(N):
    arr[i] = int(input())

def checkSequenceLength():
    global arr
    arr += [0]
    arrTemp = arr[:]
    seqCnt = 1
    # print(arr)
    for i in range(N):
        if arr[i] == arr[i+1]:
            seqCnt += 1
        else : 
            # 연속된 숫자 0으로
            if seqCnt >= M : 
                for j in range(i-seqCnt+1,i+1):
                    arrTemp[j] = 0
            seqCnt = 1
    arr = arrTemp[:-1]
    # print(arr)

def gravity():
    global arr
    arrTemp = [0] * N
    tempIndex = 0
    for i in range(N):
        if arr[i] :
            arrTemp[tempIndex] = arr[i]
            tempIndex += 1
    arr = arrTemp[:]

def isSame(arr1,arr2):
    for i in range(len(arr1)):
        if arr1[i] != arr2[i]:
            return False
    return True

while True:
    arrPrevious = arr[:]
    checkSequenceLength()
    if isSame(arrPrevious,arr):
        break
    gravity()

def countNonzero():
    global arr
    cnt = 0
    for i in arr:
        if i:
            cnt += 1
    return cnt

print(countNonzero())
for i in arr:
    if i :
        print(i)


test = [1,2,3,4,5,-1,1,-1,1,1]
numbers = list(filter(lambda x: x > 0, test))

print(numbers)