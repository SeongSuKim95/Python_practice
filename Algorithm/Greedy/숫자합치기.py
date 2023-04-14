import heapq

N = int(input())

lst = list(map(int,input().split()))

answer = 0
heap = []

for elem in lst:
    heapq.heappush(heap,elem)
# list 원소들을 heappush로 넣어주어야함!

while len(heap) > 1 :

    a = heapq.heappop(heap)
    b = heapq.heappop(heap)
    answer += a+b
    heapq.heappush(heap,a+b)

print(answer)