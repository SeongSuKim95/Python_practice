# String을 등간격으로 나누기 (List comprehension 사용)

a = "aabbccddee"

length = 2

split = [a[i:i+length] for i in range(0,len(a),length)]
print(split)

# Zip 을 이용하여 비교 조합 만들기

for a,b in zip(split,split[1:]+['']):
    # 한칸 밀어주는 센스 : split[1:] + ['']
    print(a,b)


# 최대공약수
# 유클리드 호제법 사용 하거나 간단하게 math.gcd 사용하자.
from math import gcd

def lcm(x,y): # 최소 공배수
    return x*y//gcd(x,y)

# 가정문과 list comprehension을 통한 list filtering
# comprehensions create a new list

sequence = [1,1,1,1,2,3]

x = 1

filtered_list = [item for item in sequence if item != x]
print(filtered_list)
# to avoid generating a new object, use generators
filtered_list = (item for item in sequence if item != x)


# heapq 사용

# Loop내의 sorting에 의한 시간초과가 뜰때는(특히, list의 크기가 커서 시간 복잡도가 감당이 안되는 경우), heapq를 사용하자.
# heapq는 일반적인 리스트와 다르게, 가지고 있는 요소를 push,pop 할때마다 자동 정렬해준다.

import heapq as hq


# 최소 heap
heap = []
hq.heappush(heap,4)
hq.heappush(heap,7)
# [4,7]
hq.heappop(heap)
# [7]

# 최대heap

nums = [4,1,7,3,8,5]
heap = []

for num in nums:
    hq.heappush(heap,(-num,num))


# Stack 사용하기
# 어렵게 생각하지 말고, pop, append만 생각하자.
# stack을 써야하는 상황인지만 파악하면 그 다음은 쉽다..

# 짝지어 제거하기 
def solution(s):
    answer = []
    for i in s:
        if not(answer):
            answer.append(i)
        else:
            if(answer[-1] == i):
                answer.pop()
            else:
                answer.append(i)    
        print(answer)
    return not(answer)

# itertools product

from itertools import product

arr1 = [1,2,3]
arr2 = [5,6,7]
l = [(1,2),(3,4)]

print(list(product(arr1,arr2)))
print(list(product(*l)))

## String type의 정렬을 알고 있어야 풀 수 있는 문제
# List sort 시 lambda 식으로 원소들의 기준을 바꾸는 법
def solution(numbers):
    answer = ''
    numbers_str = [str(num) for num in numbers]
    numbers_str.sort(key=lambda num : num *3 ,reverse=True)
    
    return str(int(''.join(numbers_str)))