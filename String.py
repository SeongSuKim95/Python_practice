a = "Hello"
b = "World"
print(a + " " + b)

a = "String"
print(a*3)

# String은 immutable, item assignment가 불가능

# Tuple 또한 immutable 객체이며, list와 달리 문법상 소괄호 ()를 이용

# Tuple

# 서로 다른 성질의 데이터를 묶어서 관리해야 할떄
# Ex) 최단 경로 알고리즘에서 (비용, 노드 번호)의 형태로 튜플 자료형을 자주 사용
# 데이터의 나열을 해싱(Hashing)의 키 값으로 사용해야 할때
# Tuple은 immutable하므로, key 값으로 사용할 수 있음 (list는 불가)
