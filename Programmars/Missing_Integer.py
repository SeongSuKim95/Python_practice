# 내코드
from bisect import bisect_left,bisect_right

A = [1,3,6,4,1,2]
A = list(set(A))

idx = bisect_right(A,0)
A = A[idx:]
if not A:
    print(1)
else:
    table = {i: False for i in range(A[0],A[-1]+1)}
    for i in A:
        table[i] = True

    for k,v in table.items():
        if not v:
            print(k)
            break
        if k == A[-1]:
            print(A[-1]+1)

# 정답
def solution(A):
    A.sort()
    min = 1
    for i in A:
        if i == min:
            min += 1
    return min

# 쉽게 쉽게 생각하자!