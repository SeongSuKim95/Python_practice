s = {{2},{2,1},{2,1,3},{2,1,3,4}}
# 내 풀이
def solution(s):
    temp = s[2:-2].split("},{")

    temp.sort(key=lambda x : len(x))

    answer = []
    set_dict = {}
    for i in temp:
        b = list(map(int,i.split(",")))
        for j in b:
            try:
                if set_dict[j]:
                    continue
            except:
                set_dict[j] = True
                answer.append(j)
    return answer

# 정답 풀이

def solution(s):

    s = Counter(re.findall('\d+', s))
    return list(map(int, [k for k, v in sorted(s.items(), key=lambda x: x[1], reverse=True)]))

import re
from collections import Counter