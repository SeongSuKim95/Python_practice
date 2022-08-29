def solution(arr):
    answer = 1
    for i in arr:
        answer = lcm(answer,i)
    return answer

def lcm(a,b):
    answer = 1
    for i in range(1,max(a,b)):
        if a % i == 0 and b % i == 0 and i >= answer:
            answer = i
    
    return answer * a//answer * b//answer
