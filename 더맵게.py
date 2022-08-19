import heapq


def solution(scoville,K):
    
    answer = 0 
    heap = []
    for num in scoville:
        heapq.heappush(heap,num)
    
    while heap[0] < K :
        try:     
            heapq.heappush(heap, heapq.heappop(heap) + (heapq.heappop(heap) * 2))

        except IndexError: 
            return -1 
        answer += 1
    return answer


# 내코드
def solution(scoville,K):
    cnt = 0
    heapq.heapify(scoville) # heapify 해서 min heap으로 먼저 만들어 주기
    while True:
        a = heapq.heappop(scoville)
        b = heapq.heappop(scoville)
        heapq.heappush(scoville,a+2*b) # 작은 두 값을 pop하여 더한후 heap에 추가!
        cnt +=1
        if scoville[0] >= K :
            return cnt
        elif len(scoville) == 1 and scoville[0] < K: # 마지막까지 더 했는데 최상단 node가 K보다 작으면 return -1
            return -1

# 2차 코드

def solution(scoville,K):
    answer = 0
    heapq.heapify(scoville)
    while scoville[0] < K:
        if len(scoville) == 1:
            return -1
        heapq.heappush(scoville,heapq.heappop(scoville) + 2*heapq.heappop(scoville))
        answer += 1
    return answer