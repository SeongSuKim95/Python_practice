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


def binary_search(array,target,start,end): #탐색을 수행하고자 하는 배열 정보, 찾고자 하는 데이터, 탐색범위
    if start > end :
        return None
    mid = int((start+end)/2)  # (start+end) // 2
    if array[mid] == target :
        return mid
    elif array[mid] < target :
        return binary_search(array,target,mid+1,end)
    elif array[mid] > target :
        return binary_search(array,target,start,mid-1)


def binary_search_2(array,target,start,end):
    while start <= end:
        mid = (start+end)//2
        if array[mid] == target:
            return mid
        elif array[mid] > target :
            end = mid -1
        else :
            start = mid + 1
    return None
 

# n , target = list(map(int, input().split()))

# array = list(map(int, input().split()))

# result = binary_search(array,target,0,n-1)

# if result == None :
#     print("원소가 존재하지 않음")
# else :
#     print(result+1)

#값이 특정 범위에 속하는 데이터 개수 구하기

def count_by_range(array, left_value, right_value):
    right_index = bisect_right(array,right_value)
    left_index = bisect_left(array,left_value)
    return right_index - left_index
a = [1,2,3,3,3,3,4,4,8,9]

print(count_by_range(a,4,4)) #값이 4인 데이터 개수 출력
print(count_by_range(a,1,9)) #값이[-1,3] 범위에 있는 데이터 개수 출력

# Parametric search : 최적화 문제를 결정 문제('예'혹은'아니오')로 바꾸어 해결하는 방식
# 특정한 조건을 만족하는 가장 알맞은 값을 빠르게 찾는 최적화 문제
