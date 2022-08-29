
def solution(s):
    
    answer = ''
    flag = True
    answer = []
    for i in s:
        
        if i == ' ':
            flag = True
            answer.append(i)
        else : 
            if flag == True:
                answer.append(i.upper())
                flag = False
            else :
                if i.isalpha():
                    answer.append(i.lower())
    
    return ''.join(answer)
        