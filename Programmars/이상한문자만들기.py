def solution(s):
    answer = ''
    word_list = s.split(' ')
    
    for word in word_list:
        word = word.lower()
        temp = ''
        for idx,alpha in enumerate(word):
            if idx % 2 == 0 :
                temp += alpha.upper()
            else:
                temp += alpha
        answer += temp + ' '
    return answer[:-1]

# s.split() 과 s.split(' ')의 차이
# 문자열 양끝의 공백을 고려하는지 안하는지가 갈린다.
test_str = ' s s s s sss '

print(test_str.split(),test_str.split(' '))