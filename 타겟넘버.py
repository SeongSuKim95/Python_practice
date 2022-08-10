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