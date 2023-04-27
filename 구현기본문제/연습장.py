import heapq
import time
# N = int(input()) 

# markets = []
# pq = []

# for _ in range(N):
#     temp = tuple(map(int,input().split()))
#     markets.append(temp)
#     heapq.heappush(pq,temp)
N = int(input())
markets = []
for _ in range(N):
    markets.append(tuple(map(int,input().split())))

markets.sort()
numbers = []
for d,v in markets:
    numbers.append(v)
start = time.time()

stack = []
answer = 0

for i in range(len(numbers)):
        while stack and numbers[stack[-1]] > numbers[i]:
            stack.pop()
            answer += numbers[i]
        stack.append(i)
while stack:
        idx = stack.pop()
        answer += numbers[idx]
print(answer)
end = time.time()
print(end - start)
# pq = []
# for i in range(1000):
#     heapq.heappush(pq,(i,1))

# # 거리, 가격
# markets.sort()
# answer = 0  

# # heapq 의 전형적인 format
# for cur_d,cur_v in markets: 
#     temp = []
#     flag = False
#     while pq :
#         p_d,p_v = heapq.heappop(pq) # pq[0] 
#         temp.append((p_d,p_v)) 
#         if cur_d < p_d and cur_v > p_v :  
#             answer += p_v 
#             flag = True
#             break
#     if not flag :
#         answer += temp[0][1]
    
#     # 후보군에서 제외된 가게들을 다음 가게 판단할 때 사용하기 위해서 다시 넣어줌
#     for td,tv in temp:
#         heapq.heappush(pq,(td,tv))
#     # 현재 가게 
#     heapq.heappop(pq)

# print(answer)