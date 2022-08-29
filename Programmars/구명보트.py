from collections import deque

# def solution(people, limit):
    
#     people = sorted(people)
#     i , j = 0,len(people)-1
#     cnt = 0
#     while i <= j: 
#         if people[i] + people[j] <= limit:
#             cnt +=1 
#             i +=1
#             j -=1
#         else:
#             cnt+=1
#             j-=1
         
#     return cnt

def solution(people, limit):
    result = 0
    deque_people = deque(sorted(people))

    while deque_people:
        left = deque_people.popleft()
        if not deque_people:
            return result + 1
        right = deque_people.pop()
        if left + right > limit:
            deque_people.appendleft(left)
        result += 1
    return result

# 내 코드

# def solution(people, limit):
#     result = 0
#     people.sort()
    
#     # 맨 처음 값, 마지막 값 같이 태워서
#     # limit 넘기면 마지막 값 따로 태우기
#     # 첫값은 그다음 큰값이랑 같이 태워보기
#     # 탈 수있으면 둘이 태우기
#     # list 빌때까지 반복
#     i = 0
#     j = len(people) -1
#     while i <= j:
        
#         if people[i] + people[j] > limit:
#             result +=1
#             j -=1
#         elif people[i] + people[j] <= limit:
#             result +=1
#             i +=1
#             j -=1
    
#     return result
