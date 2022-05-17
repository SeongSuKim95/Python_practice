# Dictionary는 Immutable 자료형만을 key로 사용할 수 있다.= dict(c =1,b=2)
# 초기화
a = dict()

a['a'] = 1
a['b'] = 2

key_list = list(a.keys())
print(key_list)

# Set
# 중복을 허용하지 않고, 순서가 없음
# list 와 dictionary형태로 초기화

data = set([1,2,3])

data.add(4) # 하나의 원소 추가
data.update([5,6]) # 여러 원소 추가
data.remove(3) # 원소 삭제

# Dictionary 와 set은 순서가 없기 때문에 indexing으로 값을 얻을 수 없음




