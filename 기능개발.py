
def solution(progresses, speeds):
    
    # 앞에 기능이 전부 100이 되어야 True
    # 매주 몇개의 기능이 배포되는가?
    answer = []
    while progresses:
        for i in range(len(progresses)):
            progresses[i] += speeds[i]
        cnt = 0
        while progresses and progresses[0] >= 100:
            progresses.pop(0)
            speeds.pop(0)
            cnt +=1
        if cnt > 0 :
            answer.append(cnt)
    return answer

# queue의 개념을 사용하여, 앞에서부터 i번째까지 확인하는 작업을 while progresses and progresses[0] >=100 과 같이 확인
# 즉, 100이상의 수가 나타나지 않을때까지 pop하여 제거

