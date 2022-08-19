# hash를 이용한 풀이

# 내 풀이
from collections import defaultdict

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

# 내풀이 2

def solution(phone_book):
    
    answer = True
    phone_book.sort(key=lambda x : len(x))
    
    max_len,min_len = len(phone_book[-1]),len(phone_book[0])
  
    for i in range(min_len,max_len+1):
        temp = defaultdict(int)
        for j in phone_book:
            if temp[j[:i]] :
                return False
            else:
                if len(j) == i:
                    temp[j[:i]] = 1

    return answer