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