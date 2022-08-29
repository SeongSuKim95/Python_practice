# itertyo

from itertools import permutations, combinations, product, combinations_with_replacement

data = ['A','B','C']

# 순열

print(list(permutations(data,3)))
# iterable 객체에서 r개의 데이터를 중복 없이 뽑아 일렬로 나열하는 모든 경우(순열)제시
# class 이므로 객체 초기화 후, list 자료형으로 변환 해야함
# <class itertools.permutations>
# [('A', 'B', 'C'), ('A', 'C', 'B'), ('B', 'A', 'C'), ('B', 'C', 'A'), ('C', 'A', 'B'), ('C', 'B', 'A')]

# 중복 허용
print(list(product(data,repeat=3)))
# [('A', 'A', 'A'), ('A', 'A', 'B'), ('A', 'A', 'C'), ('A', 'B', 'A'), ('A', 'B', 'B'), ('A', 'B', 'C'), ('A', 'C', 'A'), ('A', 'C', 'B'), ('A', 'C', 'C'), ('B', 'A', 'A'), ('B', 'A', 'B'), ('B', 'A', 'C'), ('B', 'B', 'A'), ('B', 'B', 'B'), ('B', 'B', 'C'), ('B', 'C', 'A'), ('B', 'C', 'B'), ('B', 'C', 'C'), ('C', 'A', 'A'), ('C', 'A', 'B'), ('C', 'A', 'C'), ('C', 'B', 'A'), ('C', 'B', 'B'), ('C', 'B', 'C'), ('C', 'C', 'A'), ('C', 'C', 'B'), ('C', 'C', 'C')]

# 조합

print(list(combinations(data,2))) 
# iterable 객체에서 r개의 데이터를 중복 없이 뽑아 순서 없이 일렬로 나열하는 모든 경우(조합)제시 
# class 이므로 객체 초기화 후, list 자료형으로 변환 해야함
# <class itertools.combinations>
# [('A', 'B'), ('A', 'C'), ('B', 'C')]

# 중복 허용
print(list(combinations_with_replacement(data,2)))
#[('A', 'A'), ('A', 'B'), ('A', 'C'), ('B', 'B'), ('B', 'C'), ('C', 'C')]