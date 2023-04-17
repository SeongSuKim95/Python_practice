from collections import deque

def solution(progresses, speeds):
    answer = []
    
    progresses,speeds = deque(progresses), deque(speeds)
    
    while progresses:
        for i in range(len(progresses)):
            progresses[i] += speeds[i]
        cnt = 0
        while progresses and progresses[0] >= 100 :
            progresses.popleft()
            speeds.popleft()
            cnt += 1
        if cnt != 0 :
            answer.append(cnt)

    return answer

# queue의 개념을 사용하여, 앞에서부터 i번째까지 확인하는 작업을 while progresses and progresses[0] >=100 과 같이 확인
# 즉, 100이상의 수가 나타나지 않을때까지 pop하여 제거

