# bisect - 이진 탐색을 쉽게 구현!
# '정리된 배열'에서 특정한 원소를 찾을때 매우 효과적이다!
# bisect_left(), bisect_right() 함수의 시간 복잡도는 O(log N)

# bisect_left(a,x): 정렬 순서 유지하며 리스트 a에서 data x를 삽입 할 가장 왼쪽 index를 찾음
# bisect_right(a,x):  정렬 순서 유지하며 리스트 a에서 data x를 삽입 할 가장 오른쪽 index를 찾음

from bisect import bisect_left, bisect_right

a = [1,2,4,4,8]

x = 4

print(bisect_left(a,x)) # 2
print(bisect_right(a,x)) # 4

# bisect_left(), bisect_right() : 정렬된 리스트에서 "값이 특정 범위에 속하는 원소의 개수"를 구할때 효과적이다.

def count(a,left_value,right_value):

    left_index = bisect_left(a,left_value)
    right_index = bisect_right(a,right_value)

    return right_index - left_index

a = [1,2,3,3,3,3,4,5]

# a list에서 값이 3인 데이터의 개수
print(count(a,3,3)) # 4 

# a list에서 [-1,3] 범위에 있는 데이터의 개수
print(count(a,-1,3)) # 6