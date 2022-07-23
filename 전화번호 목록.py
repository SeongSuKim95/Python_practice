# hash를 이용한 풀이

# 내 풀이

def solution(phone_book):
    answer = True
    
    phone_book = sorted(phone_book, key = len)
    min_length,max_length = len(phone_book[0]),len(phone_book[-1])
    for length in range(min_length,max_length):
        num_dict = {}
        for idx,i in enumerate(phone_book):
            if len(i) >= length:
                temp = i[:length]
                if temp not in num_dict.keys():
                    if length == len(i):
                        num_dict[temp] = 1
                    else :
                        num_dict[temp] = 2 
                else :
                    if num_dict[temp] ==1 :
                        answer = False

    return answer

# 다른 사람의 풀이