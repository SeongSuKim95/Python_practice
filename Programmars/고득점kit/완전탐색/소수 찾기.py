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

##

primeSet = set()

def isPrime(number):
    if number in (0, 1):
        return False
    for i in range(2, number):
        if number % i == 0:
            return False

    return True


def makeCombinations(str1, str2):
    if str1 != "":
        if isPrime(int(str1)):
            primeSet.add(int(str1))
        # 여기서 리턴을 치지 않는다
    for i in range(len(str2)):
        makeCombinations(str1 + str2[i], str2[:i] + str2[i + 1:]) # 문장 combination 하는 방법


def solution(numbers):
    makeCombinations("", numbers)

    answer = len(primeSet)

    return answer
