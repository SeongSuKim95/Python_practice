N = int(input())

answer = ''

patterns = ['1','22','333','4444']
cnt = 0

def curr_str(depth):
    global cnt, answer

    if depth == N :
        cnt += 1 
        return

    if depth > N:
        return

    for pattern in patterns:
        temp = answer
        answer = answer + pattern
        curr_str(depth + len(pattern))
        answer = temp

curr_str(0)

print(cnt)

'''
Global 변수 사용하지 않고 Return값으로 count하기

def choose(idx_num): #들어갈 값의 인덱스
    if idx_num == n:#0~n-1인덱스에 값이 들어가고 n을 보면 끝
        return 1
    elif idx_num > n: #n보다 뒤를 보면 조건 성립 x
        return 0
    
    total =0
    for i in range(1,5):#1~4들어감
        total += choose(idx_num+i)
    
    return total

'''
