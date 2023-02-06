from itertools import combinations
D, W, K = map(int,input().split())

data_ = [list(map(int,input().split())) for _ in range(D)]

list_ = [i for i in range(0,D)]

def combination(list,n):
    ret = []
    if n > len(list) : return ret
    if n == 0 : return [[]]
    if n == 1 :
        for i in list :
            ret.append([i])
    elif n > 1:
        for i in range(len(list)- n + 1):
            for temp in combination(list[i+1:],n-1):
                ret.append([list[i]]+ temp)
    return ret

def fill(rows,type):
    
    data_temp = [row[:] for row in data_]
    for row in rows :
        data_temp[row] = [type] * W
    cnt = 0
    for col in range(W) :
        stack = []
        for row in range(D):
            if not stack :
                stack.append(data_temp[row][col])
            else:
                if stack[-1] == data_temp[row][col]:
                    stack.append(data_temp[row][col])
                else :
                    stack = []
                    stack.append(data_temp[row][col])
            if len(stack) >= K :
                break
        if len(stack) < K :
            break
        else :
            cnt += 1
    if cnt == W :  
        return True
    else :
        return False

Flag = False
for i in range(D+1):
    combs = combination(list_,i)
    for comb in combs :
        if fill(comb,0) or fill(comb,1) : 
            Flag = True
            break
    if Flag :
        print(i)
        break
            
        
        
    
    
    