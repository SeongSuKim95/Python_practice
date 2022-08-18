# Priority queue를 구현하기 위해 자료구조 heap을 쓴다.
import heapq

# 최소 힙 기본 코드
def heapsort_min(iterable):
    h = []
    result = []

    # 모든 원소를 차례대로 힙에 삽입
    for value in iterable:
        print(value)
        heapq.heappush(h,value)

    # 힙의 모든 원소 꺼내기
    for i in range(len(h)):
        tmp = heapq.heappop(h)
        print(tmp)
        result.append(tmp)
    return result

result = heapsort_min([2,1,3,0,5,4])
print(result)

# 최대 힙 기본 코드 : - 값을 붙여서 priority를 inversion!
def heapsort_max(iterable):
    h = []
    result = []

    # 모든 원소를 차례대로 힙에 삽입
    for value in iterable:
        print(value)
        heapq.heappush(h,-value)

    # 힙의 모든 원소 꺼내기
    for i in range(len(h)):
        tmp = heapq.heappop(h)
        print(tmp)
        result.append(-tmp)
    return result

result = heapsort_max([2,1,3,0,5,4])
print(result)

# heapq 는 최솟값,최댓값을 계속 뽑아내야할때 사용할 수 있다.
# 정렬 이후 값을 뽑는 방법도 있지만 만약 새로운 값들이 계속 추가된다면, 추가될때마다 정렬을 해야하기 때문에 heapq를 사용한다.

# heap는 완전이진트리의 한 종류이며, 완전 이진트리는 리스트로 코딩이 가능하다
# 어떻게?
# root 는[0], root의 왼쪽 자식을 [1], 오른쪽 자식을 [2]라고 할때
# [1]의 왼쪽 자식은 [3], 오른쪽 자식은 [4]
# [2]의 왼쪽 자식은 [5], 오른쪽 자식은 [6]

# 즉, [x]의 왼쪽 자식은 [2x+1], 오른쪽 자식은 [2x+2]로 정리