# 선택 정렬
# 가장 작은 원소를 맨 앞으로!
array = [8,2,4,5,7,6,9,10,1]

for i in range(len(array)):
    min_index = i 
    for j in range(i+1,len(array)):
        if array[min_index] > array[j]:
            min_index = j
    array[i],array[min_index] = array[min_index],array[i]
print(array)

# 삽입 정렬
# 앞쪽 원소들이 정렬되어있다고 가정하고 , 원소를 올바른 위치에 삽입!

array2 = [8,2,4,5,7,6,9,10,1]

for i in range(1, len(array2)):
    for j in range(i,0,-1): # i 부터 0 까지 감소
        if array2[j] < array2[j-1]:
            array2[j] ,array2[j-1] = array2[j-1], array2[j] # swap
        else :
            break
print(array2)

# 퀵 정렬 (NlogN)
# 퀵 정렬은 재귀적으로 수행됨!

array3 = [5,7,9,0,3,1,6,2,4,8]
array = array3
def quick_sort(array,start,end):
    if start >= end: # 원소의 개수가 1개인 경우 종료
        return
    pivot = start # 첫번째 원소를 pivot으로
    left = start + 1 # pivot을 제외한 원소중 가장 왼쪽 원소를 left
    right = end # pivot을 제외한 원소중 가장 오른쪽 원소를 right
    while(left <= right): # left와 right가 엇갈릴때까지 반복
        while(left <= end and array[left] <= array[pivot]):
            left += 1
        while(right > start and array[right] >= array[pivot]):
            right -= 1
        if (left > right): # 엇갈렸을때 pivot과 right의 원소를 swap
            array[right], array[pivot] = array[pivot],array[right]
        else :
            array[left], array[right] = array[right], array[left]
        
    # 분된 이후에 왼쪽 array와 오른쪽 array 를 분할하여 각각 정렬 수행
    # Recurise
    quick_sort(array,start,right-1)
    quick_sort(array,right+1,end)

def quick_sort2(array):
    # list가 하나 이하의 원소만 담고 있다면 종료
    if len(array) <= 1:
        return array

    pivot = array[0]
    tail = array[1:]
    left_side = [x for x in tail if x<=pivot]
    right_side = [x for x in tail if x> pivot]

    return quick_sort2(left_side)+[pivot]+quick_sort2(right_side)

quick_sort(array,0,len(array)-1)
print(array)
print(quick_sort2(array))

# 계수 정렬

# 모든 원소의 값이 0 보다 크거나 같다고 가정
array4 = [7,5,9,0,3,1,6,2,9,1,4,8,0,5,2]
# 모든 범위를 포함하는 리스트 선언(모든 값은 0으로 초기화)
count = [0] * (max(array) + 1)

for i in range(len(array)):
    count[array[i]] += 1 # 각 데이터에 해당하는 인덱스의 값 증가

for i in range(len(count)):
    for j in range(count[i]):
        print(i,end=' ')