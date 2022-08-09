def solution(s, n):
    answer = ''
    # 97 --> 122
    # 65 --> 90
    for i in s :
        temp = ord(i) + n 
        if i.isupper():
            if temp > 90:
                temp -= 26
            answer += chr(temp)
        elif i.islower():
            if temp > 122 :
                temp -= 26
            answer += chr(temp)
        else:
            answer += " "
    return answer


# 알파벳 소문자의 ASCII CODE : 97 - 122 (a-z)
# 알파벳 대문자의 ASCII CODE : 65 - 90 (A-Z)
# 문자의 ASCII CODE : ord() , ASCII CODE 를 문자로 : chr() 
