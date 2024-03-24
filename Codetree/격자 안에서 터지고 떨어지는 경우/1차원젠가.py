N = int(input())
arr = [0] * N

for i in range(N):
    arr[i] = int(input())

s1,e1 = list(map(lambda x : int(x)-1,input().split()))
s2,e2 = list(map(lambda x : int(x)-1,input().split()))

def explode(s,e):
    global arr
     
    for i in range(s,e+1):
        arr[i] = 0
    temp = [0] * N
    tempIndex = 0
    for i in range(N):
        if arr[i] : 
            temp[tempIndex] = arr[i]
            tempIndex += 1
    arr = temp[:]

def getNonZeroArray():
    global arr
    for i in range(N):
        if not arr[i]:
            arr = arr[:i][:]
            return

explode(s1,e1)
explode(s2,e2)
getNonZeroArray()
print(len(arr))
for i in range(len(arr)):
    print(arr[i])


