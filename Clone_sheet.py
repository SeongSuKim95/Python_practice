##BFS 문제 전력망을 둘로 나누기

# from collections import defaultdict,deque


# def bfs(del_line,n,wire_dict):

#     cnt = 1
#     visited = [False] * (n+1)
#     visited[del_line[0]] = True
#     queue = deque([del_line[0]])
#     while queue:
#         curr = queue.popleft()
#         for connected in wire_dict[curr]:
#             if visited[connected] or connected == del_line[1]:
#                 continue
#             cnt +=1
#             queue.append(connected)
#             visited[connected] = True
#     return cnt

# def solution(n,wires):

#     answer = 1000
#     data = defaultdict(set)
    
#     for v1,v2 in wires:

#         data[v1].add(v2)
#         data[v2].add(v1)
    
#     for w in wires:

#         temp = bfs(w,n,data)
#         answer = min(answer,abs(n - temp - temp))

#     return answer

# n = 9 
# wires = [[1,3],[2,3],[3,4],[4,5],[4,6],[4,7],[7,8],[7,9]]
# print(solution(n,wires))


# 구명보트
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

# def solution(people, limit):
#     result = 0
#     deque_people = deque(sorted(people))

#     while deque_people:
#         print(deque_people)
#         left = deque_people.popleft()
#         if not deque_people:
#             return result + 1 # 마지막 사람
#         right = deque_people.pop()
#         if left + right > limit:
#             deque_people.appendleft(left)
#         result += 1
#     return result


# people = [70,50,80,50]
# limit = 100

# print(solution(people,limit))

# queue : popleft, pop, appendleft

# def solution(n, computers):
#     answer = 0
#     visited = [False for i in range(n)]
#     for com in range(n):
#         if visited[com] == False:
#             BFS(n, computers, com, visited)
#             answer += 1
#     return answer

# def BFS(n, computers, com, visited):
#     visited[com] = True
#     queue = []
#     queue.append(com)
#     while len(queue) != 0:
#         com = queue.pop(0)
#         visited[com] = True
#         for connect in range(n):
#             if connect != com and computers[com][connect] == 1:
#                 if visited[connect] == False:
#                     queue.append(connect)

# n = 3
# computers = [[1, 1, 0], [1, 1, 0], [0, 0, 1]]
# print(solution(n,computers))


def binary_search(array,target,start,end):

    if start > end :
        return None
    mid = (start+end)//2
    if array[mid] == target:
        return mid
    elif array[mid] < target:
        return binary_search(array,target,mid+1,end)
    elif array[mid] > target:
        return binary_search(array,target,start,mid-1)