# 내 코드
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


# 프로그래머스 정답

import heapq as hq

def solution(scoville, K):

    hq.heapify(scoville)
    answer = 0
    while True:
        first = hq.heappop(scoville)
        if first >= K:
            break
        if len(scoville) == 0:
            return -1
        second = hq.heappop(scoville)
        hq.heappush(scoville, first + second*2)
        answer += 1  

    return answer