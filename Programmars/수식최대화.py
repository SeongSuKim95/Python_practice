from itertools import permutations
import re

expression = "100-200*300-500+20"

def solution(expression):

    answer = 0 
    num = re.split('\+|\-|\*',expression)
    opr = re.split('[0-9]+',expression)[1:-1] # [0-9] = [0123456789], matching 반복 끝날때까지
    
    for order in permutations("-+*",3):
        nc = num.copy()
        oc = opr.copy()
        for o in order:
            idx = 0
            while idx < len(oc):
                if oc[idx] == o :
                    nc[idx] = str(eval(''.join((nc[idx],o,nc[idx+1]))))
                    nc.pop(idx+1)
                    oc.pop(idx)
                    idx -=1
                idx +=1
        answer = max(answer,abs(int(nc[0])))

    return answer

print(solution(expression))