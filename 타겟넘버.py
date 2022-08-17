# BFS 풀이

def solution(numbers,target):
    answer = 0
    leaves = [0]
    
    for num in numbers:
        tmp = []
        for parent in leaves:
            tmp.append(parent+num)
            tmp.append(parent-num)
        leaves = tmp
    return leaves.count(target)            


# DFS 풀이
def DFS(numbers,target,depth):
    
    answer = 0
    if depth == len(numbers):
        print(numbers)
        if sum(numbers) == target:
            return 1
        else:
            return 0 
    else:
        answer += DFS(numbers,target,depth+1)
        numbers[depth] *= -1
        answer += DFS(numbers,target,depth+1)
        return answer

def solution(numbers,target):
    answer = DFS(numbers,target,0)
    return answer

# 내코드

def DFS(numbers,target,depth,sum):
    answer = 0
    if depth == len(numbers):
        if sum == target:
            return 1
        else:
            return 0 
    else:
        temp1 = sum + numbers[depth]
        answer += DFS(numbers,target,depth+1,temp1)
        temp2 = sum - numbers[depth]
        answer += DFS(numbers,target,depth+1,temp2)
    
    return answer

def solution(numbers,target):
    answer = DFS(numbers,target,0,0)
    return answer

# BFS

from collections import deque

def solution(numbers,target):
    
    queue = deque(numbers)
    answer = [[] for _ in range(len(numbers))]
    answer[0].append(numbers[0])
    answer[0].append(-1*numbers[0])
    queue.popleft()
    idx = 0
    while queue:
        num = queue.popleft()
        for i in answer[idx]:
            answer[idx+1].append(i+num)
            answer[idx+1].append(i-num)
        idx +=1
    return answer[-1].count(target)

## 같은것을 수행하는 코드임에도 너무.. 다르다..
## leaves = [0]이라고 선언후, tmp라는 list에 update를 한 후 leaves로 교체하면 된다