from collections import deque

def solution(queue1, queue2):
    target_sum = (sum(queue1) + sum(queue2)) / 2
    print(target_sum)
    left_sum = sum(queue1)
    queue1 = deque(queue1)
    queue2 = deque(queue2)

    answer = 0
    while queue1 and queue2:
        if left_sum < target_sum:
            tmp = queue2.popleft()
            left_sum += tmp
            queue1.append(tmp)
            answer += 1
        elif left_sum > target_sum:
            left_sum -= queue1.popleft()
            answer += 1
        else:
            return answer
        print(f"queue1:{queue1},queue2:{queue2},left_sum:{left_sum}")
    else:
        return -1


# 포인트
# 1. 탐색 종료 시점이 두 queue의 합이 같을때 또는 두 queue중 하나라도 빈 큐가 생겼을때라는것
# 2. 두 queue중 하나의 합계 값만 알아도 된다는 것


from collections import deque
def solution(queue1, queue2):      
    if sum(queue1)>sum(queue2):
        tmp=queue1
        queue1=queue2
        queue2=tmp
        
    q=queue1+queue2
    
    
    start=0
    end=len(queue1)-1
    cnt=0
    
    s1=sum(queue1)
    s2=sum(queue2)
    
    while start<=end and end<len(q):
        if s1==s2:
            return cnt
        elif s1<s2 and end+1<len(q):
            end+=1
            s1+=q[end]
            s2-=q[end]
        else:
            s1-=q[start]
            s2+=q[start]
            start+=1
        
        
        cnt+=1
    
        return -1