from itertools import permutations as pm
import math

def solution(numbers):
    answer = 0
    num_list = []
    for j in range(1,len(numbers)+1):
        comb = list(pm(numbers,j))
        num = set([int(''.join(list(k))) for k in comb])
        for i in num:
            num_list.append(i)
    num_list = set(num_list)
    for i in num_list:
        flag = True 
        if i >=2:
            for j in range(2, int(math.sqrt(i)+1)):
                if i % j == 0:
                    flag = False

            if flag:
                answer +=1

    return answer