from itertools import combinations
from collections import Counter

def solution(orders, course):
    answer = []

    for c in course:
        temp = [] # combination 담을 list
        for order in orders:
            combi = (combinations(sorted(order),c))
            temp += combi
        counter = Counter(temp)
        if len(counter) != 0 and max(counter.values()) != 1:
            
            # answer += [''.join(f) for f in counter] 이러면 key만 출력됨
            answer += [''.join(f) for f in counter if counter[f] == max(counter.values())]

    return sorted(answer)