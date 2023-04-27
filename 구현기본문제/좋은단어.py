N = int(input())
cnt = 0

def check():
    stack = []
    for i in input():
        if not stack:
            stack.append(i)
        else:
            if stack[-1] != i :
                stack.append(i)
            elif stack[-1] == i :
                stack.pop()
            
    if stack :
        return 0,stack
    else :
        return 1,stack
    
for _ in range(N):
    cnt += check()[0]
print(cnt)