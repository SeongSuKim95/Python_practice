
# N = map(int,input())

# num = list(map(int,input().split()))

# equations = list(map(int,input().split()))

# 내 코드
N = 6
num = [1,2,3,4,5,6]
equations = [2,1,1,1]
answer = []

def dfs(idx,equations,num,sum):

    global answer
    if idx == len(num):
        answer.append(sum)
        return 

    cur = num[idx]
    print(cur)
    for i in range(4):
        if equations[i] != 0 :
            temp = equations.copy()
            if i == 0 :
                temp[i] -=1
                dfs(idx+1,temp,num,sum+cur)
            elif i== 1:
                temp[i] -=1
                dfs(idx+1,temp,num,sum-cur)
            elif i==2:
                temp[i] -=1
                dfs(idx+1,temp,num,sum*cur)
            elif i==3:
                temp[i] -=1
                dfs(idx+1,temp,num,sum//cur)
            


def solution(N,num,equations):

    # 개수가 0 보다 큰 부호들에 대해서 dfs
    global answer
    start = 1
    dfs(start,equations,num,num[0])
    print(max(answer))
    print(min(answer))

solution(N,num,equations)
