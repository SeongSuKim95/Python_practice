def solution(N, stages):
    temp1 = [0] * (N+2)
    temp2 = [0] * (N+2)
    answer = {}
    num = len(stages)
    for i in stages:
        if i != N+1:
            temp2[i] +=1
        for j in range(1,i+1):
            temp1[j] +=1
    for i in range(N):
        answer[i+1] = temp2[1:-1][i]/temp1[1:-1][i]
    
    answer = sorted(answer.keys(), key = lambda key : answer[key], reverse = True)
    return answer
# 런타임 에러: 이중 for 문,,
# 도달한 stage에 대해서는 생각하지 않는다.

def solution(N,stages):
    result = {}
    denominator = len(stages)
    
    for stage in range(1,N+1):
        if denominator != 0 :
            count = stages.count(stage)
            result[stage] = count / denominator
            denominator -= count
        else:
            result[stage] = 0
    print(sorted(result, key = lambda key : result[key], reverse = True))
    print(sorted(result.keys(), key = lambda key : result[key],reverse = True))
    return sorted(result, key = lambda key : result[key], reverse = True)