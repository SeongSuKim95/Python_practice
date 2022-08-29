def solution(operations):
    answer = []
    
    for i in operations:
        op,num = i.split(" ")
        if op == "I" :
            answer.append(int(num))
        else:
            if answer:
                if num == "1":
                    answer.remove(max(answer))
                elif num == "-1":
                    answer.remove(min(answer))
    if not answer:
        answer = [0,0]
    else:
        answer = [max(answer),min(answer)]
    return answer


## 내코드 heap 사용
import heapq

def solution(operations):
    answer = []
    
    for op in operations:
        oper,num = op.split(' ')
        if oper == "I":
            heapq.heappush(answer,int(num))
        elif oper == "D":
            if not answer :
                continue
            else:
                if num == "-1":
                    heapq.heappop(answer)            
                elif num == "1":
                    answer.remove(max(answer))
                    # 하고나서 heapify해줘야 heap이 안깨짐
    
    if not answer : 
        return [0,0]
    else:
        return [max(answer),min(answer)]