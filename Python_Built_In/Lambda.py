# 함수를 define하지 않고 사용
# 매개변수를 ,를 이용하여 나열하고, : 뒤에 함수 식을 적음

def add(a,b):
    return a+b

print(add(3,7))
print((lambda a,b : a+b)(3,7))

array = [('a',6),('b',4),('c',5)]


# Lambda 식 예시
def my_key(x):
    return x[1]

print(sorted(array,key = my_key))

# key로 함수를 넣어 정렬기준을 명시할수 있음, 이때 lambda 식 사용 가능
print(sorted(array,key = lambda x : x[1]))


list1= [1,2,3,4,5]
list2 = [6,7,8,9,10]

# map
# 각각의 원소에 함수를 적용하고 싶을때 사용!
result = map(lambda a,b: a+b, list1,list2)
print(list(result))
