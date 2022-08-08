def solution(arr):
    stack = []
    for i in arr:
        if not stack:
            stack.append(i)
        else:
            if i == stack[-1]:
                continue
            else:
                stack.append(i)
    return stack