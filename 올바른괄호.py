def solution(s):
    
    stack = []
    for i in s:
        if i == "(":
            stack.append(0)
        else:
            try:
                stack.pop() # pop left를 할필요가 없다..
            except:
                return False
    if not stack:
        return True
    else:
        return False

# 처음에 stack.pop(0)때문에 효율성 통과를 못했는데, 그냥 pop()을 해주면 된다. popleft(0)의 시간복잡도가 다름을 감안해야함