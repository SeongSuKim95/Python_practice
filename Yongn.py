
from itertools import combinations

def solution(factory):
    answer = []
    item = {i for i in range(0,len(factory[1]))}
    for i in range(1,len(factory[1])+1):
        for j in combinations(item,i):
            fact = {p: False for p in range(len(factory))}
            for index in j:
                for idx,k in enumerate(factory):
                    if k[index]:
                        fact[idx] = True
            if sum(list(fact.values())) == len(factory):
                return i 


factory = [[1,1,0,0,0,0,0,0],[0,0,0,0,1,1,0,0],[0,0,1,1,0,0,1,0],[0,0,0,0,0,0,0,1]]

print(solution(factory))