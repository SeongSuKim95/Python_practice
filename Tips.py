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